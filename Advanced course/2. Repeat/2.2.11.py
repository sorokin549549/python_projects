word = input() + ' запретил букву'
b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word2 = 0
for i in range(32):
    if b[i] in word:


        print(word, b[i])

        word = word.replace(b[i], '')
        word = word.strip()
        if '  ' in word:
            word = word.replace("  ", " ")












