import requests


url = "http://127.0.0.1:8000/get_form/"
data = {'field_phone': '+7 925 008 14 25', 'field_email': 'qwe@rty.tu', 'field_text': 'dsfasdg fd gfds gfdsg fdg',
        'field_date': '20.02.2002'}
response = requests.post(url, data=data)
print(response.text)
