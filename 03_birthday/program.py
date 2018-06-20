import datetime


def print_header():
    print('---------------------------------')
    print('          BIRTHDAY APP')
    print('---------------------------------')
    print()


def get_birthday_from_user():
    print('When were you born?')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.date(year, month, day)

    return birthday


def get_difference_between_dates(original_date, now):
    original_with_actual_year = datetime.date(now.year, original_date.month, original_date.day)

    return (original_with_actual_year - now).days


def print_days(days):
    if days < 0:
        print('Your birthday was {} days ago'.format(-days))
    elif days > 0:
        print('Your birthday will be in {} days'.format(days))
    else:
        print('Happy birthday! :D')


def main():
    print_header()

    bday = get_birthday_from_user()

    now = datetime.date.today()

    days = get_difference_between_dates(bday, now)

    print_days(days)


if __name__ == "__main__":
    main()
