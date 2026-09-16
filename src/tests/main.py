import requests
import json

url = "https://codeforces.com/api/problemset.problems?tags=implementation"

res = requests.get(url).json()

print(res)



