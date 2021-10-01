import requests as r 
import json 


output='/tmp/foo.json'
with open(output, 'w') as f :
    f.write(r.get("http://worldclockapi.com/api/json/cet/now").text)