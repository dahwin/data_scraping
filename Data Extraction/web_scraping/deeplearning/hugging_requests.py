import requests
import json

# Define the API endpoint for the model hub
model_hub_api_url = "https://huggingface.co/api/models"

# Make a GET request to the API
response = requests.get(model_hub_api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    models = response.json()

    # Save the content as a JSON file
    with open("models.json", "w", encoding="utf-8") as json_file:
        json.dump(models, json_file, ensure_ascii=False, indent=2)

    print("JSON file saved successfully.")
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")
    print(response.text)
