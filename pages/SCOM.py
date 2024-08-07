import streamlit as st
from servers_from_scom import get_sample_data
from Home import users
from streamlit_authenticator import Authenticate


auth = Authenticate(
    users,
    "streamlit_auth",
    "streamlit_auth_key",
    cookie_expiry_days=30
)
name, authentication_status, username = auth.login()

if authentication_status:
    st.title("SCOM: The Microsoft Monitoring Suite")

    # Seperate section for Data
    with st.container():
        # Defining Tabs
        tab1, tab2, tab3 = st.tabs(["SCOM 2016", "SCOM 2019", "SCOM 2022"])

        # 2016 tab
        with tab1:
            st.subheader("Servers monitored in SCOM 2016")
            st.caption("Number of servers: 2000")
            data = get_sample_data()
            st.dataframe(data)

        # 2019 tab
        with tab2:
            st.subheader("Servers monitored in SCOM 2019")
            st.caption("Number of servers: 1500")
            data = get_sample_data()
            st.dataframe(data)

        # 2022 tab
        with tab3:
            st.subheader("Servers monitored in SCOM 2022")
            st.caption("Number of servers: 2000")
            data = get_sample_data()
            st.dataframe(data)
        # Logout button
        if st.session_state["authentication_status"]:
            auth.logout("Logout", "sidebar")

elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
