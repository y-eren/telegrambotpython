import telebot
import requests
import time

bot_token = ''

bot = telebot.TeleBot(bot_token)

altin_api_link = 'https://api.genelpara.com/embed/altin.json'

dollar_api_link = 'https://api.genelpara.com/embed/doviz.json'

    

def get_altin():
    response = requests.get(altin_api_link)
    veri = response.json()
    altin_fiyati = veri['satis']
    altin_mesaji = 'Güncel altın fiyatı : {}'.format(altin_fiyati)
    return altin_mesaji
    
    
def get_dolar():
    response = requests.get(dollar_api_link)
    veri = response.json()
    dolar_fiyati = veri['satis']
    dolar_mesaji = 'Güncel dolar fiyati : {}'.format(dolar_fiyati)
    return dolar_mesaji



@bot.message_handler(commands=['start'])
def hosgeldinmesaji(mesaj):
   bot.reply_to(mesaj, 'Hoşgeldiniz, güncel kurlar için doğru adres burasıdır.Aşağıdaki komutlar kullanılılabilir:\n /dolar - Güncel dolar fiyaıtını 4 saatte bir alırsınız. \n /altın - Güncel altın fiyatını 4 saatte bir gösterir. \n /hepsi - Mevcut tüm kurlardan bilgi alırsınız. ')
   dolar_mesaji = get_dolar()
   altin_mesaji = get_altin()
   bot.send_message(chat_id = mesaj.chat.id, text = '{}\n{}'.format(altin_mesaji, dolar_mesaji))
     
@bot.message_handler(commands=['altın'])
def sadece_altin(mesaj):
    while True:
     altin_mesaji = get_altin()
     bot.send_message(chat_id=mesaj.chat.id, text=altin_mesaji)
     time.sleep(3600)

@bot.message_handler(commands=['dolar'])
def sadece_dolar(mesaj):
    while True :
     dolar_mesaji = get_dolar()
     bot.send_message(chat_id=mesaj.chat.id, text=dolar_mesaji)
     time.sleep(3600)

@bot.message_handler(commands=['hepsi'])
def hepsi_fiyatlari(mesaj):
    while True:
     dolar_mesaji = get_dolar()
     altin_mesaji = get_altin()
     bot.send_message(chat_id = mesaj.chat.id, text = '{}\n{}'.format(altin_mesaji, dolar_mesaji))
     time.sleep(3600)

bot.polling()
