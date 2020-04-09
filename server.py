from bot import telegram_chatbot

bot = telegram_chatbot("config.cfg")

def profanity_check(text):
    dictionary = ["bad","verybad"]
    if set(dictionary).intersection(set(text.split())):
        return True
    else:
        return False

def make_reply(msg):
    reply = None
    if msg is not None:
        reply ="Working!"
    return reply

update_id = None

while True:
    print("...")
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)
    print("...")

