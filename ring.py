from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
import telegram
from twilio.rest import Client


def Call(bot,update,args):
    phone = args[0]

    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC663b0f839179ecb7f9564716807bf4a3'
    auth_token = '846374aa0e4a6e7bfc2c6a491f5624e3'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            url='http://demo.twilio.com/docs/voice.xml',
                            to='+'+phone,
                            from_='+552139579317'
                        )
    update.message.reply_text()
    print(call.sid)

def ajuda(bot,update):
    update.message.reply_text('/ring [phone number with international code] to ring your phone')

def main():
    token = '974868761:AAHXpA6hANLinqREJ29J4q6LElciflb9Sb0'
    
    updater = Updater(token=token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram

    dispatcher.add_handler(
        CommandHandler('ring', Call,pass_args=True)
    )
    
    dispatcher.add_handler(
        CommandHandler('help', ajuda)
    )
    
    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    print('Press Ctrl+C to stop.')
    
    main()