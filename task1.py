import datetime;

def get_days_from_today(date: str) -> int: 
  today = datetime.datetime.today();

  try:
    date_input = datetime.datetime.strptime(date, '%Y-%m-%d');
  except ValueError as e:
    # just to show the error message
    return e;
  
  
  return (today - date_input).days;

print(get_days_from_today('2020-10-09'));