import requests

callID = 0  # api call_id
apiKey = "your_api_key"  # algoboost api Key


def get_results(callID, apiKey):
    host = "https://app.algoboost.ai"
    url = f"{host}/api/model/get_results/{callID}"
    headers = {
        "Authorization": f"Bearer {apiKey}"
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


results = get_results(callID, apiKey)
if results is not None:
    # Now you can work with the 'results' variable
    print(results)
