#pip install requests && argparse
import requests
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="Name of the file to save the Python script")
args = parser.parse_args()

api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY") #Create your own\
    #api-key and replace this value ^^^^ set your ket with->> export OPENAI_API_KEY=(enter your api key)

requests_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + api_key
}

requests_data ={
    "model": "text-davinci-003", #you can change model to codex if you want
    "prompt": f"Write python script {args.prompt}. Provide only code, no text",
    "max_tokens": 500,#max number of words or punctuation marks that the api should generate in its response
    "temperature": 0.5 #this is set to 0 or 1 for creativity of the api engine half predictable half creativity response
}

response = requests.post(api_endpoint, headers=requests_headers, json=requests_data)

if response.status_code == 200:
    response_text = (response.json()["choices"][0]["text"])
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Request failed with status code: {str(response.status_code)}")#this is a int but str returns a string message

#py python-chatgpt.py "give an arugument Ex. -> Print We connecting to OpenAI" "make up a name to save response to a file ex. test.py"
#py python-chatgpt.py "go through files in Downloads folder, check their dates and if they are older than 30 days, move them to folder called to_delete" \
#"clean_downloads.py"
