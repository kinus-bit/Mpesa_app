import requests
import base64

#get url
url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

CONSUMER_KEY = "tffWyALA2mzWPgMZ7KwenoLqBIkxYtmncda99aACldfdxcYe"
CONSUMER_SECRET = "9Xha5QXgUmHqCmaz6r9IYheGZe85800kvN0RO926hHAc1auIGaEs6urFMXfGwtiu"

def getaccess_token():
    try:
        #this is the request body
        
        credentials= f'{CONSUMER_KEY}:{CONSUMER_SECRET}'
        encoded_credentials = base64.b64encode(credentials.encode()).decode()

        #headers
        #Authorization (basic auth)
        headers = {"Authorization": f'Basic {encoded_credentials}'}

        #paramas has grant_type which is  client_credentials
        response = requests.get(url=url,headers=headers)
        return response.json()
        # print(response)
    except Exception as e:
        return {'error':str(e)}
