from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from extract import conj_show, noun_show
import settings

def main():
    updater = Updater(settings,TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("conj", find_verb_form))
    dp.add_handler(CommandHandler("n", find_noun))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Привет! Этот телеграм канал предназначен для людей, изучающих Недерландский язык.\
     Есть ты хочешь узнать артикль им.существиетльного, введи команду "\noun" и искомое слово.\
     Если ты хочешь узнать спряжение глагола, то введи команду и глагол в зависимости от времени спряжения:\
     "\pr" - настоящее время, "\pa" - прошедшее время, "\pp" - перфект, "\pap" - паст перфект\"'
    print(text)
    update.message.reply_text(text)

def find_verb_form(bot, update):
    user_text = update.message.text.split(' ')
    if len(user_text)==3:
        update.message.reply_text("\n".join(conj_show(user_text[1], user_text[2])))
    else: 
        update.message.reply_text('?')

def find_noun(bot, update):
    user_text = update.message.text.split(' ')
    if len(user_text) == 2:
        update.message.reply_text("\n".join(noun_show(user_text[1])))
    else:
        update.message.reply_text('?')
# main()
