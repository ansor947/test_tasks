from calendar import Calendar, FRIDAY
import re

def get_last_friday(string: str) -> str:
    pattern = r"\W+"
    string_reg = re.split(pattern, string)
    dates = Calendar().monthdatescalendar(int(string_reg[1]), int(string_reg[0]))
    # dates = Calendar().monthdatescalendar(2023, 6)
    friday_list = []
    for week in dates:
        if week[FRIDAY].strftime("%m") == string_reg[0]:
            friday_list.append(week[FRIDAY])

    return type(str(friday_list[-1]))


# print(get_last_friday('08/2022'))


    