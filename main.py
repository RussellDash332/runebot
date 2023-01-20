from env import TOKEN
from runes import *
import os, telebot, hashlib, json

error_msg = "I smell a sense of power abuse. Fix the keywords :\")"
# For now it's a blacklist instead of whitelist
bans = ["exec", "eval", "import", "with", "code",
        "open", "close", "globals", "exit", "locals",
        "print", "quit", "super", "vars", "name", "main",
        "doc", "package", "loader", "class", "debug", "raise",
        "input", "dir", "try", "except", "staticmethod", "help",
        "builtin", "attr"]
def overlap(arr, string):
    for i in arr:
        if i in string:
            return True
    return False

for code in json.load(open('secret_runes.json', 'r'))['runes']:
    exec(code)

bot = telebot.TeleBot(TOKEN)

def compile(message, fn):
    try:
        clear_all()
        try:
            cmd = message.text.strip()
            if overlap(bans, cmd):
                raise Exception(error_msg)
            rune = eval(cmd, globals())

            fn(rune)
            if fn != hollusion:
                bot.send_photo(message.chat.id, vp[1], caption=f'`{cmd}`', parse_mode="markdown")
            else:
                # LOL hax
                filename = hashlib.sha256(str(message.__dict__).encode()).hexdigest()
                save_hollusion(filename)
                filename += '.gif'
                bot.send_animation(message.chat.id, open(filename, 'rb'), caption=f'`{cmd}`', parse_mode="markdown")
                os.remove(filename)
            clear_all()
        except Exception as e:
            if e.__class__.__name__ == "RecursionError":
                e = "RecursionError! Probably input number too high, I'm not that strong :("
            bot.reply_to(message, f'Sorry, it seems that there is an error. Try again.\n<b>Note:</b> {e}', parse_mode="HTML")
    except Exception as e:
        bot.reply_to(message, "Query cannot be parsed, am truly sorry :'(")

if __name__ == "__main__":
    print("Press CTRL + C to kill the bot")
    
    @bot.message_handler(commands=['start'])
    def show_welcome(message):
        welcome_txt = [
            "*Welcome to the official Rune Compiler Bot! (v3.0.0)*",
            "",
            "Compile your rune here! Here's how to use them:",
            "/show to just show the rune without any special effect",
            "/anaglyph to show the rune with a glitchy 3D-effect",
            "/hollusion to get the hollusion GIF of the rune",
            "/stereogram to generate a stereogram of the rune",
            "",
            "After inputting one of the commands above, the bot will request for the rune to be compiled.",
            "For example: `circle_bb`, `sail_bb`, `nova_bb`, `stack(rcross_bb, black_bb)`",
            "",
            "Other supported runes:",
            "- `cs1010s(rune)`, generates a CS1010S-shaped rune art",
            "- `number(n, rune)`, our newest number system",
            "- `qr(bytes)`"
            "- `chess()`, build a chessboard with just runes",
            "- `pawn_bb`",
            "- `rook_bb`",
            "- `knight_bb`",
            "- `bishop_bb`",
            "- `queen_bb`",
            "- `king_bb`",
            "- (Advanced) `chess(pieces_str)`, each from `\"PRNBQKprnbqk\"` represents a chess piece",
            "",
            "Some runes made from the supporting runes that you can try:",
            "- `cs1010s(rcross_bb)`",
            "- `number(123 * 45, nova_bb)`",
            "- `number(31415, sail_bb)`",
            "",
            "Have fun!"
        ]
        bot.reply_to(message, '\n'.join(welcome_txt), parse_mode="markdown")

    @bot.message_handler(commands=['show'])
    def show_ask_rune(message):
        text = "Enter the rune that you want to show"
        sent_msg = bot.reply_to(message, text, parse_mode="markdown")
        bot.register_next_step_handler(sent_msg, show_send_rune)
    def show_send_rune(message):
        compile(message, show)

    @bot.message_handler(commands=['anaglyph'])
    def anaglyph_ask_rune(message):
        text = "Enter the rune that you want to apply anaglyph on"
        sent_msg = bot.reply_to(message, text, parse_mode="markdown")
        bot.register_next_step_handler(sent_msg, anaglyph_send_rune)
    def anaglyph_send_rune(message):
        compile(message, anaglyph)

    @bot.message_handler(commands=['hollusion'])
    def hollusion_ask_rune(message):
        text = "Enter the rune that you want to make a GIF hollusion on"
        sent_msg = bot.reply_to(message, text, parse_mode="markdown")
        bot.register_next_step_handler(sent_msg, hollusion_send_rune)
    def hollusion_send_rune(message):
        compile(message, hollusion)

    @bot.message_handler(commands=['stereogram'])
    def stereogram_ask_rune(message):
        text = "Enter the rune that you want to apply stereogram on"
        sent_msg = bot.reply_to(message, text, parse_mode="markdown")
        bot.register_next_step_handler(sent_msg, stereogram_send_rune)
    def stereogram_send_rune(message):
        compile(message, stereogram)

    bot.infinity_polling()