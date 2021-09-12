# font_bot
At first I thought to use any modification from pyTelegramBotAPI for convering strings in different fonts. But pyTelegramBotAPI don`t have functionalities for it.

Then I searched any information about unicode and ways to use groups of fonts or any styles of unicode. I didn`t find python libraries for converting strings in any fonts.

So I decided to use module unicodedata as database for searching symbols in different fonts which I found  here: https://nickfinder.com/fancy-writer

But I didn`t take all fonts which found from that website because some range of strings were without logic orderliness. So font_bot have some less availables fonts than here - https://nickfinder.com/fancy-writer

Also font_bot don`t convert Cyrilic letters, signs, smiles or emojis.
