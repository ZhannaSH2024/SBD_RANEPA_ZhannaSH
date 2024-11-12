import joblib
import sys
import click
import matplotlib.pyplot as plt
import seaborn as sns

# Четвертый узел DAG
@click.command()
@click.option("--infile", default="df3.job", prompt="df3.job", help="Входной файл.")
@click.option("--outfile", default="df4.job", prompt="df4.job", help="Выходной файл.")

def run(infile, outfile):
    df=joblib.load(infile)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='bill_length_mm', y='bill_depth_mm', hue='species', palette='deep')
    plt.title('Характеристики пингвинов в зависимости от их вида')
    plt.xlabel('Длина клюва (мм)')
    plt.ylabel('Глубина клюва (мм)')
    plt.legend(title='Вид', labels=['Adelie', 'Chinstrap', 'Gentoo'])
    plt.show()

    joblib.dump(df, outfile)
    click.echo(f"Создан файл: {outfile}!")

if __name__ == '__main__':
    run()

