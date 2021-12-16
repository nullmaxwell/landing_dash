from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app


def serve_layout() -> list:
    """
    Defines and returns the layout for the landing page.
    """

    return [getInfoComponent()]


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
