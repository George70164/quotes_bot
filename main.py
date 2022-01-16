import telebot
from telebot import types
from api import quote
from database import *
import psycopg2

TOKEN = '5030499076:AAHBxY5m2nzuxUksYQxAsoLBpegLw1FUiZU'


db_connection = psycopg2.connect(DB_URI, sslmode="require")
db_object = db_connection.cursor()


bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Статистика')
    item2 = types.KeyboardButton('Цитата')
    item3 = types.KeyboardButton('Выбрать')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.text == 'Статистика':
        bot.send_message(message.chat.id, 'ХЗ, {0.first_name}'.format(message.from_user))
    #elif message.text == 'цитата':
    #markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    #item1 = types.KeyboardButton('+')
    #item2 = types.KeyboardButton('-')
    #markup.add(item1, item2)
    #bot.send_message(message.chat.id, quote['quoteText'], reply_markup=markup)


    elif (message.text == "Цитата"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Цитата понравилась")
        btn2 = types.KeyboardButton("Цитата не понравилась")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, quote(), reply_markup=markup)

    elif (message.text == "Цитата понравилась"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("У цитаты хорошее настроеные")
        btn2 = types.KeyboardButton("У цитаты грустное настроение")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Отлично", reply_markup=markup)
    elif (message.text == "У цитаты хорошее настроеные" or message.text == "У цитаты грустное настроение"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Статистика')
        item2 = types.KeyboardButton('Цитата')
        item3 = types.KeyboardButton('Выбрать')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)

    elif (message.text == "Цитата не понравилась"):
        bot.send_message(message.chat.id, quote())

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Статистика')
        item2 = types.KeyboardButton('Цитата')
        item3 = types.KeyboardButton('Выбрать')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)




    elif (message.text == "Выбрать"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Грустное настроение')
        item2 = types.KeyboardButton('Хорошое настроение')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, text="какое у вас настроение?", reply_markup=markup)

    elif (message.text == "Грустное настроение"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Статистика')
        item2 = types.KeyboardButton('Цитата')
        item3 = types.KeyboardButton('Выбрать')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, text="Появляется цитата с грустным настроением из базы данных и возвращяет в главное меню", reply_markup=markup)
    elif (message.text == "Хорошое настроение"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Статистика')
        item2 = types.KeyboardButton('Цитата')
        item3 = types.KeyboardButton('Выбрать')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, text="Появляется цитата с хорошим настроением из базы данных и возвращяет в главное меню", reply_markup=markup)





bot.polling(none_stop = True)