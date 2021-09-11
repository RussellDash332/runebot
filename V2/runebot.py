from env import TOKEN, DELIMITER
from runes import *

from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

error_msg = "I smell a sense of power abuse. Fix the keywords :\")"

# For now it's a blacklist instead of whitelist
bans = ["exec", "eval", "import", "random", "with",
        "open", "close", "globals", "exit", "locals",
        "print", "quit", "super", "vars", "name", "main",
        "doc", "package", "loader", "class", "debug", "raise",
        "input", "dir", "try", "except", "staticmethod", "help", "code",
        "builtin", "attr"]
log_it = True

def overlap(arr, string):
    for i in arr:
        if i in string:
            return True
    return False

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
        "`number(n, rune=circle_bb)`",
        "",
        "*Note:* Please use `math.sqrt` instead of `sqrt`!",
        ]

    update.message.reply_text('\n'.join(welcome_txt), parse_mode = "markdown")

def show_rune(update, context):
    try:
        msg_id = update.message.message_id
    except:
        pass
    if context.args:
        success = 1
        try:
            cmd = " ".join(context.args)
            
            if overlap(bans, cmd):
                raise(Exception(error_msg))
            rune = eval(cmd, globals())

            show(rune)
            save_image(f"data/show_{update.message.chat['id']}")
            clear_all()
            try:
                update.message.reply_photo(open(f"data/show_{update.message.chat['id']}.png", 'rb'), reply_to_message_id = msg_id)
            except:
                update.message.reply_photo(open(f"data/show_{update.message.chat['id']}.png", 'rb'))
        except Exception as e:
            success -= 1
            try:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML", reply_to_message_id = msg_id)
            except:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML")

        if log_it:
            with open("data/_log_full.tsv", "a") as f:
                f.write(f"{update.message.chat['username']}{DELIMITER}{update.message.chat['id']}{DELIMITER}{msg_id}{DELIMITER}show{DELIMITER}{cmd}{DELIMITER}{success}\n")
                f.close()
    else:
        try:
            update.message.reply_text('Sorry, please give me something to show.', reply_to_message_id = msg_id)
        except:
            update.message.reply_text('Sorry, please give me something to show.')

def anaglyph_rune(update, context):
    try:
        msg_id = update.message.message_id
    except:
        pass
    if context.args:
        success = 1
        try:
            cmd = " ".join(context.args)
                    
            if overlap(bans, cmd):
                raise(Exception(error_msg))
            rune = eval(cmd, globals())
            
            anaglyph(rune)
            save_image(f"data/anaglyph_{update.message.chat['id']}")
            clear_all()
            try:
                update.message.reply_photo(open(f"data/anaglyph_{update.message.chat['id']}.png", 'rb'), reply_to_message_id = msg_id)
            except:
                update.message.reply_photo(open(f"data/anaglyph_{update.message.chat['id']}.png", 'rb'))
        except Exception as e:
            success -= 1
            try:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML", reply_to_message_id = msg_id)
            except:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML")

        if log_it:
            with open("data/_log_full.tsv", "a") as f:
                f.write(f"{update.message.chat['username']}{DELIMITER}{update.message.chat['id']}{DELIMITER}{msg_id}{DELIMITER}anaglyph{DELIMITER}{cmd}{DELIMITER}{success}\n")
                f.close()
    else:
        try:
            update.message.reply_text('Sorry, please give me something to show.', reply_to_message_id = msg_id)
        except:
            update.message.reply_text('Sorry, please give me something to show.')

def hollusion_rune(update, context):
    try:
        msg_id = update.message.message_id
    except:
        pass
    if context.args:
        success = 1
        try:
            cmd = " ".join(context.args)
                    
            if overlap(bans, cmd):
                raise(Exception(error_msg))
            rune = eval(cmd, globals())
            
            hollusion(rune)
            save_hollusion(f"data/hollusion_{update.message.chat['id']}")
            clear_all()
            try:
                update.message.reply_animation(open(f"data/hollusion_{update.message.chat['id']}.gif", 'rb'), reply_to_message_id = msg_id)
            except:
                update.message.reply_animation(open(f"data/hollusion_{update.message.chat['id']}.gif", 'rb'))
        except Exception as e:
            success -= 1
            try:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML", reply_to_message_id = msg_id)
            except:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML")

        if log_it:
            with open("data/_log_full.tsv", "a") as f:
                f.write(f"{update.message.chat['username']}{DELIMITER}{update.message.chat['id']}{DELIMITER}{msg_id}{DELIMITER}hollusion{DELIMITER}{cmd}{DELIMITER}{success}\n")
                f.close()
    else:
        try:
            update.message.reply_text('Sorry, please give me something to show.', reply_to_message_id = msg_id)
        except:
            update.message.reply_text('Sorry, please give me something to show.')

def stereogram_rune(update, context):
    msg_id = update.message.message_id
    if context.args:
        success = 1
        try:
            cmd = " ".join(context.args)
                    
            if overlap(bans, cmd):
                raise(Exception(error_msg))
            rune = eval(cmd, globals())
            
            stereogram(rune)
            save_image(f"data/stereogram_{update.message.chat['id']}")
            clear_all()
            try:
                update.message.reply_photo(open(f"data/stereogram_{update.message.chat['id']}.png", 'rb'), reply_to_message_id = msg_id)
            except:
                update.message.reply_photo(open(f"data/stereogram_{update.message.chat['id']}.png", 'rb'))
        except Exception as e:
            success -= 1
            try:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML", reply_to_message_id = msg_id)
            except:
                update.message.reply_text(f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode = "HTML")

        if log_it:
            with open("data/_log_full.tsv", "a") as f:
                f.write(f"{update.message.chat['username']}{DELIMITER}{update.message.chat['id']}{DELIMITER}{msg_id}{DELIMITER}stereogram{DELIMITER}{cmd}{DELIMITER}{success}\n")
                f.close()
    else:
        try:
            update.message.reply_text('Sorry, please give me something to show.', reply_to_message_id = msg_id)
        except:
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
