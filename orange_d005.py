import joblib
import sys
import click
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

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
    joblib.dump(df, outfile)
    click.echo(f"Создан файл: {outfile}!")

if __name__ == '__main__':
    run()
