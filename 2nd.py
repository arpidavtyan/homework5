import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import quandl
import plotly.graph_objs as go
import pandas as pd
from plotly.offline import plot, iplot
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)
from Graphs import figure4
from Graphs import figure3


quandl.ApiConfig.api_key = "xhp4sV5t6fVz3gVq8sxH"

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})


facebook = quandl.get("WIKI/FB",transformation="rdiff")
amazon = quandl.get("WIKI/AMZN",transformation="rdiff")
sandridge_energy = quandl.get("WIKI/SD",transformation="rdiff")
steelcase = quandl.get("WIKI/SCS",transformation="rdiff")
ashford = quandl.get("WIKI/AHT",transformation="rdiff")

facebook_price = round(facebook.Close[1:5,],3)
amazon_price = round(amazon.Close[1:5,],3)
sandridge_energy_price = round(sandridge_energy.Close[1:5,],3)
steelcase_price = round(steelcase.Close[1:5,],3)
ashford_price=round(ashford.Close[1:5,],3)

churnGraph = dcc.Graph(id="churn", figure=figure4)
mapGraph = dcc.Graph(id="roadmap", figure=figure3)

gdp_us = quandl.get("FRED/GDP")

app.layout = html.Div([
    html.Div([
        html.Div([

            html.H1("Homework 3",
            style={
            'textAlign': 'center',
            'color': 'red'
                }),

            html.Div([
                html.Div([dcc.RadioItems(
                    id = 'rbutton',
                options=[
                {'label': 'Employee Churn', 'value': 'churn'},
                {'label': 'Startup RoadMap', 'value': 'map'}
                ],  
            ),
        ], className='three columns'),
       
        html.Div([], id = 'gd1',className='nine columns')
    ],
    className='row'
            ),
     ])
        ],
        className='row'),
    html.Div([
        html.Div([
            dcc.Dropdown(
        id = 'stock',
        options=[   
            {'label': 'facebook', 'value': 'fb_price'},
            {'label': 'amazon', 'value': 'amz_price'},
            {'label': 'sandridge_energy', 'value': 'sd_price'},
            {'label': 'steelcase', 'value': 'scs_price'},
            {'label': 'ashford', 'value': 'aht_price'}
        ],
        multi=True,
        placeholder="Please, select a stock",
        className='row'),
    html.Div([], id = "gd2", className = 'ten rows')
    ]),
    html.Div([
    dcc.Graph(id='graph_gdp'),
    
    dcc.RangeSlider(
    id = 'option',
    min=0,
    max=len(gdp_us.index),
    step = 5,
    value=[0, len(gdp_us.index)]
    ),
    html.Div(id='output-container-range-slider')
])      ])
])


@app.callback(
    Output('graph_gdp', 'figure'),
    [Input('option', 'value')]
)
def update_graph(input_value):
    transformed_index = gdp_us.index[input_value[0]:input_value[1]]
    transformed_values = gdp_us.Value[input_value[0]:input_value[1]]

    sliderData = [go.Scatter(x=transformed_index,y=transformed_values,fill="tozeroy")]
    sliderLayout = dict(title = 'US GDP over time')
    sliderFigure_gdp = dict(data=sliderData, layout = sliderLayout)
    return sliderFigure_gdp

@app.callback(
    Output(component_id='gd2',component_property='children'),
    [Input(component_id='stock',component_property='value')]
)
def update_graph(graphs):
    headerArray = []
    cellsArray = []
    boxData = []
    if len(graphs) > 1 and len(graphs)< 3:
        for value in graphs:
            if(value=="fb_price"):
                headerArray.append('fb_price')
                cellsArray.append(facebook_price)
                boxData.append(go.Box(x=facebook_price, name = 'fb_price'))
            elif(value=="amz_price"):
                headerArray.append('amz_price')
                cellsArray.append(amazon_price)
                boxData.append(go.Box(x=amazon_price, name = 'amz_price'))
            elif(value=="sd_proce"):
                headerArray.append('sd_price')
                cellsArray.append(sandridge_energy_price)
                boxData.append(go.Box(x=sandridge_energy_price, name = 'sd_price'))
            elif(value=="scs_price"):
                headerArray.append('scs_price')
                cellsArray.append(steelcase_price)
                boxData.append(go.Box(x=steelcase_price, name = 'scs_price'))
            elif(value=="aht_price"):
                headerArray.append('aht_price')
                cellsArray.append(ashford_price)
                boxData.append(go.Box(x=ashford_price, name = 'aht_price'))

        parentDiv = html.Div([getBox(boxData), getTable(headerArray, cellsArray)], className='row' )
        return parentDiv
    else: return  'Max 2 stocks'

def getBox(boxData):
    boxLayout = dict(title = 'Stocks Distribution Figure')
    boxFigure = dict(data=boxData, layout=boxLayout)
    boxstocks = dcc.Graph(id="box", figure=boxFigure)
    return boxstocks

def getTable(headerArray, cellsArray):
    header = dict(values = headerArray,
            fill = dict(color='red')
            )
    cells = dict(values = cellsArray,
            fill = dict(color = ["white","blue"])
            )
    traceTable = go.Table(header = header, cells=cells)
    dataTable = [traceTable]
    layoutTable = dict(width=500, height=300)
    figureTable = dict(data=dataTable, layout=layoutTable)
    tablestocks = dcc.Graph(id="stock_prices", figure=figureTable)
    return tablestocks

if __name__ == '__main__':
    app.run_server()