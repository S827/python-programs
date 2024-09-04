from translate import Translator

translator = Translator(to_lang='')

text = 'I am doing fine'
trans_text = translator.translate(text)

print(trans_text)

with open('test.txt', mode='r+') as my_file:
    text = my_file.readlines()
    n_text = ','.join(text)
    my_file.write(translator.translate(n_text))
