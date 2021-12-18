import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    title="New Tab Dash",
    assets_url_path="assets/",
    external_stylesheets=[dbc.themes.LITERA],  # QUARTZ
    suppress_callback_exceptions=True,
)

server = app.server
