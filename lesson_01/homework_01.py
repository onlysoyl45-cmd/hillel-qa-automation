# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 3
banana = apples * 4
print("Яблук:", apples, "Бананів:", banana)

# task 05 == виправте назви змінних
side_length_1 = 1
side_length_2 = 2
side_length_3 = 3
side_length_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = side_length_1 + side_length_2 + side_length_3 + side_length_4
print("perimetery:", perimetery)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
# двояка умова, вважаю, що слив на 2 менше, ніж яблунь
trees_apple = 4
trees_pear = trees_apple + 5
trees_plum = trees_apple - 2
all_trees = trees_apple + trees_pear + trees_plum
print("Яблуні:", trees_apple)
print("Груші:", trees_pear)
print("Сливи:", trees_plum)
print("Всіх дерев:", all_trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temp_morning = 0 + 5
temp_afternoon = temp_morning - 10
temp_evening = temp_afternoon + 4
print("Температура до обіду:", temp_morning)
print("Температура після обіду:", temp_afternoon)
print("Температура надвечір:", temp_evening)

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_total = 24
girls_total = boys_total // 2
boys_sick = 1
girls_sick = 0
girls_absent = 2
boys_absent = 0
boys_today = boys_total - boys_sick - boys_absent
girls_today = girls_total - girls_sick - girls_absent
children_today = boys_today + girls_today
print("К-сть дітей сьогодні в театральному гуртку:", children_today)

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book_1 = 8
book_2 = book_1 + 2
book_3 = (book_1 + book_2) / 2
all_books_price = book_1 + book_2 + book_3
print("Ціна першої книги:", book_1, "грн.")
print("Ціна другої книги:", book_2, "грн.")
print("Ціна третьої книги:", book_3, "грн.")
print("Загальна ціна всіх книг:", all_books_price, "грн.")