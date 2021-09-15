# from env import TOKEN, DELIMITER
import os
TOKEN, DELIMITER, DP_URL = os.environ['TOKEN'], os.environ['DELIMITER'], os.environ['DP_URL']

from runes import *
from json import loads
from urllib import request, parse

from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode

error_msg = "I smell a sense of power abuse. Fix the keywords :\")"

# For now it's a blacklist instead of whitelist
bans = ["exec", "eval", "import", "with", "code",
        "open", "close", "globals", "exit", "locals",
        "print", "quit", "super", "vars", "name", "main",
        "doc", "package", "loader", "class", "debug", "raise",
        "input", "dir", "try", "except", "staticmethod", "help",
        "builtin", "attr"]
log_it = False # set to False because GitHub Actions won't log it anyway

def overlap(arr, string):
    for i in arr:
        if i in string:
            return True
    return False

def read_dp():
	full_url = [DP_URL, '.body.json?lastUpdate=0']
	with request.urlopen(''.join(full_url)) as response:
		resp = response.read()

	return loads(resp.decode())['body']

# Secret runes
for cmd in loads(read_dp())["commands"]:
    exec(cmd, globals())

def start(update, context):
    welcome_txt = [
        "*Welcome to the official Rune Compiler Bot!*",
        "",
        "Compile your rune here! Here's a sample execution:",
        "/show heart\_bb",
        "/anaglyph circle\_bb",
        "/hollusion nova\_bb",
        "/stereogram sail\_bb",
        "",
        "Other supported functions:",
        "`beside(r1, r2)`",
        "`stack(r1, r2)`",
        "`stackn(n, rune)`",
        "`overlay(r1, r2)`",
        "`stack_frac(frac, r1, r2)`",
        "`overlay_frac(frac, r1, r2)`",
        "`make_cross(rune)`",
        "`mosaic(a, b, c, d)`",
        "`simple_fractal(rune)`",
        "`egyptian(rune, n)`",
        "`fractal(rune, n)`",
        "`dual_fractal(pic1, pic2, n)`",
        "`steps(a, b, c, d)`",
        "`tree(n, rune)`",
        "`helix(rune, n)`",
        "`cs1010s(rune)`",
        "`number(n, rune = circle_bb)`",
        "`chess()`",
        "`chess(pieces_str)`",
        "",
        "*Note:* Please use `random` instead of `random.random`!",
        ]

    update.message.reply_text('\n'.join(welcome_txt), parse_mode = "markdown")

def show_rune(update, context):
    try:
        clear_all()
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
                save_image(f"show_{update.message.chat['id']}")
                clear_all()
                try:
                    update.message.reply_photo(open(f"show_{update.message.chat['id']}.png", 'rb'), reply_to_message_id = msg_id)
                except:
                    update.message.reply_photo(open(f"show_{update.message.chat['id']}.png", 'rb'))
            except Exception as e:
                success -= 1
                if e.__class__.__name__ == "RecursionError":
                    e = "RecursionError! Probably input number too high, I'm not that strong :("
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
    except:
        update.message.reply_text("BadRequest error. Please try another query.")

def anaglyph_rune(update, context):
    try:
        clear_all()
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
                save_image(f"anaglyph_{update.message.chat['id']}")
                clear_all()
                try:
                    update.message.reply_photo(open(f"anaglyph_{update.message.chat['id']}.png", 'rb'), reply_to_message_id = msg_id)
                except:
                    update.message.reply_photo(open(f"anaglyph_{update.message.chat['id']}.png", 'rb'))
            except Exception as e:
                success -= 1
                if e.__class__.__name__ == "RecursionError":
                    e = "RecursionError! Probably input number too high, I'm not that strong :("
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
    except:
        update.message.reply_text("BadRequest error. Please try another query.")

def hollusion_rune(update, context):
    try:
        clear_all()
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
                save_hollusion(f"hollusion_{update.message.chat['id']}")
                clear_all()
                try:
                    update.message.reply_animation(open(f"hollusion_{update.message.chat['id']}.gif", 'rb'), reply_to_message_id = msg_id)
                except:
                    update.message.reply_animation(open(f"hollusion_{update.message.chat['id']}.gif", 'rb'))
            except Exception as e:
                success -= 1
                if e.__class__.__name__ == "RecursionError":
                    e = "RecursionError! Probably input number too high, I'm not that strong :("
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
    except:
        update.message.reply_text("BadRequest error. Please try another query.")

def stereogram_rune(update, context):
    try:
        clear_all()
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
                
                stereogram(rune)
                save_image(f"stereogram_{update.message.chat['id']}")
                clear_all()
                try:
                    update.message.reply_photo(open(f"stereogram_{update.message.chat['id']}.png", 'rb'), reply_to_message_id = msg_id)
                except:
                    update.message.reply_photo(open(f"stereogram_{update.message.chat['id']}.png", 'rb'))
            except Exception as e:
                success -= 1
                if e.__class__.__name__ == "RecursionError":
                    e = "RecursionError! Probably input number too high, I'm not that strong :("
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
    except:
        update.message.reply_text("BadRequest error. Please try another query.")

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
