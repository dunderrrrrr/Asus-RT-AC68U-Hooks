import requests
import base64

asus_ip = "10.1.1.1" # IP of router/gateway
appPayload = "nvram_get(time_zone)" # Your payload
auth = {
    "user": "admin", # admin username
    "passwd": "password" # admin passwd
}

def genBase64(data): 
    string = "{}:{}".format(data['user'], data['passwd'])
    string_bytes = string.encode('ascii')
    base64_bytes = base64.b64encode(string_bytes)
    output = base64_bytes.decode('ascii')
    return(output)    

def getToken(login):
    payload = "login_authorization={}".format(login)
    headers = {
        'user-agent': "asusrouter-Android-DUTUtil-1.0.0.201"
    }
    r = requests.post(url = 'http://{}/login.cgi'.format(asus_ip), data=payload, headers=headers)
    return(r.json()['asus_token'])

def appGet(token, appPayload):
    payload = "hook={}".format(appPayload)
    headers = {
        'user-agent': "asusrouter-Android-DUTUtil-1.0.0.201",
        'cookie': 'asus_token={}'.format(token)
    }
    r = requests.post(url = 'http://{}/appGet.cgi'.format(asus_ip), data=payload, headers=headers)   
    print("Status code: ", r.status_code)
    print(r.text) 

if __name__ == "__main__":

    login = genBase64(auth)
    token = getToken(login)

    appGet(token, appPayload)