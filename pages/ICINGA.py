import streamlit as st
from urls import get_url_data, process_url_rows
from ilos import get_ilo_data, process_ilo_rows
from msz import get_msz_data, process_msz_rows
import pandas as pd
from upload_ilo_csv import save_ilo_csv, save_msz_csv
from Home import auth

name, authentication_status, username = auth.login()

if authentication_status:
    st.set_page_config(layout="wide")
    st.title("ICINGA: The Open Source Monitoring Tool")
    if st.button("Clear Cache", type="primary"):
        st.cache_data.clear()
    # Separate section for Data
    with st.container():
        # Defining Tabs
        tab1, tab2, tab3 = st.tabs(["URLs", "MSZ Servers", "Hardware ILOs"])

        # URL Tab
        with tab1:
            st.subheader("URLs")

            # Fetching URL Data from DB
            df = get_url_data()
            total_urls = len(df)

            st.caption(f"All the URLs monitored in ICINGA : {total_urls}")
            on = st.toggle("Edit URLs")

            # Edit Mode
            if on:
                with st.form("url_form"):
                    deleted_rows = []
                    edited_data_list = []

                    # Displaying the data editor
                    st.data_editor(
                        df,
                        num_rows="dynamic",
                        hide_index=True,
                        key="url",
                        column_config={
                            "port": st.column_config.NumberColumn(),
                            "ssl": st.column_config.CheckboxColumn(required=True, default=True),
                            "on_redirect": st.column_config.SelectboxColumn(options=["follow", "ok"], default="follow",
                                                                            required=True)},
                        column_order=("id", "hostname", "vhost", "url", "port", "ssl", "on_redirect", "certificate_age",
                                      "assignment_group"),
                        disabled=("id",),
                    )

                    # When form is submitted
                    if st.form_submit_button('Save Changes'):
                        _ = st.session_state.url
                        # Altered Data fetched from session state
                        edited_rows = st.session_state["url"]["edited_rows"]
                        added_rows = st.session_state["url"]["added_rows"]
                        deleted_indexes = st.session_state["url"]["deleted_rows"]

                        # This loop gets the original ID for each edited row and create a list
                        for row_num in edited_rows.keys():
                            row_orig_id = df.iloc[row_num]["id"]
                            edited_rows[row_num]["id"] = row_orig_id
                            edited_data_list.append(edited_rows[row_num])

                        # This loop gets the entire row that needs to be deleted
                        for row_num in deleted_indexes:
                            row_dict = df.iloc[row_num].to_dict()
                            deleted_rows.append({"id": row_dict["id"]})

                        process_url_rows(edited_data_list, deleted_rows, added_rows)
            # View Mode
            else:
                st.dataframe(df)

        # MSZ Servers Tab
        with tab2:
            st.subheader("MSZ Servers")

            # fetching ilo data from DB
            msz_df = get_msz_data()
            total_msz = len(msz_df)

            st.caption(f"All the ILOs monitored in ICINGA : {total_msz}")
            on = st.toggle("Edit MSZ Servers")

            if on:
                with st.form("msz_form"):
                    deleted_rows = []
                    edited_data_list = []
                    st.data_editor(
                        msz_df,
                        num_rows="dynamic",
                        hide_index=True,
                        key="msz",
                        column_order=("id", "fqdn", "name", "ip", "os_family", "dc_zone"),
                        disabled=("id",)
                    )

                    if st.form_submit_button("Save Changes"):
                        st.session_state.msz

                        edited_rows = st.session_state["msz"]["edited_rows"]
                        deleted_indexes = st.session_state["msz"]["deleted_rows"]
                        added_rows = st.session_state["msz"]["added_rows"]

                        print(edited_rows)
                        # This loop gets the original ID for each edited row and create a list
                        for row_num in edited_rows.keys():
                            row_orig_id = msz_df.iloc[row_num]["id"]
                            edited_rows[row_num]["id"] = row_orig_id
                            edited_data_list.append(edited_rows[row_num])

                        # This loop gets the entire row that needs to be deleted
                        for row_num in deleted_indexes:
                            row_dict = msz_df.iloc[row_num].to_dict()
                            deleted_rows.append({"id": row_dict["id"]})

                        process_msz_rows(edited_data_list, deleted_rows, added_rows)

            else:
                with st.expander("Upload MSZ data from CSV"):
                    msz_csv = '''fqdn,name,os_family,dc_zone,ip'''
                    st.download_button(
                        data=msz_csv,
                        label="Download format",
                        file_name="msz_csv_upload_format.csv",
                        mime="text/csv",
                    )
                    uploaded_msz_csv = st.file_uploader("Choose a CSV File", type=['csv'])
                    if uploaded_msz_csv is not None:
                        msz_csv_df = pd.read_csv(uploaded_msz_csv, sep="[,;]", engine="python")
                        st.data_editor(msz_csv_df, key="ilo-csv")
                        if st.button("Upload"):
                            save_msz_csv(msz_csv_df)

                st.dataframe(msz_df)

        # Hardware ILOs Tab
        with tab3:
            st.subheader("Hardware ILOs")

            # fetching ilo data from DB
            ilo_df = get_ilo_data()
            total_ilos = len(ilo_df)

            st.caption(f"All the ILOs monitored in ICINGA : {total_ilos}")
            on = st.toggle("Edit ILOs")

            if on:
                with st.form("ilo_form"):
                    deleted_rows = []
                    edited_data_list = []
                    st.data_editor(
                        ilo_df,
                        num_rows="dynamic",
                        hide_index=True,
                        key="ilo",
                        column_config={
                            "region": st.column_config.SelectboxColumn(options=["NASA", "EMEA", "APAC"], default="NASA",
                                                                       required=True)},
                        column_order=("id", "fqdn", "ip", "region", "version"),
                        disabled=("id",)
                    )

                    if st.form_submit_button("Save Changes"):
                        _ = st.session_state.ilo

                        edited_rows = st.session_state["ilo"]["edited_rows"]
                        deleted_indexes = st.session_state["ilo"]["deleted_rows"]
                        added_rows = st.session_state["ilo"]["added_rows"]

                        print(edited_rows)
                        # This loop gets the original ID for each edited row and create a list
                        for row_num in edited_rows.keys():
                            row_orig_id = ilo_df.iloc[row_num]["id"]
                            edited_rows[row_num]["id"] = row_orig_id
                            edited_data_list.append(edited_rows[row_num])

                        # This loop gets the entire row that needs to be deleted
                        for row_num in deleted_indexes:
                            row_dict = ilo_df.iloc[row_num].to_dict()
                            deleted_rows.append({"id": row_dict["id"]})

                        process_ilo_rows(edited_data_list, deleted_rows, added_rows)

            else:
                with st.expander("Upload ILO data from CSV"):
                    ilo_csv = '''fqdn,ip,region,version'''
                    st.download_button(
                        data=ilo_csv,
                        label="Download format",
                        file_name="ilo_csv_upload_format.csv",
                        mime="text/csv",
                    )
                    uploaded_ilo_csv = st.file_uploader("Choose a File", type=['csv'])
                    if uploaded_ilo_csv is not None:
                        ilo_csv_df = pd.read_csv(uploaded_ilo_csv, sep="[,;]", engine="python")
                        st.data_editor(ilo_csv_df, key="ilo-csv")
                        if st.button("Upload"):
                            save_ilo_csv(ilo_csv_df)

                st.dataframe(ilo_df)
                # Logout button
                if st.session_state["authentication_status"]:
                    auth.logout("Logout", "sidebar")
                    # st.rerun()
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
