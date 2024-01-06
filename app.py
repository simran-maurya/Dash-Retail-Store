import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State
from views import navbar, dashboard, stores, accounts
from dash.exceptions import PreventUpdate
import pandas as pd 
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,'/assets/style.css'])

class Singleton:
    __shared_state = dict()
    df = pd.DataFrame()
    new_df = pd.DataFrame()
    edited_df = pd.DataFrame()

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return self.df

    def read_file(self):
        self.df = pd.read_csv('assets/store_details.csv')
        self.new_df = pd.DataFrame()
        self.edited_df = pd.DataFrame()

singleton_instance = Singleton()
singleton_instance.read_file()


nav_bar = navbar.navbar_layout()
content = html.Div(id="page-content")
app.layout = html.Div([dcc.Store(id='root-url',storage_type='memory',clear_data=True),
                       dcc.Store(id='loaded',storage_type='memory',clear_data=True,data=False),
                       dcc.Location(id='url',refresh=False),
                       nav_bar,
                       content
                    ])


@app.callback(
    [Output('root-url','data'),
     Output('loaded','data')],
    [Input('url','pathname')],
    [State('loaded','data')]
)
def update_root_url(url,loaded):
    """
    Description: Function is used to dynamically instantiate 
                 the root-url when the webapp is launched
    """
    if not loaded:
        return url, True
    else: 
        raise PreventUpdate


@app.callback(
    [Output('page-content','children')],
    [Input('url','pathname')],
    [State('root-url','data'),
     State('loaded','data')]
)
def display_page(pathname,root_url,is_loaded):
    """
    Description: Updates the page content when URL changes

    """
    if not is_loaded:
        return [html.Div("Welcome to the Store",style={'textAlign':'center'})]

    if is_loaded:
        if (pathname == root_url + 'dashboard'):
            return [dashboard.dashboard_layout(singleton_instance.df)]
        
        elif (pathname == root_url + 'stores'):
            return [stores.stores_layout(singleton_instance.df)]
        
        elif (pathname == root_url + 'accounts'):
            return [accounts.accounts_layout(singleton_instance.df)]
        
        else: 
            return [html.Div("Unauthorized Access",style={'textAlign':'center'})]


if __name__ == '__main__':
    app.run_server(debug=True)