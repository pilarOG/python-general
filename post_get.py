import validators
import requests
import json

def postRequest(url, headers=None, data=None, params=None):
    # Validate input
    if validators.url(url) == False: raise ValueError('Url malformed')
    if type(data) != dict and data != None: raise TypeError('Data should be a dict')
    if type(headers) != dict and headers != None: raise TypeError('Headers should be a dict')
    if type(params) != dict and params != None: raise TypeError('Parameters should be a dict')

    # Make post
    response = requests.post(url, data=json.dumps(data), headers=headers, params=params)
    print(response.url)
    # Check status code
    if response.status_code == 200:
        return response.text
    else:
        raise Exception('Post status code was {}'.format(response.status_code))

# print postRequest('http://127.0.0.1:5000/echo',data={'input':'hola'}, headers={'content-type': 'application/json'})
# print postRequest('http://127.0.0.1:5000/repeat',params={'input':'hola'})
# print postRequest('http://127.0.0.1:5000/pprint/hola')
