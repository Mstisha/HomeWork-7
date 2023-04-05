text = input("Введите текст: ")

def word(words):
    texts = words.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    arr = f(texts[0])
    if all([f(i) == arr for i in texts]):
        return 'Парам пам-пам'
    return 'Пам парам'

print(word(text))