 from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
       

def main():
    updater = Updater("591697560:AAFHrSB8MwFmwEB41OHXlhupmFPVv_aeyz0")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    updater.start_polling()
    updater.idle()
main()

