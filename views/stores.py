from dash import html

def stores_layout(df):
       layout = html.Div("Stores Page",
                     style={'font-size':20,
                            'textAlign':'center'
                            }
                     )
       return layout