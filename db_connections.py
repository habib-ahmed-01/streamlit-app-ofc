import streamlit as st


@st.cache_resource
def icinga_pg_conn():
    return st.connection("postgresql", type="sql")
