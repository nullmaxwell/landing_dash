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
            html.H3(
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


def createBookmarks(bookmarks) -> any:
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
                                    style={"height": "50px"},
                                ),
                                className="d-flex justify-content-center",
                                width=6,
                            ),
                            dbc.Col(
                                name,
                                id=name + "title",
                                className="d-flex justify-content-center",
                                width=6,
                            ),
                        ]
                    )
                ],
                href=url,
            )
        )
        pass

    return group_items
