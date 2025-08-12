import requests

data_api_url = "http://localhost:8000/stocks" #FastAPI server in Docker Container running at port 8000

def get_data():
    """Retrieves stock data from a FastAPI server and returns it as a dictionary.
        Returns:
            dict: Stock data retrieved from the API."""
    response = requests.get(data_api_url)

    if response.status_code == 200:
        data = response.json()
        #print(data)
        return data
    else:
        print(f"Error: {response.status_code}")

#get_data()