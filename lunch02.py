import requests
import json
import input_data

# dictに変換
jdata = json.loads(input_data.past_lunches)

inputdate = input()
print('date=' + inputdate)

inputcost = input()
print('cost=' + inputcost)

new_lunches = {"date": inputdate,"cost": inputcost}

url = 'ec2-52-14-90-229.us-east-2.compute.amazonaws.com/lunches'
headers = {'content-type': 'application/json'}
response = requests.post(url, json.dumps(new_lunches), headers=headers)