import streamlit as st

st.set_page_config(
    layout="centered",
    initial_sidebar_state="expanded"
)
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