import requests

resp = requests.post(url = 'http://oa:5000/sendImg',data={
    'name':'制哥',
    'msg':'https://avatars1.githubusercontent.com/u/4088439?s=460'
})
print(resp.content)