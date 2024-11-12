import joblib
import sys
import click
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Четвертый узел DAG
@click.command()
@click.option("--infile", default="df4.job", prompt="df4.job", help="Входной файл.")
@click.option("--outfile", default="df5.job", prompt="df5.job", help="Выходной файл.")

def run(infile, outfile):
    df=joblib.load(infile)
    X = df.drop('species', axis=1)
    y = df['species']

# Разделяем данные на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Байесовский классификатор
    nb_classifier = GaussianNB()
    nb_classifier.fit(X_train, y_train)

    nb_predictions = nb_classifier.predict(X_test)

    accuracy = accuracy_score(y_test, nb_predictions)
    print(f"Точность Байесовского классификатора: {accuracy:.4f}")
    conf_matrix = confusion_matrix(y_test, nb_predictions)

    plt.figure(figsize=(8, 6))
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Adelie', 'Chinstrap', 'Gentoo'],
            yticklabels=['Adelie', 'Chinstrap', 'Gentoo'])
    plt.title('Матрица ошибок (Confusion Matrix)')
    plt.xlabel('Предсказано')
    plt.ylabel('Фактическое')
    plt.show()

    joblib.dump(nb_predictions, outfile)
    click.echo(f"Создан файл: {outfile}!")

if __name__ == '__main__':
    run()
