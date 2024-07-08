import datetime;

# Helper function (Map callback)
def convert_birthday_to_datetime_obj(user):
  user['birthday'] = datetime.datetime.strptime(user['birthday'], '%Y.%m.%d').date();

  return user;

def get_upcoming_birthdays(users):
  today = datetime.datetime.today().date();
  modified_users = list(map(convert_birthday_to_datetime_obj, users));
  upcoming_birthdays_result = [];

  for user in modified_users:
    birthday_this_year = datetime.datetime(today.year, user['birthday'].month, user['birthday'].day).date();
    
    if birthday_this_year >= today and birthday_this_year - today <= datetime.timedelta(days=7):
      day_name = birthday_this_year.strftime("%A");
      
      match day_name:
        case 'Saturday':
          birthday_this_year += datetime.timedelta(days=2);
        case 'Sunday':
          birthday_this_year += datetime.timedelta(days=1);
        case _:
          pass;

      upcoming_birthdays_result.append({'name': user['name'], 'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')});

  return upcoming_birthdays_result;


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jane Smith2", "birthday": "2024.07.08"},
    {"name": "Jane Smith3", "birthday": "2024.07.09"},
    {"name": "Jane Smith4", "birthday": "2024.07.13"},
]

print(get_upcoming_birthdays(users));