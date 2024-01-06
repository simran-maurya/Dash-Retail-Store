from dash import html
import dash_bootstrap_components as dbc

def navbar_layout():
    nav_list = [
                ("Dashboard","dashboard"),
                ("Stores","stores"),
                ("Accounts","accounts"),
                ]
    
    navbar = html.Div([dbc.Row([
                                dbc.Col(html.Div(html.Img(src="/assets/logo.jpg",
                                                          style={'width':'100px',
                                                                 'height':'50px',
                                                                 'padding':'0px'
                                                                }
                                                          )
                                                )
                                        ),
                                dbc.Col(html.Div(html.H3("Retail Store Dashboard",style={'margin':'20px 0px 0px 0px'}),
                                                 style={'width':'400px',
                                                        'font-size':'15px',
                                                        'font-weight':'500',
                                                        'color':'black',
                                                        'flex-grow':'1',
                                                        'text-align':'center',
                                                        }
                                                 )
                                        ),
                                dbc.Col(html.Div("User Details",
                                                 style={'width':'400px',
                                                        'font-size':'15px',
                                                        'font-weight':'500',
                                                        'color':'black',
                                                        'flex-grow':'1',
                                                        'text-align':'end',
                                                        }
                                                 )
                                        ),
                                ],
                                style={'diplay':'flex',
                                       'backgroundColor':'#EDEDED',
                                       'align-items':'center',
                                       'padding':'4px',
                                       }
                                ),
                      dbc.Row([
                                dbc.Col(dbc.Nav([
                                                dbc.NavItem(
                                                            dbc.NavLink(f"{val[0]}",
                                                                        href=f"{val[1]}",
                                                                        style={'color':'white'}
                                                                        ),
                                                            style={'margin-right':'1px',
                                                                   'font-size':'12px'
                                                                  }           
                                                            ) for val in nav_list
                                                ],
                                                horizontal='start',
                                                vertical=False,
                                                pills=False,
                                                style={'backgroundColor':'blue',
                                                       'boxShadow':'0px 3px 6px #00000029',
                                                       'opacity':'1',
                                                       'padding':'10px',
                                                       'width':'100%',
                                                       'height':'50px',
                                                       'margin':'0',
                                                       },
                                                ),
                                                width=12,
                                        )
                            ],
                            style={'position':'relative'},
                            ),
                    ]
                )

    return navbar