print("Task 1-3:")
alice_in_wonderland = ('"Would you tell me, please, which way I ought to go from here?"\n'
                       '"That depends a good deal on where you want to get to," said the Cat.\n'
                       '"I don\'t much care where ——" said Alice.\n'
                       '"Then it doesn\'t matter which way you go," said the Cat.\n'
                       '"—— so long as I get somewhere," Alice added as an explanation.\n'
                       '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
print('', "Task 4:", sep="\n")
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436_402
azov_sea_area = 37_800
summ_area = black_sea_area + azov_sea_area

print(f'Так як площа Чорного моря {black_sea_area} км2, а площа Азовського моря - {azov_sea_area} км2,\n '
      f'то для того щоб знайти загальну площу яку займають два моря \n'
      f'необхідно додати дві площі {black_sea_area} + {azov_sea_area} та отримуємо {summ_area} км2.\n'
      f'Відповідь: {summ_area} км2 площа, яку займають Чорне та Азовське моря разом')

# task 05
print('', "Task 5:", sep="\n")
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sklad_123 = 375_291
sklad_12 = 250_449
sklad_23 = 222_950
sklad_1 = sklad_123-sklad_23
sklad_2 = sklad_12 - sklad_1
sklad_3 = sklad_123-sklad_12
# print(sklad_12 - sklad_1 == sklad_23-sklad_3)
print(f'Всього на 3-х складах {sklad_123} товару, а на першому та другому {sklad_12} товарів.',
      f'Тобто для того, щоб дізнатися скільки продуктів на третьому складні необхідно від загальної',
      f'кількості товару відняти суму товару на перших двох складах і виходить: '
      f'{sklad_123} - {sklad_12} = {(sklad_123-sklad_12)}.',
      f'Так само можна обчислити суму товару на першому складі, віднявши від загальної кількості '
      f'суму товарів на другому та третьому складі: {sklad_123} - {sklad_23} = {(sklad_123-sklad_23)}.',
      'Залишилось обчислити скільки товарів на другому складі і '
      'тут можна виконати віднімання декількома способами:',
      f'спосіб 1: від суми всіх товірав відняти суму першого і третього складу: '
      f'{sklad_123} - {sklad_1} - {sklad_3} = {(sklad_123-sklad_1-sklad_3)}',
      'спосіб 2: від суми першого і другого складу відняти товари, що на першому складі: '
      f'{sklad_12} - {sklad_1} = {(sklad_12-sklad_1)}',
      'спосіб 3: від суми другого і третього складу відняти товари, що на третьому складі: '
      f'{sklad_23} - {sklad_3} = {(sklad_23-sklad_3)}', sep="\n")
print(f"Відповідь: На першому складі {sklad_1} товарів, "
      f"на другому складі {sklad_2} товарів та на третьому - {sklad_3} товарів")

# task 06
print('', "Task 6:", sep="\n")
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_time = int(1.5*12)
credit_monthly_part = 1179
leptop_cost = float(credit_time * credit_monthly_part)
print(f'Так як кожного місяця потрібно буде виплачувати {credit_monthly_part} грн, а термін дії кредиту півтора року\n'
      f'тобто 12 місяців + 6 місяців = {credit_time} місяців, то варість комп\'ютера дорівнює\n'
      f'{credit_monthly_part} помножити на {credit_time} і дорівнює {leptop_cost} грн.')
print(f"Відповідь: Варість комп\'ютера {leptop_cost} грн")

# task 07
print('', "Task 7:", sep="\n")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = [8019, 9907, 2789, 7248, 7128, 19224]
b = (8, 9, 5, 6, 5, 9)
i = 0
for i in range(6):
    print(f'Остача від ділення {a[i]} на {b[i]} дорівнює {a[i] % b[i]}, '
          f'де {a[i]} - {a[i] // b[i]} * {b[i]} = {a[i] % b[i]}')

# task 08
print('', "Task 8:", sep="\n")
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
all_cost = 4*274 + 2*218 + 4*35 + 1*350 + 3*21
cost_text = "4*274 + 2*218 + 4*35 + 1*350 + 3*21"
print('Для того щоб дізнатися скільки грошей необхідно Іринці для замовлення потбрібно \n'
      'перемножити кожну кількість товару на вартість. Тобто маємо наступне рівняння:\n'
      f'{cost_text} = {all_cost}\n'
      f'Відповідь: Іринці необхідно {all_cost} грн')

# task 09
print('', "Task 9:", sep="\n")
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photo = 232
album_list = 8
left_photo = photo % album_list
count_list = photo // album_list
if left_photo != 0:
    count_list = count_list+1
print('Якщо у Ігоря є 232 фотографії, а на кожній сторінці можна розмістити по 8 фотографій \n'
      'то для того, щоб знайти скільки сторінок знадобиться Ігорю потрібно провести операцію ділення.\n'
      f'{photo} розділити на {album_list} і ми отримуємо {count_list} '
      'сторінок необхідно для того щоб вклеїти всі фото\n'
      f'Відповідь: Ігорю необхідно {count_list} сторінок, щоб вклеїти всі фото')

# task 10
print('', "Task 10:", sep="\n")
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
all_way = 1600
gas_for_all_way = all_way*9/100
print('1) Для того щоб обчислити необхідну кількість бензину для всієї подорожі потрібно:\n'
      f'визначити необхідну кількіть бензину на 1 км і помножити на всю відстань між містами {all_way} км,\n'
      f'тобто 9 розділити на 100 і помножити на {all_way} = {gas_for_all_way}\n'
      f'Виходить нам потрібно {gas_for_all_way} літрів бензину')
stop_gas = int(gas_for_all_way // 48)
if (gas_for_all_way % 48) != 0:
    stop_gas = stop_gas+1
print('2) Для визначення необхідної кількості зупинок потрібно провести операцію ділення\n'
      f'де загальну кількість безнизу {gas_for_all_way} літрів ми розділимо на місткість баку 48 літрів\n'
      f'і отримуємо {gas_for_all_way} / 48 = {stop_gas} ')

print(f'Відповідь: \n'
      f'1) {gas_for_all_way} літрів бензину знадобиться для такої подорожі\n'
      f'2) Щонайменше {stop_gas} разів родині необхідно заїхати на заправку під час цієї подорожі')
