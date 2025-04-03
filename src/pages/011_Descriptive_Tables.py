import plotly.express as px
import polars as pl
import streamlit as st

import scripts.script_functions as functs


def display_graph(fig_title: str, fig, fig_dta: pl.DataFrame):
    st.write(f"## {fig_title}")
    st.plotly_chart(fig, use_container_width=True)
    chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
    if chart_display:
        st.write(f"#### {fig_title} Dataframe")
        st.dataframe(fig_dta)
        st.write(f"Dataframe shape: {fig_dta.shape}")


def main() -> None:
    page_title = "Descriptive Graphs"
    functs.set_page_configs(page_title)
    df = functs.load_dta()
    # get total articles by company
    df_by_day = df.group_by(pl.col("day")).agg(pl.len().alias("day_count")).sort("day")
    df_by_week = df.group_by(pl.col("week")).agg(pl.len().alias("week_count")).sort("week")
    st.write("## Events by Day")
    st.write(df_by_day)
    st.write("## Events by Week")
    st.write(df_by_week)
    # display simple bar graphs for events by day
    fig_title = "Bar Graph of Events by Day"
    st.write(f"## {fig_title}")
    fig = px.bar(df_by_day, x="day", y="day_count")
    display_graph(fig_title, fig, df_by_day)
    # display simple bar graphs for events by day
    fig_title = "Bar Graph of Events by Week"
    st.write(f"## {fig_title}")
    fig = px.bar(df_by_week, x="week", y="week_count")
    display_graph(fig_title, fig, df_by_week)
    # get total word count by company
    st.sidebar.write(functs.print_updated_time())  # PROGRESSTRACKING:
    print(functs.print_updated_time())  # PROGRESSTRACKING:


main()
