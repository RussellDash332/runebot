from env import TOKEN, DELIMITER

##import threading
##import requests
from os import path
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

def start(update, context):
    welcome_txt = [
        "*Welcome to the Rune Compiler!*",
        "",
        "Compile your rune here! Here's a sample execution:",
        "/show heart\_bb",
        "/anaglyph heart\_bb",
        "/hollusion heart\_bb",
        "/stereogram heart\_bb",
        "",
        "Supported functions:",
        "`mosaic(a, b, c, d)`",
        "`simple_fractal(rune)`",
        "`egyptian(rune, n)`",
        "`fractal(rune, n)`",
        "`dual_fractal(pic1, pic2, n)`",
        "`steps(a, b, c, d)`",
        "`tree(n, rune)`",
        "`helix(rune, n)`",
        "`cs1010s(rune)`",
        "",
        "*Note:* Please use `math.sqrt` instead of `sqrt`!",
        ]

    update.message.reply_text('\n'.join(welcome_txt),parse_mode="markdown")

def show_rune(update, context):
    #print(update.message.chat)
    if context.args:
        with open("data/waiting_list_show.txt", "a") as f:
            f.write(f"{update.message.chat['id']}{DELIMITER}{update.message.message_id}{DELIMITER}{' '.join(context.args)}\n")
            f.close()
        #save_image("show")
        update.message.reply_text('Please wait, your image will be processed soon.')
    else:
        update.message.reply_text('Sorry, please give me something to show.')
##    update.message.reply_photo(open('show.png', 'rb'))

def anaglyph_rune(update, context):
    if context.args:
        with open("data/waiting_list_anaglyph.txt", "a") as f:
            f.write(f"{update.message.chat['id']}{DELIMITER}{update.message.message_id}{DELIMITER}{' '.join(context.args)}\n")
            f.close()
        update.message.reply_text('Please wait, your image will be processed soon.')
    else:
        update.message.reply_text('Sorry, please give me something to show.')

def hollusion_rune(update, context):
    if context.args:
        with open("data/waiting_list_hollusion.txt", "a") as f:
            f.write(f"{update.message.chat['id']}{DELIMITER}{update.message.message_id}{DELIMITER}{' '.join(context.args)}\n")
            f.close()
        update.message.reply_text('Please wait, your image will be processed soon.')
    else:
        update.message.reply_text('Sorry, please give me something to show.')

def stereogram_rune(update, context):
    if context.args:
        with open("data/waiting_list_stereogram.txt", "a") as f:
            f.write(f"{update.message.chat['id']}{DELIMITER}{update.message.message_id}{DELIMITER}{' '.join(context.args)}\n")
            f.close()
        update.message.reply_text('Please wait, your image will be processed soon.')
    else:
        update.message.reply_text('Sorry, please give me something to show.')

def do():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("show", show_rune))
    dp.add_handler(CommandHandler("anaglyph", anaglyph_rune))
    dp.add_handler(CommandHandler("hollusion", hollusion_rune))
    dp.add_handler(CommandHandler("stereogram", stereogram_rune))

    updater.start_polling()
    print("++++++++++ STARTING BOT +++++++++++")
    updater.idle()
    print("++++++++++  KILLING BOT  ++++++++++")

if __name__ == "__main__":
    print("Press CTRL + C to kill the bot")
    do()
