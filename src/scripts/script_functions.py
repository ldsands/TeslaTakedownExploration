from pathlib import Path

import plotly.express as px
import polars as pl
import streamlit as st


def set_page_configs(page_title) -> None:
    """
    Configures the Streamlit page settings.

    This function sets the layout to wide, the page title to "Basic Descriptive Graphs",
    and the initial sidebar state to expanded. Additionally, it hides the Streamlit
    main menu and footer for a cleaner interface.

    Returns:
        None
    """
    # can only set this once, first thing to set
    st.set_page_config(
        page_title=page_title,
        layout="wide",
        initial_sidebar_state="expanded",
    )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def print_updated_time():
    """
    Returns the current time formatted as a string indicating the last update time.

    This function retrieves the current system time, formats it to a string in the
    format "HH:MM:SS", and returns a message indicating the last update time.

    Returns:
        str: A string message indicating the last update time in the format "App last updated at HH:MM:SS".
    """
    from datetime import datetime

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"App last updated at {current_time}"


def load_dta():
    def get_dirs() -> Path:
        parent_dir = Path(__file__).parent.parent
        dataframe_dir = parent_dir / "Dataframes"
        return dataframe_dir

    def load_dta_path(dataframe_dir) -> pl.DataFrame:
        return pl.read_parquet((dataframe_dir / "TeslaTakedown_events.parquet"))

    def remove_missing_values(dta: pl.DataFrame) -> pl.DataFrame:
        return dta.drop_nulls()

    dataframe_dir = get_dirs()
    dta = load_dta_path(dataframe_dir)
    dta = remove_missing_values(dta)
    return dta


def display_graph_dta(fig_dta: pl.DataFrame, fig_title):
    """
    Display a dataframe in a Streamlit app with an optional checkbox.

    Parameters:
    fig_dta (pl.DataFrame): The dataframe to be displayed.
    fig_title (str): The title of the figure or dataframe.

    Returns:
    None
    """
    chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
    if chart_display:
        st.write(f"#### {fig_title} Dataframe")
        st.dataframe(fig_dta)
        st.write(f"Dataframe shape: {fig_dta.shape}")


# TESTCODE:
def line_graph(fig_dta: pl.DataFrame, x_col: str, y_col: str, color_col: str, title: str):
    fig = px.line(fig_dta, x=x_col, y=y_col, color=color_col, title=title)
    return fig


"""
#FF0000
#aa0000
#550000
#00FF00
#32CD32
#006400
#0000FF
#000099
#000033
#FFFF00
#999900
#333300
#00FFFF
#009999
#003333
#FF00FF
#990099
#330033
#808080
#C0C0C0
#1a1a1a
#800000
#4d0000
#1a0000
#808000
#4d4d00
#1a1a00
#008000
#003300
#001100
#800080
#4d004d
#1a001a
#008080
#004d4d
#001a1a
#000080
#00004d
#5b5bff
#FF8C00
#663800
#331c00
#DAA520
#836313
#eccc7d
#FF1493
#6e003b
#ff79c1

Red         #FF0000     #aa0000     #550000
Lime        #00FF00     #32CD32     #006400
Blue        #0000FF     #000099     #000033
Yellow      #FFFF00     #999900     #333300
Cyan        #00FFFF     #009999     #003333
Magenta     #FF00FF     #990099     #330033
Gray        #808080     #C0C0C0     #1a1a1a
Maroon      #800000     #4d0000     #1a0000
Olive       #808000     #4d4d00     #1a1a00
Green       #008000     #003300     #001100
Purple      #800080     #4d004d     #1a001a
Teal        #008080     #004d4d     #001a1a
Navy        #000080     #00004d     #5b5bff
darkorange  #FF8C00     #663800     #331c00
black       #000000     #000000     #000000

Cool colors
Lime        #00FF00     #32CD32     #006400
Blue        #0000FF     #000099     #000033
Cyan        #00FFFF     #009999     #003333
Olive       #808000     #4d4d00     #1a1a00
Green       #008000     #003300     #001100
Purple      #800080     #4d004d     #1a001a
Teal        #008080     #004d4d     #001a1a
Navy        #000080     #00004d     #5b5bff

Warm colors
Red         #FF0000     #aa0000     #550000
Yellow      #FFFF00     #999900     #333300
Magenta     #FF00FF     #990099     #330033
Maroon      #800000     #4d0000     #1a0000
darkorange  #FF8C00     #663800     #331c00

Other color groups
Gray        #808080     #C0C0C0     #1a1a1a
"""
