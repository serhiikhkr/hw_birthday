from datetime import datetime


users = [{
    'name': 'Nick',
    'birthday': '28.07.1990'},
    {
    'name': 'Rost',
    'birthday': '30.07.1993'},
    {
    'name': 'Oleg',
    'birthday': '01.06.1989'},
    {
    'name': 'Sasha',
    'birthday': '28.07.1996'},
    {
    'name': 'Parker',
    'birthday': '29.07.2000'},
    {
    'name': 'Tim',
    'birthday': '31.07.1992'},
    {
    'name': 'Sergey',
    'birthday': '27.07.1995'},
    {
    'name': 'Dina',
    'birthday': '30.07.2002'},
    {
    'name': 'Eva',
    'birthday': '27.07.2010'},
    {
    'name': 'Vlad',
    'birthday': '02.08.1989'},
]

numbers_with_days_of_week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Next Monday',
    6: 'Next Monday'
}

list_days_for_print = {
    'Monday': [],
    'Tuesday': [],
    'Wednesday': [],
    'Thursday': [],
    'Friday': [],
    'Next Monday': []
}


def get_birthday_per_week(user_list):
    selected_days = []
    text =""
    today = datetime.now().date()
    number_of_weekday_today = today.weekday()
    different = 6 - number_of_weekday_today
    ordinal_today = today.toordinal()
    for u in user_list:
        for k in u.keys():
            if k == "birthday":
                list_of_date = u[k].split('.')
                time_to_datetime = datetime(day=int(list_of_date[0]), month=int(list_of_date[1]), year=today.year).date()
                different_day = time_to_datetime.toordinal() - ordinal_today
                if 0 <= different_day <= different:
                    selected_days.append([u.get('name'), time_to_datetime.weekday()])

    for select in selected_days:
        name_of_day = numbers_with_days_of_week.get(select[1])
        list_days_for_print[name_of_day].append(select[0])

    for k, v in list_days_for_print.items():
        if len(v) > 0:
            text = text + f'{k} : {",".join(v)}\n'

    print(text)



if __name__ == "__main__":
    get_birthday_per_week(users)