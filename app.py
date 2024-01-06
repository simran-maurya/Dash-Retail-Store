import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,'/assets/style.css'])

app.layout = html.Div(dbc.Button("CLICK HERE"))

if __name__ == '__main__':
    app.run_server(debug=True)