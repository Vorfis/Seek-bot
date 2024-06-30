import csv

def find_phone_number(filename, phone_number):

  with open(filename, 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      if phone_number in row:
        
        row.remove(phone_number)
        return ', '.join(row)
  return None


phone_number = input("Введите номер телефона: ")

filename = "EYEOFGOD telegram 774k.csv"  

result = find_phone_number(filename, phone_number)

if result:
  print(f"Найдено соответствие: {result}")
else:
  print(f"Номер телефона {phone_number} не найден.")

