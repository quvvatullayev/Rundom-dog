import requests, json

TOKIN = '5567524975:AAHH4ioN3ZGUXbzPPPrXNk2tdWJU3O_fFyk' #user TOKIN

def teligramButton(id:int):

    """teligram uchun tasodifiy it suratini tanlash tugmasi uchun funksiya"""

    buttonText1 = {'text':'start rundom 🐶'}
    keyboard = {
        'KeyboardButton':[
            [buttonText1]
        ]
    }

    data = {
        'chat_id':id,
        'text':'Click to see a random dog picture',
        'reply_markup':keyboard
    }

    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    r = requests.post(url, json=data)

def getUpdates():
    """a function that retrieves information about users"""

    url = f"https://api.telegram.org/bot{TOKIN}/getUpdates"
    data = requests.post(url)
    return data.json()

def getData(data:json) ->str and int:
    """function that returns id, text and update_id of users"""

    data = data['result'][-1]
    update_id = data['update_id']
    id = data['message']['from']['id']
    text = data['message']['text']
    return update_id, id, text

def sendPhoto(id:int, dog:str):
    """function that sends photos to users"""

    url = f'https://api.telegram.org/bot{TOKIN}/sendPhoto'
    r = requests.get(url, params={'chat_id':id, 'photo':dog})
    r.json()

def rundomDogPhoto(id:int,text:str):
    """a function that randomly selects and returns a picture of dogs"""

    if text == 'start rundom 🐶':
        url = "https://random.dog/woof.json"
        dog = requests.get(url)
        dogJson = dog.json()
        dog = dogJson['url']
        sendPhoto(id, dog)

x = ''
while True:
    """cycle using bot"""
    data = getData(getUpdates())
    update_id, id, text = data
    print(text)
    if x != update_id:
        rundomDogPhoto(id,text)
        teligramButton(id)
        x = update_id