import requests

# Replace 'YOUR_ALGOBOOST_API_KEY' with your actual AlgoBoost API key
ALGOBOOST_API_KEY = 'YOUR_ALGOBOOST_API_KEY'
model = 'your_model_name'
endpoint = 'your_endpoint'
collection_name = 'your_collection_name'
partition = 'your_partition'
image_path = 'path_to_your_image'  # path to your image file


def image_inference(model, endpoint, collection_name, partition, image_path):
    """
    Perform image inference using AlgoBoost API.

    Args:
        model (str): The name of the model.
        endpoint (str): The API endpoint for inference.
        collection_name (str): The name of the collection.
        partition (str): The partition for collection.
        image_path (str): Path to the image file for inference.

    Returns:
        dict: Dictionary containing the inference results.
    """
    # Check if required parameters are provided
    if not all([model, endpoint, collection_name, partition, image_path]):
        print("Error: Missing required parameters.")
        return None

    # Open the image file
    with open(image_path, 'rb') as file:
        # Prepare the files for the request
        files = {'image': (file.name, file)}

        # Set the request headers with the API key
        headers = {"Authorization": f"Bearer {ALGOBOOST_API_KEY}"}
        url = f"https://app.algoboost.ai/api/model/inference/{model}/{endpoint}"

        try:
            # Make a POST request to the API with form data and files
            response = requests.post(
                url,
                headers=headers,
                files=files,
                data={'collection_name': collection_name,
                      'partition': partition}
            )

            # Check the HTTP status code
            if response.status_code == 200:
                # Parse the JSON response
                results = response.json()
                return results
            else:
                print(
                    f"API request failed with status code: {response.status_code}")
                return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


# Call the function and capture the results
inference_results = image_inference(model,
                                    endpoint,
                                    collection_name, partition, image_path)
if inference_results:
    print(inference_results)
