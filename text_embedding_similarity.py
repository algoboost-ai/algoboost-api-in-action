import requests

collection_name = "******"  # Replace with your collection name
partition = "******"  # Replace with your chosen partition :: OPTIONAL
text = "******"     # Replace with input text your want to search
model = "{MODEL}"  # Replace {MODEL} with your model name
endpoint = "{ENDPOINT}"  # Replace {ENDPOINT} with your endpoint
api_key = "{API_KEY}"  # Replace {API_KEY} with your API key


def embedding_vector_similarity(collection_name, partition, text, model,
                                endpoint, api_key):
    payload = {
        "collection_name": collection_name,
        "partition": partition,
        "text": text,
    }

    # Make the POST request
    response = requests.post(
        f"https://app.algoboost.ai/api/model/similarity/{model}/{endpoint}",
        headers={"Authorization": f"Bearer {api_key}"},
        data=payload
    )

    # Parse the JSON response
    result = response.json()
    return result


result = embedding_vector_similarity(collection_name, partition, text, model,
                                     endpoint, api_key)
print(result)
