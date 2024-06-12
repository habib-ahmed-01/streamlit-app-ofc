import requests
from io import StringIO
import pandas as pd


def get_sample_data():
    # Example URL for a JSON API (replace with your actual URL)
    url = "https://api.sampleapis.com/futurama/characters"

    # Fetch the JSON data from the API
    response = requests.get(url)
    json_data = response.text  # Get the JSON data as a string

    # Use StringIO to wrap the JSON string
    json_data_io = StringIO(json_data)

    # Read the JSON data into a pandas DataFrame
    df = pd.read_json(json_data_io)

    # Print the DataFrame
    return df
