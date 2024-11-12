import joblib
import click
import numpy as np
import pandas as pd

# Третий узел DAG
@click.command()
@click.option("--infile", default="df2.job", prompt="df2.job", help="Входной файл.")
@click.option("--outfile", default="df3.job", prompt="df3.job", help="Выходной файл.")

def run(infile, outfile):
    """ Увеличиваем размер выборки"""
    df=joblib.load(infile)
    df['species'] = df['species'].astype('category').cat.codes

    # Оставляем только числовые столбцы для агрегации
    numeric_columns = df.select_dtypes(include=[np.number])

    # Добавляем обратно категорию species для группировки
    numeric_columns['species'] = df['species']

    # Рассчитаем среднее и стандартное отклонение для каждого вида (только для числовых столбцов)
    distribution_params = numeric_columns.groupby('species').agg(['mean', 'std']).reset_index()

    # Список имен столбцов
    distribution_params.columns = ['species'] + [f'{col}_{stat}' for col, stat in distribution_params.columns[1:]]

    # Количество новых записей для генерации
    num_samples = 10000 

    def generate_samples(means, stds, num_samples):
        return np.random.normal(loc=means, scale=stds, size=(num_samples, len(means)))

    # Генерация данных
    samples = []
    species_list = []
    for _, params in distribution_params.iterrows():
        means = params.filter(like='mean').values
        stds = params.filter(like='std').values
        generated_samples = generate_samples(means, stds, num_samples)
        samples.append(generated_samples)
        species_list.append(np.full(num_samples, params['species']))

# Объединяем сгенерированные данные в один DataFrame
    generated_columns = [col for col in distribution_params.columns if '_mean' in col]
    df_generated = pd.DataFrame(np.vstack(samples), columns=generated_columns)

# Добавляем столбец с метками видов
    df_generated['species'] = np.concatenate(species_list)

    df_generated.columns = [col.replace('_mean', '') for col in df_generated.columns]

    joblib.dump(df_generated, outfile)
    click.echo(f"Создан файл: {outfile}!")

if __name__ == '__main__':
    run()

