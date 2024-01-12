from dash import html
import dash_ag_grid as dag

def stores_layout(df):
       # layout = html.Div("Stores Page",
       #               style={'font-size':20,
       #                      'textAlign':'center'
       #                      }
       #               )

       layout = html.Div([
                          dag.AgGrid(id="stores-grid",
                                     rowData=df.to_dict("records"),
                                     className='ag-theme-alpine font',
                                     columnDefs=[{
                                                 'field':i,

                                                 } for i in df.columns
                                                 ],
                                     defColumnOptions=[]
                                     )
                        ])

       return layout