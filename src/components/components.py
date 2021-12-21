# Dash imports
from dash import html
import dash_bootstrap_components as dbc

# Application imports
from app import app


def createCategory(title: str, bookmarks: list) -> any:
    """
    Creates a named category with the links and images provided.

    bookmarks parameter is a list of tuples, it must be received in the following format:
    ```
    bookmarks = [
        ("images/image_path1", "title1", "url1"),
        ("images/image_path2", "title2", "url2"),
    ]
    ```
    """
    return dbc.Col(
        id=title,
        children=[
            html.P(
                title,
                id=title + "-title",
                className="d-flex justify-content-center",
            ),
            dbc.ListGroup(
                id=title + "-bookmarks",
                children=createBookmarks(bookmarks),
                className="d-flex justify-content-center",
            ),
        ],
        style={"width": "20%"},
    )


def createBookmarks(bookmarks: list) -> any:
    """
    Generates a ListGroup of links with their respective images.

    This assumes that the bookmarks parameter is a list of tuples.
    """

    group_items = list()

    # Loops through each tuple and constructs a listgroup item for it
    for bookmark in bookmarks:

        # Breakdown for readability
        image_path = bookmark[0]
        name = bookmark[1]
        url = bookmark[2]

        # Appending a list group item to
        group_items.append(
            dbc.ListGroupItem(
                children=[
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    id=name + "-logo",
                                    src=app.get_asset_url(image_path),
                                    style={"height": "35px"},
                                ),
                                className="d-flex justify-content-center",
                                width=4,
                            ),
                            dbc.Col(
                                name,
                                id=name + "title",
                                className="d-flex justify-content-center",
                                width=8,
                                style={"padding-top": "6%"},
                            ),
                        ]
                    )
                ],
                href=url,
                className="border-0 d-flex justify-content-center align-middle",
            )
        )
        pass

    return group_items


def getCurrentTime() -> str:
    """
    Simple datetime wrapper that gets the current time and
    returns it as a formatted string.

    # Returns:
    "HH:MM"
    """
    return dt.now().strftime("%H:%M")


def getCurrentDate() -> str:
    """
    Datetime wrapper that gets the current date and
    returns it as a formatted string.

    # Returns:
    "DD MONTH YEAR"
    """
    return dt.now().strftime("%d %B %Y")


def getDynamicGreeting() -> str:
    """
    Determines greeting text string based on the current time.
    """

    time = dt.now()
    relative_time = None

    if time.hour < 12:
        relative_time = "morning"
    elif time.hour >= 12 and time.hour < 16:
        relative_time = "afternoon"
    else:
        relative_time = "evening"

    return "Good " + relative_time + " friend, drink more water!"
