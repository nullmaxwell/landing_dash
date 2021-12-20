from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Dash mandatory imports
from app import app

# Components import
from components import components


def serve_layout() -> list:
    """
    Defines and returns the layout for the landing page.
    """
    container = dbc.Container(
        id="main-container", children=[html.Div(children=[getMainPanel()])]
    )

    return [container]


def getMainPanel() -> any:
    """
    Defines and returns the main content components.
    """

    return dbc.Container(
        id="content",
        children=[
            dbc.Col(id="info-bar", children=[], width=12),
            dbc.Col(id="left-pane", children=[getLeftPaneContent()], width=10),
            dbc.Col(id="image-pane", children=[], width=2),
        ],
    )


def getInfoBarContent() -> any:
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
    return None


def getLeftPaneContent() -> any:
    """
    Defines and returns the elements within the left hand side pane.
    In order I would like the following items:

    Title bar -- centered (maybe this can be the time)
    Subtext -- centered (welcome message)

    Row of 5 columns
    """
    return dbc.Row(
        id="left-container",
        children=[
            components.createCategory(
                title="Category1",
                bookmarks=[
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 1",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                ],
            ),
            components.createCategory(
                title="Category2",
                bookmarks=[
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 1",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                ],
            ),
            components.createCategory(
                title="Category3",
                bookmarks=[
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 1",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                ],
            ),
            components.createCategory(
                title="Category4",
                bookmarks=[
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 1",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                ],
            ),
            components.createCategory(
                title="Category5",
                bookmarks=[
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 1",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                    (
                        "icons/io.polymail.ios-large.png",
                        "Test 2",
                        "https://google.com",
                    ),
                ],
            ),
        ],
    )


def getRightPaneContent() -> any:
    """
    Defines and returns the elements within the right hand side pane.
    """
    return html.Div(id="image-view", style={"background-color": "blue"})


def getInfoComponent() -> any:
    """
    Defines and returns a basic information component to ensure that the app works.
    """
    comp = dcc.Markdown(
        """
        # Welcome to your dash application!

        If you are seeing this message then you are good to go ✅

        If you cannot see this message then you are a liar. ❌
        """
    )

    return comp
