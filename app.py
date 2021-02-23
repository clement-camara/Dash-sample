import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine
from config import name, user, password, host
from request import request
from dash.dependencies import Input, Output

# 'values', 'countries', 'flows', 'products'
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

conn = create_engine(f'postgresql://{user}:{password}@{host}/{name}')
df = pd.read_sql(request, conn)

fig = px.bar(df, x="years", y="values", color="countries", template='plotly_dark')

app.layout = html.Div(children=[
    html.H1(children='TRANSITION ENERGETIQUE'),

    html.Div(children='''
        Importation des énergies renouvelables
    '''),

    dcc.Graph(className='row',
              id='example-graph',
              figure=fig
              ),
])


if __name__ == '__main__':
    app.run_server(debug=True)
