from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from extract import conj_show, noun_show
import settings

def main():
    updater = Updater(settings,TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("conj", find_verb_form))
    dp.add_handler(CommandHandler("noun", find_noun))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Привет! Этот телеграм канал предназначен для людей, изучающих Нидерландский язык.\
     Есть ты хочешь узнать артикль им.существиетльного, введи команду \ "noun" и искомое слово.\
     Если ты хочешь узнать спряжение глагола, то введи команду и глагол в зависимости от времени спряжения:\
     \ "pr" - настоящее время, \ "pa" - прошедшее время, \ "prp" - перфект, \ "pap" - паст перфект, \ "f" - будущее, \
     \ "cm" - условное наклонение, \ "sm"  - сосглагательное наклонение, \ "cp" - условный перфект.'
    print(text)
    update.message.reply_text(text)

def find_verb_form(bot, update):
    user_text = update.message.text.split(' ')
    tense_dict={'pr':'0', 'prp':'1', 'pa':'2', 'f':'3', 'cm':'4', 'sm':'5', 'pap':'6', 'cp':'7'}
    if len(user_text)==3:
        update.message.reply_text("\n".join(conj_show(user_text[2], tense_dict.get(user_text[1]))))
    else: 
        update.message.reply_text('?')

def find_noun(bot, update):
    user_text = update.message.text.split(' ')
    if len(user_text) == 2:
        update.message.reply_text(noun_show(user_text[1]))
    else:
        update.message.reply_text('?')

main() 
