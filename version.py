import requests

url = "https://raw.githubusercontent.com/kangxi11/CMPUT404-lab1/main/version.py"
# print(requests.__version__)
# print(requests.get("https://www.google.com/"))

r = requests.get(url)

print(r.text)