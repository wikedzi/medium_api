import http.client
import json

def fetchData():
	#API variables
	host 	="api.medium.com"
	auth 	="Bearer 25701d75b893f2e267ea7b8b3af98aa9dd39b190ac738aab0818d7443b2050ebe"
	cType 	="application/json"
	accept 	="application/json"
	userId	="1573b2156fb06a3ed9c6d9eed8f7e24042733be2bfa833bf1af1b30f46ba8a9a7"

	httpHeaders = {"Content-type":cType,"Accept": accept,"Accept-Charset": "utf-8", "Authorization":auth}
	URI = "/v1/users/"+userId+"/publications"

	#Connecting to Medium with an API using GET method
	conn = http.client.HTTPSConnection(host)
	conn.request("GET",URI,"",httpHeaders)

	#Fetching Response object
	response = conn.getresponse()
	print(response.status, response.reason)
	data = response.read()
	#closing The connection to relase resources
	conn.close()

	return json.loads(data)# returns a json object of all publications that I own or follows

publications = fetchData()
for publication in publications['data']:
	#print(publication)
    print('ID: {0[id]:s};Name: {0[name]:s};url: {0[url]:s}'.format(publication))
    print("----------------------------------------------------------------------")
    print(publication['description'])
    print("************************************************************************************")
    print()

