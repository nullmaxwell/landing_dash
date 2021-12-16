from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app
from views import landing


# Basic layout definition
app.layout = dbc.Container(
    id="main-content", children=[dcc.Location(id="url", refresh=False)]
)


# Callback to change which page to display
@app.callback(Output("main-content", "children"), [Input("url", "pathname")])
def display_page(pathname) -> any:
    """
    Placeholder description
    """
    if pathname == "/":
        return landing.serve_layout()
    if pathname == "/other":
        return "404 page under construction"


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050, debug=True)
