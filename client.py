# import the library module
import sys
import hashlib
import webbrowser

import requests

payload = {"email": "best@example.com"}
hash = "243262243136246e4c66354f79775933646f6a626a6e6c68526d57702e4a595843456c7057475030496d6a3165504346526446504551526a726d5575"
#url = "http://localhost:8080"
url = "https://zkp-service-amitrangra.cloud.okteto.net"

if sys.version_info < (3, 6):
    import sha3

headers = {"Content-Type": "application/json"}

loginResponse = requests.post(url+"/login", headers=headers, json=payload).json()

print("Login response: ", loginResponse)

challengeResponse = loginResponse
state = "CONTINUE"
count = 1
while state == "CONTINUE":
    link = challengeResponse['challenge']['link']
    indicesToHash = challengeResponse['challenge']['indicesToHash']
    dataFromHash = ""
    for index in indicesToHash:
        dataFromHash += hash[index]
    challenge_answer = hashlib.sha3_256(dataFromHash.encode("UTF-8")).hexdigest()
    payload = {"email": challengeResponse['email'], "challengeAnswer": challenge_answer, "token": challengeResponse['challenge']['body']['token']}
    challengeResponse = requests.post(url+link, headers=headers, json=payload).json()
    print("challengeResponse ",count," :", challengeResponse)
    count = count + 1
    state = challengeResponse['challengeState']

if challengeResponse['challengeState'] == "SUCCESS":
    webbrowser.open_new(url+"/login?token="+challengeResponse['token'])