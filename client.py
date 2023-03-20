# import the library module
import sys
import hashlib
import requests

payload = {"email": "test@example.com"}
hash = "afd6b72cece9506a1c20bec92c2fa1c9"
url = "http://localhost:8080/login"

if sys.version_info < (3, 6):
    import sha3

headers = {"Content-Type": "application/json"}

loginResponse = requests.post(url, headers=headers, json=payload, verify=False).json()

print("Login response: ", loginResponse)

challengeResponse = loginResponse
state = "CONTINUE"
while state == "CONTINUE":
    link = challengeResponse['challenge']['link']
    indicesToHash = challengeResponse['challenge']['indicesToHash']
    dataFromHash = ""
    for index in indicesToHash:
        dataFromHash += hash[index]
    challenge_answer = hashlib.sha3_256(dataFromHash.encode("UTF-8")).hexdigest()
    payload = {"email": challengeResponse['email'], "challengeAnswer": challenge_answer, "token": challengeResponse['challenge']['body']['token']}
    challengeResponse = requests.post(link, headers=headers, json=payload, verify=False).json()
    print("challengeResponse: ", challengeResponse)
    state = challengeResponse['challengeState']
