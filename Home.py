import streamlit as st
import streamlit_authenticator as stauth

st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded"
)

# Configure the authenticator
users = {
    "usernames": {
        "user1": {
            "email": "user1@example.com",
            "name": "User One",
            "password": "password123"  # Use hashed passwords in production
        },
        "user2": {
            "email": "user2@example.com",
            "name": "User Two",
            "password": "password456"  # Use hashed passwords in production
        }
    }
}

auth = stauth.Authenticate(
    users,
    "streamlit_auth",
    "streamlit_auth_key",
    cookie_expiry_days=30
)
# st.session_state
name, authentication_status, username = auth.login()

if authentication_status:
    st.title("Merck: ICINGA & SCOM")

    with st.container(border=True):
        st.markdown(
            '''
    
            ## ICINGA Monitoring Tool
        
            ### About ICINGA
            
            ICINGA is an open-source monitoring system that checks the availability of your network resources, notifies users of outages, and generates performance data for reporting. Designed to monitor large, complex environments, ICINGA provides powerful features including:
            
            ### Current Monitoring Statistics
    
            Servers in ICINGA monitoring : 16000+    
            
            ### CSV File Editing for ICINGA Import Sources
            
            This application also includes a feature to edit CSV files that are used as import sources for ICINGA. 
            - *MSZ Servers*
            - *Hardware ILOs*
            
            By leveraging this tool, you can efficiently manage your ICINGA import sources, ensuring your monitoring setup remains accurate and comprehensive.
            '''
        )

    with st.container(border=True):
        st.markdown(
            '''
            ## SCOM Monitoring Tool
            ### About SCOM 
            System Center Operations Manager (SCOM) is a comprehensive data center monitoring tool from Microsoft. 
            SCOM provides an extensive array of features to monitor services, devices, and operations across various environments:
            
            ### Current Monitoring Statistics
            
            Servers in ICINGA monitoring : 16000+
            
            By utilizing SCOM, we can proactively manage our IT infrastructure, quickly identifying and addressing potential issues to ensure uninterrupted service and optimal performance.
            '''
        )

        # Logout button
        if st.session_state["authentication_status"]:
            auth.logout("Logout", "sidebar")
            # st.rerun()
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
