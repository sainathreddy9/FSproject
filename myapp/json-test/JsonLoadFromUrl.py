import json
from urllib.request import urlopen

'''with urlopen("https://in.finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:'''
with urlopen("https://www.google.com/") as response:
    source = response.read()

'''data = json.loads(source)'''
print(source)
'''print(json.dumps(data, indent=2))'''