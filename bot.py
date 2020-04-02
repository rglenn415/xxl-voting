import requests
headers = {'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"}
data = {"action": "media_poll_vote", "poll_id": "10523173", "post_id": 884664, "answer_id": "48703415"}
res = requests.post('https://www.xxlmag.com/rest/carbon/api/poll/votenow', data = data, headers=headers)
print(res.json())
