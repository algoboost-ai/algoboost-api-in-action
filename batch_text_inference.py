import requests

# Replace 'YOUR_ALGOBOOST_API_KEY' with your actual AlgoBoost API key
ALGOBOOST_API_KEY = ''
model = ''
endpoint = ''
collection_name = ''
partition = ''
sentences = []  # list of text


def batch_text_inference(model, endpoint, collection_name, partition, sentences):
    """
    Perform batch text inference using AlgoBoost API.

    Args:
        model (str): The name of the model.
        endpoint (str): The API endpoint for inference.
        collection_name (str): The name of the collection.
        partition (str): The partition for collection.
        sentences (list): List of text sentences to infer.

    Returns:
        dict: Dictionary containing the inference results.
    """
    # Check if required parameters are provided
    if not all([model, endpoint, collection_name, partition, sentences]):
        print("Error: Missing required parameters.")
        return None

    # Prepare the form data for the request
    form_data = {
        'collection_name': collection_name,
        'partition': partition,
        'sentences': sentences
    }

    # Set the request headers with the API key
    headers = {"Authorization": f"Bearer {ALGOBOOST_API_KEY}"}
    url = f"https://app.algoboost.ai/api/model/batch/inference/{model}/{endpoint}"

    try:
        # Make a POST request to the API with form data and files
        response = requests.post(
            url,
            headers=headers,
            data=form_data,
        )

        # Check the HTTP status code
        if response.status_code == 200:
            # Parse the JSON response
            results = response.json()
            return results
        else:
            print(f"API request failed with status code: {response.status_code}")
            return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Call the function
batch_text_inference(model, endpoint, collection_name, partition, sentences)
