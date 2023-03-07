import requests
import os


api_key = os.getenv("OPENAI_API_KEY") #Create your own\
    #api-key and replace this value ^^^^ set your ket with->> export OPENAI_API_KEY=(enter your api key)

def send_message_to_chatgpt(message):
    # Your ChatGPT API URL
    api_endpoint = "https://api.openai.com/v1/completions"

    # Your ChatGPT API key
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    }
    # Data to be sent to ChatGPT API
    data = {
        "model": "text-davinci-003", #you can change model to codex if you want
        "prompt": "This is a test ",
        "max_tokens": 500,#max number of words or punctuation marks that the api should generate in its response
        "temperature": 0.5 #this is set to 0 or 1 for creativity of the api engine half predictable half creativity response
    }
    print(data)
# Sending post request and saving response as response object
    response = requests.post(api_endpoint, headers=headers, json=data)
    print(response)
        # Extracting response text
    if response.status_code == 200:
        response_text = response.json()['choices'][0]['text']
        print(response_text)
    # returning response text
    #return response_text

    # Example incoming message
    incoming_message = input()

    # Sending message to ChatGPT API
    response_message = send_message_to_chatgpt(incoming_message)

    # Printing response message
    print(response_message)
