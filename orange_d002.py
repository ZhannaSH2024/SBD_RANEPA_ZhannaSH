import joblib
import sys
import click

# Второй узел DAG
@click.command()
@click.option("--infile", default="df1.job", prompt="df1.job", help="Входной файл.")
@click.option("--outfile", default="df2.job", prompt="df2.job", help="Выходной файл.")

def run(infile, outfile):
    """Очищает выборку от NaN"""
    df = joblib.load(infile)
    df = df.dropna()
    joblib.dump(df, outfile)
    click.echo(f"Создан файл: {outfile}!")

if __name__ == '__main__':
    run()

