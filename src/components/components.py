# Dash imports
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

# Application imports
from app import app

# Method imports
from json import load
from math import radians, pi, cos, sin, acos, tan
from datetime import datetime as dt

# ---------------------------------------------------------------------------------------


def createCategories() -> any:
    """
    Reads the bookmarks json and compiles all bookmarks into a column that is returned.
    FLow:
    1. Read json
    2. loop through each key within the dict and create a category.
    """

    # Reading the JSON data.
    bookmark_data = None
    categories = list()

    try:
        f = open("src/bookmarks.json")
        bookmark_data = load(f)
        f.close
    except FileNotFoundError:
        return dcc.Markdown("❌ JSON data not found.❌ ")
    except:
        return dcc.Markdown("❌ Error reading JSON.❌ ")

    for key in bookmark_data.keys():
        categories.append(createCategory(key, bookmark_data[key]))

    return categories


def createCategory(title: str, bookmarks: dict) -> any:
    """
    Creates a named category with the links and images provided.

    Each category consists of a title header and the bookmarks themselves.
    The `group_items` variable is built first and represents the list of bookmarks
    that are added within the category.
    ```
    """
    group_items = list()

    # Building the list of bookmarks within the category
    for key in bookmarks.keys():

        current_bookmark = bookmarks[key]

        # Breakdown for readability
        name = key
        url = current_bookmark["link"]
        image_path = current_bookmark["image_path"]

        # Appending a dbc list group item to our group_items list
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
                        ],
                        className="gx-1",
                    )
                ],
                href=url,
                className="border-0 d-flex justify-content-center align-middle",
            )
        )

    # Then return a column representing the category with a title and list group of the bookmarks
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
                children=group_items,
                className="d-flex justify-content-center",
            ),
        ],
        style={"width": "20%"},
    )


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


def getMoonPhase(utc: int) -> str:
    """
    Estimates the current moon phase based on today's date.

    lunar_day indicates the duration of days of a lunar cycle.
    """
    now = dt.now()
    lunar_day = 29.53058770576
    y2k_new_moon = dt(year=2000, month=1, day=6, hour=(18 + utc), minute=14)

    seconds_delta = (now - y2k_new_moon).total_seconds()

    mod_val = seconds_delta % lunar_day

    phases = [
        ("New", 0, 1),
        ("Waxing Crescent", 1, 6.38264692644),
        ("First Quarter", 6.38264692644, 8.38264692644),
        ("Waxing Gibbous", 8.38264692644, 13.76529385288),
        ("Full", 13.76529385288, 15.76529385288),
        ("Waning Gibbous", 15.76529385288, 21.14794077932),
        ("Last Quarter", 21.14794077932, 23.14794077932),
        ("Waning Crescent", 23.14794077932, 28.53058770576),
        ("New", 28.53058770576, 29.53058770576),
    ]

    for phase in phases:
        if mod_val >= phase[1] and mod_val <= phase[2]:
            return phase[0]


def getSunriseSunsetTime(latitude: float, longitude: float, utc: int) -> any:
    """
    Calculates approximately what time the sun rises and sets
    based on the global LOCATION tuple.

    ## Variable Name Explanations
    gamma = fractional_year
    doy = numerical day of the year (ex: 182)
    eqtime = equation of time (in minutes)
    decl = solar declination angle
    ha = hour angle
    z_angle = zenith angle


    calculation source: https://gml.noaa.gov/grad/solcalc/solareqns.PDF
    """
    sunrise = None
    snoon = None
    sunset = None
    z_angle = 90.833  # Set specifically for the correction of atmospheric refraction
    current_time = dt.now()

    # Converting degree entries to radians
    longitude = radians(longitude)
    latitude = radians(latitude)

    doy = current_time.timetuple().tm_yday

    gamma = radians(((2 * pi) / 365) * (doy - 1 + ((current_time.hour - 12) / 24)))

    # Calculating Equation of time in minutes
    eqtime = 229.18 * (
        0.000075
        + 0.001868 * cos(gamma)
        - 0.032077 * sin(gamma)
        - 0.014615 * cos(2 * gamma)
        - 0.040849 * sin(2 * gamma)
    )

    # Calculating solar declination angle
    decl = (
        0.006918
        - 0.39912 * cos(gamma)
        + 0.070257 * sin(gamma)
        - 0.006758 * cos(2 * gamma)
        + 0.000907 * sin(2 * gamma)
        - 0.002697 * cos(3 * gamma)
        + 0.00148 * sin(3 * gamma)
    )

    # # Calculating time offset in minutes
    # time_offset = eqtime + 4 * longitude - 60 * utc

    # tst = (
    #     current_time.hour * 60
    #     + current_time.minute
    #     + current_time.second / 60
    #     + time_offset
    # )

    # # Calculating the solar hour angle
    # ha = (tst / 4) - 180

    sunrise_ha = acos(
        (((cos(z_angle)) / (cos(latitude) * cos(decl))) - (tan(latitude) * tan(decl)))
    )

    sunset_ha = -1 * acos(
        (((cos(z_angle)) / (cos(latitude) * cos(decl))) - (tan(latitude) * tan(decl)))
    )

    sunrise = 720 - 4 * (longitude + sunrise_ha) - eqtime
    snoon = 720 - 4 * longitude - eqtime
    sunset = 720 - 4 * (longitude + sunset_ha) - eqtime

    return sunrise, snoon, sunset
