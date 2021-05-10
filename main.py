import requests
def classify(text):
    key = "f6ef1c10-9dbc-11eb-8597-2599b8997dd946ffe70e-2f1d-4101-a501-f62ef6fd0ea4"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"
    response = requests.get(url, params={ "data" : text })
    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()
while(1):
    q = classify(str(input()))

    label = q["class_name"]
    confidence = q["confidence"]
    if(label=='a'):print('a')
    elif(label=='b'):print('b')
    elif(label=='c'):print('c')