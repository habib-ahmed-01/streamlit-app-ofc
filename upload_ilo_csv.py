from sqlalchemy import create_engine

# Connection details
dialect = "postgresql"
host = "localhost"
port = "5432"
database = "m_db"
username = "ic_m_user"
password = "password123#"

# Creating the engine string
engine_string = f"{dialect}://{username}:{password}@{host}:{port}/{database}"
# Create a SQL engine
engine = create_engine(engine_string)


def save_ilo_csv(df):
    # Save the DataFrame to the database
    df.to_sql('ic_ilos', engine, index=False, if_exists='append')


def save_msz_csv(df):
    # Save the DataFrame to the database
    df.to_sql('ic_msz', engine, index=False, if_exists='append')
