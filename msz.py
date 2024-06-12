import streamlit as st
from db_connections import icinga_pg_conn
from postgres_msz_pool import save_to_db


def get_msz_data():
    conn = icinga_pg_conn()
    df = conn.query("select * from ic_msz")
    return df


def edit_function(data):
    # Your edit logic here
    save_to_db('edit', data)
    print(f"Editing data: {data}")


def delete_function(data):
    # Your delete logic here
    save_to_db('delete', data)
    print(f"Deleting data: {data}")


def add_function(data):
    # Your add logic here
    save_to_db('insert', data)
    print(f"Adding data: {data}")


def process_msz_rows(edited_row, deleted_row, added_row):
    if edited_row:
        edit_function(edited_row)

    if deleted_row:
        delete_function(deleted_row)

    if added_row:
        add_function(added_row)
