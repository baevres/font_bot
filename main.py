from config import *


def start(msg):
    response = 'Hello 🖐, I convert input string in different font styles which I can.\n' \
               'Just type any string and I will convert it.\n' \
               'But if input data isn`t a string or don`t consists of latin letters I won`t convert it!\n' \
               'Also, don`t type too long text.'
    bot.send_message(msg.chat.id, response)


def font_msg(msg):
    new_msg = msg.text.encode().decode('utf-8')
    response = font_code(new_msg)
    bot.send_message(msg.chat.id, response)


def operator(msg):
    for m in msg:
        chat = m.chat.id
        try:
            if m.content_type == 'text':
                if m.text == '/start':
                    start(m)
                else:
                    font_msg(m)
            else:
                raise KeyError
        except KeyError:
            resp = '😓 Sorry, I understand only text messages'
            bot.send_message(chat, resp)


bot.set_update_listener(operator)

bot.polling(none_stop=True, interval=0)

