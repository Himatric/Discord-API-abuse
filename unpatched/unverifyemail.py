import requests
import sys
token = sys.argv[1]

if not token or token == "":
    raise TypeError(f'python {__file__} <token>')

res = requests.get("https://discord.com/api/guilds/0/members", headers={
    'Authorization': token
})

print(res.text) # "No access"
