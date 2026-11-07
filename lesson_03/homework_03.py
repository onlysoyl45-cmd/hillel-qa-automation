# task 01
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"'
                       '\n"That depends a good deal on where you want to get to," said the Cat.'
                       '\n"I don\'t much care where ——" said Alice.'
                       '\n"Then it doesn\'t matter which way you go," said the Cat.'
                       '\n"—— so long as I get somewhere," Alice added as an explanation.'
                       '\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for latter in alice_in_wonderland:
    if latter == "'":
        print("Знайдено апостроф:", latter)
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
print(f"Площа Чорного моря становить {black_sea} км², а площа Азовського моря становить {azov_sea} км²."
      f"\nЗагальна площа морів: {black_sea + azov_sea} км².")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщениx
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total = 375_291  #загальна к-сть товарів
first_and_second = 250_449   #к-сть на першому та другому
second_and_third = 222_950   #к-сть на другому та третьому
third_warehouse = total - first_and_second  #к-сть на третьому
first_warehouse = total - second_and_third  #к-сть на першому
second_warehouse = total - third_warehouse - first_warehouse  #к-сть на другому
print(f"На першому складі: {first_warehouse} товарів."
      f"\nНа другому складі {second_warehouse} товарів."
      f"\nНа третьому складі {third_warehouse} товарів."
      f"\nВсього товарів на складах {first_warehouse + second_warehouse + third_warehouse}.")
#самоперевірка
print(first_warehouse + second_warehouse, "має бути", first_and_second)
print(second_warehouse + third_warehouse, "має бути", second_and_third)

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
MONTHS_IN_YEAR = 12
term_years = 1.5
monthly_payment = 1179
term_months = MONTHS_IN_YEAR * term_years
computer_price = monthly_payment * term_months
print("Вартість комп'ютера:", int(computer_price),"грн")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"a) 8019 : 8 - остача {8019 % 8}"
      f"\nb) 9907 : 9 - остача {9907 % 9}"
      f"\nc) 2789 : 5 - остача {2789 % 5}"
      f"\nd) 7248 : 6 - остача {7248 % 6}"
      f"\ne) 7128 : 5 - остача {7128 % 5}"
      f"\nf) 19224 : 9 - остача {19224 % 9}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizza_total = 4 * 274
middle_pizza_total = 2 * 218
juice_total = 4 * 35
cake_total = 1 * 350
water_total = 3 * 21
order_total = big_pizza_total + middle_pizza_total + juice_total + cake_total + water_total
print("Іринці знадобиться", order_total,"грн для даного замовлення")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photo_per_page = 8
full_pages = total_photos // photo_per_page
remaining_photos = total_photos % photo_per_page
pages_needed = full_pages
if remaining_photos > 0:
    pages_needed = pages_needed + 1
print("Ігорю знадобиться",pages_needed, "сторінок, щоб вклеїти всі фото.")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
#за умови що на початку подорожі бак порожній
distance_km = 1600
fuel_per_100_km = 9
tank_volume = 48
segments = distance_km // 100
fuel_needed = segments * fuel_per_100_km
refuels_needed = fuel_needed // tank_volume
remaining_fuel = fuel_needed % tank_volume
if remaining_fuel > 0:
    refuels_needed = refuels_needed + 1
print(f"1) На дорогу {distance_km} км потрібно {fuel_needed}л бензину.")
print(f"2) Бак вміщає {tank_volume}л, тому заправлятися треба {refuels_needed} рази "
      f"(якщо виїжджаємо з порожнім баком).")