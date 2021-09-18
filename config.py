import telebot

from unicodedata import category, lookup, name
import random


token = '1905611937:AAGT70k4sCp61mg5WzTBKcW_BypLEV6dJqo'
bot = telebot.TeleBot(token)


font_list = ['LATIN SMALL LETTER x WITH STROKE',
             'LATIN SMALL LETTER x',
             'NEGATIVE SQUARED LATIN CAPITAL LETTER x',
             'MATHEMATICAL BOLD SCRIPT SMALL x',
             'LATIN LETTER SMALL CAPITAL x',
             'FULLWIDTH LATIN SMALL LETTER x',
             'MATHEMATICAL SCRIPT SMALL x',
             'MATHEMATICAL BOLD FRAKTUR SMALL x',
             'LATIN SMALL LETTER TURNED x',
             'MATHEMATICAL FRAKTUR SMALL x',
             'MATHEMATICAL DOUBLE-STRUCK SMALL x',
             'MODIFIER LETTER SMALL x',
             'CYRILLIC SMALL LETTER x',
             ]


def font_code(string):
    """
    Input string will convert to every font from font_list. If current font don`t exists for current symbol circle
    circle <while> will take random font from font_list for current symbol.
    But if current symbol is a smile, a sign or it matches to Cyrillic symbols it will be returned without converting.
    :param string:
    :return: new_string
    """
    new_string = ''
    for font in font_list:
        new_char = ''

        for s in string:

            if s != ' ' and (category(s)[0] not in 'SNP'):  # checking if <s> matches to a smile, a sign or a whitespace

                try:
                    if not name(s).startswith('CYRILLIC') and (not name(s).startswith('CJK')):
                        look = f'{font}'.replace('x', s)
                        if s.isupper() and not font.startswith('NEGATIVE'):
                            look = look.replace('SMALL', 'CAPITAL')
                        new_char += lookup(look)
                    else:
                        new_char += s
                except KeyError:
                    while True:
                        index = random.randrange(0, len(font_list), 1)
                        try:
                            look = f'{font_list[index]}'.replace('x', s)
                            new_char += lookup(look)
                            break
                        except KeyError:
                            continue

            else:
                new_char += s

        new_string += f'{new_char}\n'

    return new_string
