import streamlit as st


def set_page_configs():
    st.set_page_config(
        layout="wide",
        page_title="Oil Companies Streamlit Page Descriptions",
        page_icon="👋",
        initial_sidebar_state="expanded",
    )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def write_markdown():
    st.write("# Oil Companies Streamlit Home Page")

    st.sidebar.success("Select page from above to access the different graph categories.")
    st.markdown(
        """
    ## Descriptives

    This page displays some basic descriptive tables and graphs.

    """
    )


def main():
    set_page_configs()
    write_markdown()


main()
