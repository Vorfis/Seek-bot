import csv

def find_phone_number(filename, phone_number):

  with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if phone_number in row:
        # Удаляем номер телефона из строки и возвращаем оставшуюся часть
        row.remove(phone_number)
        return ', '.join(row)
  return None

# Запрос номера телефона от пользователя
phone_number = input("Введите номер телефона: ")

# Имя CSV-файла
filename = "EYEOFGOD telegram 774k.csv"  # Замените "contacts.csv" на имя вашего файла

# Поиск номера телефона
result = find_phone_number(filename, phone_number)

# Вывод результата
if result:
  print(f"Найдено соответствие: {result}")
else:
  print(f"Номер телефона {phone_number} не найден.")

