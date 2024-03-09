from datetime import datetime

def get_days_from_today(date):
  try:
    first_date = datetime.strptime(date, '%Y-%m-%d').date()
    cur_date = datetime.today().date()
    diff = (cur_date - first_date).days
    return diff
  except ValueError:
    return "Не вірний формат"
  
print (get_days_from_today(input("Введіть дату у форматі YYYY-MM-DD: ")))
