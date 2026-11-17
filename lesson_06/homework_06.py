# task 6.1
text = input("Введи рядок: ")
unique_count = len(set(text))
#print(text)
print(unique_count > 10)

# task 6.2
word = input("Введи слово з літерою h: ")
while "h" not in word.lower():
    word = input("Немає h, спробуй ще: ")
print("Є h! Ти ввів:", word)

# task 6.3
list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem 1psum']
list_2 = []
for item in list_1:
    if isinstance(item, str):
        list_2.append(item)
print(list_2)

# task 6.4
list_int = [1, 2, 3, 4, 5, 6, 0, -2, -3, 10, 321, -41231, 123, 555, 32, -1]
total = sum([n for n in list_int if n % 2 == 0])
print(f"Сума парних чисел: {total}")