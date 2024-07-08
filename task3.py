import re;
  
def normilize_phone(phone_number: str):
  phone_number = phone_number.strip();
  
  if phone_number.startswith('38'):
    phone_number = f"+{phone_number}";

  if not phone_number.startswith('+38'):
    phone_number = f"+38{phone_number}";

  return re.sub(r"[^+\d]", '', phone_number);

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normilize_phone(num) for num in raw_numbers];
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers);

print(normilize_phone("    (050)123-32-34"));
