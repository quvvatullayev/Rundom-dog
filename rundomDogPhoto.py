import requests, json

TOKIN = '5567524975:AAHH4ioN3ZGUXbzPPPrXNk2tdWJU3O_fFyk' #user TOKIN

def teligramButton(id:int):
    """teligram uchun tasodifiy it suratini tanlash tugmasi uchun funksiya"""

    buttonText1 = {'text':'start rundom 🐶'}
    buttonText2 = {'text':'start rundom 😺'}
    ReplyKeyboardMarkup = {
        'resize_keyboard':True,
        'keyboard':[
            [buttonText1, buttonText2]
        ]
    }

    data = {
        'chat_id':id,
        'text':'Click to see a random dog and cit picture',
        'reply_markup':ReplyKeyboardMarkup
    }

    url = f'https://api.telegram.org/bot{TOKIN}/sendMessage'
    r = requests.get(url, json=data)

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

    if text == 'start rundom 😺':
        url = "https://aws.random.cat/meow"
        cit = requests.get(url)
        dogJson = cit.json()
        cit = dogJson['file']
        sendPhoto(id, cit)

x = ''
while True:
    """cycle using bot"""
    data = getData(getUpdates())
    update_id, id, text = data
    if x != update_id:
        rundomDogPhoto(id,text)
        teligramButton(id)
        x = update_id