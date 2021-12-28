from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Dash mandatory imports
from app import app

# Components import
from components import components

# Globals for Sunrise/Sunset Calculation
LAT = None
LONG = None
UTC = None

# ---------------------------------------------------------------------------------------


def serve_layout() -> list:
    """
    Defines and returns the layout components for the landing page.
    """

    container = [
        dbc.Row(
            id="info-bar",
            children=getInfoBarContent(),
            style={"height": "50px"},
            className="d-flex justify-content-center align-items-center",
        ),
        html.Br(),
        dbc.Row(
            id="content-row",
            children=[
                dbc.Col(
                    id="content-pane",
                    children=[getLeftPaneContent()],
                    width=9,
                ),
                dbc.Col(
                    id="image-pane",
                    children=[],
                    width=3,
                    style={"width": "22%", "margin-left": "3%"},
                ),
            ],
        ),
    ]

    return container


def getInfoBarContent() -> list:
    """
    Defines and returns the content of the
    From left to right I would like the following items.

    Day of week
    Date
    Time
    Sunrise
    Sunset
    Moonphase
    """

    dow = dbc.Col(
        html.P(
            components.getCurrentDate(),
            id="info-content-date",
            style={"text-align": "center", "padding-top": "10px"},
        ),
        width=3,
        className="d-flex justify-content-center my-auto",
    )
    sunrise = dbc.Col(
        html.P(
            "00:00",
            id="info-content-sunrise-time",
            style={"text-align": "center", "padding-top": "10px"},
        ),
        width=3,
        className="d-flex justify-content-center my-auto",
    )
    sunset = dbc.Col(
        html.P(
            "00:00",
            id="info-content-sunset-time",
            style={"text-align": "center", "padding-top": "10px"},
        ),
        width=3,
        className="d-flex justify-content-center my-auto",
    )
    moon_phase = dbc.Col(
        html.P(
            "Full moon",
            id="info-content-moon-phase",
            style={"text-align": "center", "padding-top": "10px"},
        ),
        width=3,
        className="d-flex justify-content-center my-auto",
    )

    return [dow, sunrise, sunset, moon_phase]


def getLeftPaneContent() -> any:
    """
    Defines and returns the elements within the left hand side pane.
    In order I would like the following items:

    Title bar -- centered (maybe this can be the time)
    Subtext -- centered (welcome message)

    Row of 5 columns
    """
    return dbc.Row(
        id="content-container",
        children=[
            dbc.Row(
                id="content-header",
                children=[
                    html.Br(style={"margin": "10px"}),
                    html.H1(
                        components.getCurrentTime(),
                        id="time-header",
                        style={"text-align": "center"},
                    ),
                    html.P(
                        id="greeting-message",
                        children=components.getDynamicGreeting(),
                        style={"text-align": "center"},
                    ),
                    html.Br(style={"margin": "30px"}),
                ],
                className="d-flex justify-content-center",
            ),
            dbc.Row(id="categories-row", children=components.createCategories()),
        ],
    )


def getRightPaneContent() -> any:
    """
    Defines and returns the elements within the right hand side pane.
    """
    return html.Div(id="image-view", style={"background-color": "blue"})
