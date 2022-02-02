import requests, sys
def execute(token, channelid, userid):
    data = {
        "content": f"\<@{userid}>"
    }
    headers = {
        "Authorization": token
    }
    res = requests.post("https://discord.com/api/channels/" + channelid + "/messages", data=data, headers=headers)
    print(res.text)

if __name__ == "__main__":
    if(len(sys.argv) < 4):
        print(f"python {__file__} <token> <channelid> <userid>")
        exit()
    execute(sys.argv[1], sys.argv[2], sys.argv[3])
