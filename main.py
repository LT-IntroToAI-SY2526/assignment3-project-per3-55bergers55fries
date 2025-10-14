from crumbl import crumbl_db
from match import match 
from typing import List, Tuple, Callable, Any

def get_day(crumb):
    return crumb[0]

def get_cookie(crumb):
    return crumb[1]

def get_monday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Monday":
            result.append(get_cookie(crumb))
    return result

def get_tuesday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Tuesday":
            result.append(get_cookie(crumb))
    return result

def get_wednesday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Wednesday":
            result.append(get_cookie(crumb))
    return result

def get_thursday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Thursday":
            result.append(get_cookie(crumb))
    return result

def get_friday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Friday":
            result.append(get_cookie(crumb))
    return result

def get_saturday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Saturday":
            result.append(get_cookie(crumb))
    return result

def get_sunday_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Sunday":
            result.append(get_cookie(crumb))
    return result
def get_next_week_lineup(matches):
    run = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Next Week":
            result.append(get_cookie(crumb))

pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what is the cookie lineup for %"), get_next_week_lineup),
    (str.split("what cookie do they serve on _"))
]
def search_pa_list(src):
    
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers']"]
    return ["I don't understand"]   
