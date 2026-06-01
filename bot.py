import telebot
import os
import numpy as np
from datetime import datetime
from imageai.Detection import ObjectDetection
import requests
import random
from bot_logic import gen_pass
from bot_money import number

TOKEN = "TOKEN"

bot = telebot.TeleBot(TOKEN)

detector = ObjectDetection()
model_path = "yolov3.pt"
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
print(f"Загрузили модель: {model_path}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Чтобы узнать, что я умею, напиши /info")

@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "/hello, /feel, /bye, /password, /1or2, /weather, /geo, /listwindows, /dance, /system, /system2, /random_system, /duck, /dog, /pokemon, /fox, /clean, а ещё я умею повторять.")

@bot.message_handler(commands=['listwindows'])
def send_info(message):
    bot.reply_to(message, "Windows 1.0, Windows 2.0, Windows 3.0, Windows 89, Windows 93, Windows 95, Windows 98, Windows ME (or Millenium), Windows 2000, Windows XP, Windows Vista, Windows 7, Windows 8, Windows 9, Windows 10, Windows 11.")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет!")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['feel'])
def send_feel(message):
    bot.reply_to(message, "Как дела?")

@bot.message_handler(commands=['dance'])
def send_dance(message):
    image_url="https://masterpiecer-images.s3.yandex.net/85be56ac526311eebffbbadf81d486ab:upscaled"
    bot.send_photo(message.chat.id, photo=image_url)

@bot.message_handler(commands=['system2'])
def send_ranimg(message):
    with open('images/system2.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['system'])
def send_sun(message):
    bot.send_photo(message.chat.id, open("images/system.png", 'rb'))

@bot.message_handler(commands=['random_system'])
def send_sunny(message):
    photo = random.choice(['system.png','system2.jpg'])
    # file_path = 'images/' + photo
    file_path = f'images/{photo}'
    bot.send_photo(message.chat.id, open(file_path, 'rb'))

@bot.message_handler(commands=['clean'])
def send_cleany(message):
    bot.reply_to(message, 'Чтобы сохранить природу, нужно сокращать потребление пластика (который разлагается около 400 лет), воды, энергии, правильно утилизировать отходы (сортировать мусор, сдавать батарейки(которые приносят вред окружающей среде)), выбирать экологичный транспорт: велосипед, общественный или ходьба (угдекислый газ нам вреден), бережно относиться к живой природе, убирая за собой мусор на пикниках и не вредить животным🌼. Пожалуйста не мусорьте!')
    bot.reply_to(message, 'Из пластиковых бутылок можно делать кормушки для птиц.')
    bot.send_photo(message.chat.id, photo='https://lh5.googleusercontent.com/proxy/rQzFqsiJy4yEkS8dRR8NMBOzoa4CvirdJQwNRITqqJDfDB9wXRCyqDi3ffrhgrAcCyPm53mmuV2PCkwqydMpGJDOoha1NWFiS8mNtZbcPOikIIOgjyGWrEXjcji5CK6Cthr2occP')
    bot.reply_to(message, 'Cпасибо за понимание!')

@bot.message_handler(commands=['weather'])
def weather(message):
    city = 'Ростов - на Дону'
    url = f'http://wttr.in/{city}?format=3'
    response = requests.get(url)
    bot.send_message(message.chat.id, response.text)

def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.reply_to(message, image_url)

def get_dog_image_url():    
        url = 'https://random.dog/woof.json'
        res = requests.get(url)
        data = res.json()
        return data['url']

@bot.message_handler(commands=['dog'])
def dog(message):
    '''По команде dog вызывает функцию get_dog_image_url и отправляет URL изображения собаки'''
    image_url = get_dog_image_url()
    bot.reply_to(message, image_url)

def get_pokemon_image_url():
        pokemons = ['pikachu', 'ditto', 'slowpoke']
        random_pokemon = random.choice(pokemons)
        url = f'https://pokeapi.co/api/v2/pokemon/{random_pokemon}'
        res = requests.get(url)
        data = res.json()
        return data['sprites']['front_default']

@bot.message_handler(commands=['pokemon'])
def pokemon(message):
    '''По команде pokemon вызывает функцию get_pokemon_image_url и отправляет URL изображения собаки'''
    image_url = get_pokemon_image_url()
    bot.reply_to(message, image_url)

def get_fox_image_url():    
        url = 'https://randomfox.ca/floof/'
        res = requests.get(url)
        data = res.json()
        return data['image']

@bot.message_handler(commands=['fox'])
def fox(message):
    '''По команде dog вызывает функцию get_fox_image_url и отправляет URL изображения лисы'''
    image_url = get_fox_image_url()
    bot.reply_to(message, image_url)

@bot.message_handler(commands=['geo'])
def send_geo(message):
    bot.send_location(message.chat.id, 55.7558, 37.6173)
    bot.send_message(message.chat.id, "📍 Москва, Кремль")

@bot.message_handler(commands=['password'])
def password(message):
    qqq = gen_pass(10)
    bot.reply_to(message, gen_pass(10))

@bot.message_handler(commands=['1or2'])
def money(message):
    uuu = number()
    bot.reply_to(message, number())

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.send_message(message.chat.id, f"Получили фото")
    print(f"Получили фото")

    if not message.photo:
        return bot.send_message(message.chat.id, "Вы забыли загрузить картинку: (")
    
    file_info = bot.get_file(message.photo[-1].file_id)
    unique_id = lambda: np.random.randint(1000, 9999) #Генерация уникального ID для имени файла
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_extension = ".jpg"
    file_name = f"img_{timestamp}{unique_id()}{file_extension}"
    #Скачиваем фото
    downloaded_file = bot.download_file(file_info.file_path)

    #Сейвим фото на дисK
    save_path = os.path.join('images', file_name)

    os.makedirs("images", exist_ok=True)

    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    print(f"Сохранили фото: {save_path}")

    bot.send_message(message.chat.id, "Фото успешно сохранено. Начинаю распознавание...")

    detections = detector.detectObjectsFromImage(
        input_image=save_path,
        output_image_path="output_image.jpg",
        minimum_percentage_probability=30)
    
    print(f"Распознали фото")

    with open("output_image.jpg", 'rb') as f:  
        bot.send_photo(message.chat.id, f)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
        
bot.polling()
