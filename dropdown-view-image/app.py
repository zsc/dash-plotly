import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    dcc.Dropdown(
	options=[
	    {'label': 'house', 'value': 'Pictures/house.png'},
	    {'label': 'city_brain', 'value': 'Pictures/city_brain.jpg'},
	],
	value='Pictures/city_brain.jpg',
        id='dropdown',
    ),
    html.Button('Submit', id='button'),
    html.Div(id='output-container-button',
	 children=[]
    )
])


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('dropdown', 'value')])
def update_output(n_clicks, value):
    return [dcc.Graph(figure=go.Figure(
	    data=[
		go.Scatter(
		    x=[0, 1920],
		    y=[0, 1080],
		    hoveron = 'fills',
		    name = 'Human #{0}'.format(0+1),
		    text = 'confidence: {:.2f}'.format(0.5),
		    mode='lines',
		    line = dict(width=4,color='red'),
		    showlegend = False
		)
	    ],
	    layout=go.Layout(
		title='Sputnik Detection',
		margin = dict(l=40, r=0, t=40, b=30),
		images = [
		      dict(
		      source= app.get_asset_url('{}'.format(value)),
		      xref= "x",
		      yref= "y", 
		      x= 0,
		      y= 1080,
		      sizex= 1920,
		      sizey= 1080,
		      sizing= "contain",
		      opacity= 0.7,
		      visible = True,
		      layer= "below")]
	    )
	),
	style={'height': 600},
	id='my-graph'
      )
   ]

if __name__ == '__main__':
    app.run_server(debug=True)
