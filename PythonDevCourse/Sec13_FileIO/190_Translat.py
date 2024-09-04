from translate import Translator

translator = Translator(to_lang='hi')
try:
    with open('./test.txt', mode='r', encoding='utf-8') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
        with open('./test_hi.txt', mode='w', encoding='utf-8') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('check your file path!')
except UnicodeEncodeError as e:
    print('Encoding error')


# translator = Translator(to_lang='de')

# text = 'I am doing fine'
# trans_text = translator.translate(text)

# print(trans_text)

# with open('test.txt', mode='r+') as my_file:
#     text = my_file.readlines()
#     n_text = ','.join(text)
#     my_file.write(translator.translate(n_text))
