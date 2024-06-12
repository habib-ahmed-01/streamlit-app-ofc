from db_connections import icinga_pg_conn
from postgres_url_pool import save_to_db


# Fetch url rows from db
def get_url_data():
    conn = icinga_pg_conn()
    df = conn.query("select * from ic_urls")
    return df


# Edits the urls based on the updates provided by the user
def edit_function(data):
    # Your edit logic here
    save_to_db('edit', data)
    print(f"Editing data: {data}")


# Deleted the entry from the url list
def delete_function(data):
    # Your delete logic here
    save_to_db('delete', data)
    print(f"Deleting data: {data}")


# Adds the url to the db
def add_function(data):
    # Your add logic here
    save_to_db('insert', data)
    print(f"Adding data: {data}")


# gets the data and sends accordingly to functions
def process_url_rows(edited_row, deleted_row, added_row):
    if edited_row:
        edit_function(edited_row)

    if deleted_row:
        delete_function(deleted_row)

    if added_row:
        add_function(added_row)
