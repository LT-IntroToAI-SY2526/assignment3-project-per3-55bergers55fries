from crumbl_db import crumbl_db
from match import match 
from typing import List, Tuple, Callable, Any
import random

def get_day(crumb):
    return crumb[0]

def get_cookie(crumb):
    return crumb[1]

def get_day_cookie(matches):
    day = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == day:
            result.append(get_cookie(crumb))
    return result

def get_next_week_lineup(matches):
    run = matches[0]
    result = []
    for crumb in crumbl_db:
        if get_day(crumb) == "Next Week":
            result.append(get_cookie(crumb))
    return result

def get_cookie_availability(matches):
    cookie = matches[0]
    available = False
    result = []
    for crumb in crumbl_db:
        if cookie.lower() in get_cookie(crumb)[0].lower(): 
            available = True
            break
    if available:
        result.append("Yes")
    else:
        result.append("No")
    return result


def get_random_cookie(matches):
    run = matches[0]
    result = []
    rand = random.randint(0, 5)
    result.append(crumbl_db[rand][1])
    return result

def get_cookie_day(matches):
    cookie = matches[0]
    result = []
    for crumb in crumbl_db:
        if cookie.lower() in get_cookie(crumb)[0].lower():
            result.append(get_day(crumb))
    if len(result) > 0:
        return result
    else:
        return ["Sorry we don't have that cookie on any day"]
    
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what is the cookie lineup for %"), get_next_week_lineup),
    (str.split("what cookie do they serve on _"), get_day_cookie),
    (str.split("give me a random cookie"), get_random_cookie),
    (str.split("do you have %"), get_cookie_availability),
    (str.split("what day do they serve %"), get_cookie_day)
]
def search_pa_list(src):
    
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["No answers']"]
    return ["I don't understand"]   
