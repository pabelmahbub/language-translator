


from googletrans import Translator

translator = Translator()

my_speech1 = '''


William Shakespeare, Sonnet 33.

Even so my sun one early morn did shine,
With all triumphant splendour on my brow;
But out, alack, he was but one hour mine,
The region cloud hath mask’d him from me now ... ...'''

out = translator.translate(my_speech1, dest='ja')
print(out)

