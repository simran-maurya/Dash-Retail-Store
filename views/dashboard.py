from dash import html

def dashboard_layout(df):
       layout = html.Div("Dashboard Page",
                     style={'font-size':20,
                            'textAlign':'center'
                            }
                     )
       return layout