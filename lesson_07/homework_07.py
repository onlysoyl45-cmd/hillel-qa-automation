# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
#add = lambda x, y: x + y
#print(add(3, 4))
def add_numbers(first_number: float, second_number: float) -> float:
    """Повертає суму двох чисел."""
    return first_number + second_number


print(add_numbers(3, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers: list) -> float:
    """Повертає середнє арифметичне списку чисел."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


print(calculate_average([2, 4, 6]))
print(calculate_average([1, 2, 3, 4]))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text: str) -> str:
    """Повертає рядок у зворотному порядку."""
    return text[::-1]


print(reverse_string("Python"))
print(reverse_string("abc"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words: list) -> str:
    """Повертає найдовше слово зі списку."""
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


print(find_longest_word(["cat", "elephant", "dog"]))
print(find_longest_word(["hi", "hello", "hey"]))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1: str, str2: str) -> int:
    """Повертає індекс першого входження str2 у str1 або -1, якщо його немає."""
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7 / ДЗ_6.3
#total = 0
#list_1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem 1psum']
#for item in list_1:
#    if type(item) == int:
#        total += item
#    elif isinstance(item, str) and item.isdigit():
#        total += int(item)
#print(total)

def sum_numeric_values(items: list) -> int:
    """Повертає суму чисел і рядків із цифр у списку. bool скіп."""
    total = 0
    for item in items:
        if type(item) == int:
            total += item
        elif isinstance(item, str) and item.isdigit():
            total += int(item)
    return total


mixed_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem 1psum']
print(sum_numeric_values(mixed_list))  # 41

# task 8 / ДЗ_6
#text = input("Введи рядок: ")
#unique_count = len(set(text))
#print(unique_count > 10)

def has_many_unique_chars(text: str) -> bool:
    """Повертає True, якщо в рядку більше 10 різних символів."""
    unique_count = len(set(text))
    return unique_count > 10


print(has_many_unique_chars("hello"))        # False
print(has_many_unique_chars("abcdefghijk"))  # True

# task 9 / ДЗ_4 task 06
#first_tom = adwentures_of_tom_sawer.find("Tom")
#second_tom = adwentures_of_tom_sawer.find("Tom", first_tom + 1)
#print("Друге слово Tom зустрічається на позиції:", second_tom)

def find_second_occurrence(text: str, word: str) -> int:
    """Повертає індекс другого входження word у text або -1, якщо його немає."""
    first_position = text.find(word)
    second_position = text.find(word, first_position + 1)
    return second_position


print(find_second_occurrence("Tom met Tom", "Tom"))  # 8
print(find_second_occurrence("Tom here", "Tom"))     # -1

# task 10 / ДЗ_4 task 05
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
#words = adwentures_of_tom_sawer.split()
#capital_count = 0
#for word in words:
#    if word.lstrip('"')[0].isupper():
#        capital_count = capital_count + 1
#print(f"Слів у тексті з великої літери: {capital_count}")

def count_capitalized_words(text: str) -> int:
    """Повертає кількість слів, які починаються з великої літери."""
    words = text.split()
    capital_count = 0
    for word in words:
        if word.lstrip('"')[0].isupper():
            capital_count += 1
    return capital_count


print(count_capitalized_words("Tom and Ben met Billy"))  # 3
