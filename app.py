import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, State
from views import navbar, dashboard, stores, accounts
from dash.exceptions import PreventUpdate

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP,'/assets/style.css'])

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
            return [dashboard.layout]
        
        elif (pathname == root_url + 'stores'):
            return [stores.layout]
        
        elif (pathname == root_url + 'accounts'):
            return [accounts.layout]
        
        else: 
            return [html.Div("Unauthorized Access",style={'textAlign':'center'})]

if __name__ == '__main__':
    app.run_server(debug=True)