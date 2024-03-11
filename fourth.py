from datetime import datetime, timedelta

users = [
    # {"name": "Михайло", "birthday": "2010.03.16"},
    # {"name": "Марія", "birthday": "1996.09.08"},
    # {"name": "Володимир", "birthday": "1987.03.12"}
{'name': 'Liam Smith', 'birthday': '1995.03.18'},
{'name': 'Mohel Smith', 'birthday': '1995.03.19'},
{'name': 'John Dark', 'birthday': '1985.03.07'},
{'name': 'Mary Dark', 'birthday': '1985.03.08'},
{'name': 'Derek Dark', 'birthday': '1985.03.09'},
{'name': 'Jane Smith', 'birthday': '1990.03.10'},
{'name': 'Nick Darsel', 'birthday': '1984.03.11'},
{'name': 'Liam Smith', 'birthday': '1995.03.12'},
{'name': 'Mohel Smith', 'birthday': '1995.03.13'},
{'name': 'John Dark', 'birthday': '1985.03.14'},
{'name': 'Mary Dark', 'birthday': '1985.03.15'},
{'name': 'Derek Dark', 'birthday': '1985.03.16'},
{'name': 'Jane Smith', 'birthday': '1990.03.17'}
]


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)   # Заміна року на поточний для дня народження цього року

        if birthday_this_year < today:    # Якщо дата народження вже пройшла цього року
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)   # Переносимо наступний рік

        if 0 <= (birthday_this_year - today).days <= 7:     # Якщо день народження в межах вказаного періоду
            congratulation_date = birthday_this_year

            
            if congratulation_date.weekday() >= 5:    # Якщо день народження випадає на суботу або неділю
                
                
                days_until_monday = (7 - congratulation_date.weekday())                
                congratulation_date += timedelta(days=days_until_monday)

            upcoming_birthdays.append({                                                # Додаємо дані про майбутній день народження
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")      # Форматуємо дату у рядок
            })

    return upcoming_birthdays



upcoming = get_upcoming_birthdays(users)
for birthday_person in upcoming:
    print(f"Привітайте {birthday_person['name']} {birthday_person['congratulation_date']}!")