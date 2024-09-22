import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Создание Dash-приложения
app = Dash(__name__)

data = {
    "train": ([[2, 2, 1], [1, 1, 1], [1, 1, 2], [1, 2, 2]], ["b", "a", "a", "b"]),
    "test": ([[1, 2, 2]], ['b'])
}

# Создание DataFrame
def create_dataframe(data, label, set_name):
    df = pd.DataFrame(data, columns=["Feature 1", "Feature 2", "Feature 3"])
    df['Prediction'] = label
    df['Set'] = set_name
    return df

# Создание DataFrame для тренировочной и контрольной выборок
df_train = create_dataframe(*data["train"], 'Train')
df_test = create_dataframe(*data["test"], 'Test')

# Объединяем обе выборки
df = pd.concat([df_train, df_test], ignore_index=True)

# Создание 3D графика
fig = px.scatter_3d(df, x="Feature 1", y="Feature 2", z="Feature 3", color="Prediction",
                    title="График предсказаний модели в 3D",
                    labels={"Feature 1": "Признак 1", "Feature 2": "Признак 2", "Feature 3": "Признак 3"},
                    color_discrete_map={"a": "blue", "b": "red"})

app.layout = html.Div(children=[
    html.H1(children='Hello Dash for RandomForestClassifier'),
    dcc.Graph(id='example-graph', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)
