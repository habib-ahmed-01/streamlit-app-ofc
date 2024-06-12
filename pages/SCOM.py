import streamlit as st
from servers_from_scom import get_sample_data

st.title("SCOM: The Microsoft Monitoring Suite")


# Seperate section for Data
with st.container():
    # Defining Tabs
    tab1, tab2, tab3 = st.tabs(["SCOM 2016","SCOM 2019","SCOM 2022"])

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
