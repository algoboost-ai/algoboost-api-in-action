import requests

api_key = "{API_KEY}"  # Replace {API_KEY} with your API key


def retrieve_vector_by_id():
    # Define the URL for the API endpoint
    url = "https://app.algoboost.ai/api/model/retrieve_vectors_by_id"

    # Define the payload with the vector ID to retrieve
    payload = {"vectors": []}  # vector id list

    # Define the headers including authorization and content type
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        # Make a POST request to the API endpoint with payload and headers
        response = requests.post(url, json=payload, headers=headers)

        # Check if the response status code indicates success (e.g., 200)
        if response.status_code == 200:
            # Parse the JSON content of the response
            data = response.json()
            # Print the parsed JSON data
            print(data)
        else:
            # Print an error message for non-200 status codes
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        # Handle any exceptions or errors that may occur during the request
        print(str(e))


# Call the function to retrieve the vector by ID
retrieve_vector_by_id()
