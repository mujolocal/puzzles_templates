"http://www.pythonchallenge.com/pc/def/linkedlist.php"
import requests
import re
pattern = re.compile("[0-9]+")
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
addon = "63579"

for i in range(400):
    req = requests.get(url+addon)
    match = pattern.findall(req.text)
    print(req.text)
    addon = match[0]
    