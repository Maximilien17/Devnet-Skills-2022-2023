import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Rome, Italy"
dest = "Frascati, Italy"
key = "ABjjIl3AafTdrG4Gr5FcbGkltREjA4WS"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to": dest})

print("URL:" + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API status: " + str(json_status) + " = A successful route call.\n")