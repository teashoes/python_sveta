from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from extract_conj import conj_show
import settings

def main():
    updater = Updater(settings,TELEGRAM_API_KEY)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("conj", find_verb_form))
    updater.start_polling()
    updater.idle()

def greet_user(bot, update):
    text = 'Hoi! Het is een Telegram-bot voor mensen wie studieren Nederlands.\
     Als je wil een verba konjugeren, schriv je "/conj verba praeteritum nummer.\
     "'
    print(text)
    update.message.reply_text(text)

def find_verb_form(bot, update):
    user_text = update.message.text.split(' ')
    if len(user_text)==3:
        update.message.reply_text("\n".join(conj_show(user_text[1], user_text[2])))
    else: 
        update.message.reply_text('?')

# main()
