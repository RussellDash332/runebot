from runes import *
from graphics import *
from env import TOKEN, DELIMITER
import requests

commands = ["show", "anaglyph", "hollusion", "stereogram"]

for command in commands:
    with open(f"data/waiting_list_{command}.txt") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(DELIMITER)
            chat_id, msg_id, rune = int(data[0]), int(data[1]), data[2]
            try:
                exec(f"{command}({rune})")
                if command == "hollusion":
                    save_hollusion("data/hollusion")
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendAnimation",
                                  data={'chat_id': chat_id, 'reply_to_message_id': msg_id},
                                  files={'animation': open(f"data/{command}.gif", 'rb')})
                else:
                    save_image(f"data/{command}")
                    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
                                  data={'chat_id': chat_id, 'reply_to_message_id': msg_id},
                                  files={'photo': open(f"data/{command}.png", 'rb')})
            except Exception as e:
                print(e) # for logging
            clear_all()

    open(f"data/waiting_list_{command}.txt", "w").close() # clean content
