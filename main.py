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

if __name__ == "__main__":
    # Test get_day and get_cookie helper functions
    assert isinstance(get_day(crumbl_db[0]), str), "get_day not returning a string"
    assert get_day(crumbl_db[0]) == "Monday", "failed get_day test for Monday"
    
    assert isinstance(get_cookie(crumbl_db[0]), list), "get_cookie not returning a list"
    assert get_cookie(crumbl_db[0]) == ["Dubai chocolate brownie"], "failed get_cookie test"
    
    assert get_day(crumbl_db[6]) == "Sunday", "failed get_day test for Sunday"

    # Test get_day_cookie
    assert isinstance(get_day_cookie(["Monday"]), list), "get_day_cookie not returning a list"
    assert get_day_cookie(["Monday"]) == [["Dubai chocolate brownie"]], "failed get_day_cookie test for Monday"
    assert get_day_cookie(["Tuesday"]) == [["Biscoff tres leches"]], "failed get_day_cookie test for Tuesday"
    assert get_day_cookie(["Sunday"]) == [["Crumble is closed!!!"]], "failed get_day_cookie test for Sunday"
    assert get_day_cookie(["Nonexistent"]) == [], "failed get_day_cookie test for nonexistent day"

    # Test get_cookie_availability
    assert isinstance(get_cookie_availability(["brownie"]), list), "get_cookie_availability not returning a list"
    assert get_cookie_availability(["brownie"]) == ["Yes"], "failed get_cookie_availability test for brownie"
    assert get_cookie_availability(["Brownie"]) == ["Yes"], "failed get_cookie_availability test for Brownie (case insensitive)"
    assert get_cookie_availability(["chocolate"]) == ["Yes"], "failed get_cookie_availability test for chocolate"
    assert get_cookie_availability(["pizza"]) == ["No"], "failed get_cookie_availability test for pizza"
    assert get_cookie_availability(["Dubai"]) == ["Yes"], "failed get_cookie_availability test for Dubai"

    # Test get_cookie_day
    assert isinstance(get_cookie_day(["brownie"]), list), "get_cookie_day not returning a list"
    assert sorted(get_cookie_day(["brownie"])) == sorted(["Monday", "Thursday"]), "failed get_cookie_day test for brownie"
    assert sorted(get_cookie_day(["chocolate"])) == sorted(["Monday", "Wednesday"]), "failed get_cookie_day test for chocolate"
    assert get_cookie_day(["pizza"]) == ["Sorry we don't have that cookie on any day"], "failed get_cookie_day test for pizza"
    assert "Monday" in get_cookie_day(["Dubai"]), "failed get_cookie_day test for Dubai"

    # Test get_random_cookie
    result = get_random_cookie([""])
    assert isinstance(result, list), "get_random_cookie not returning a list"
    assert len(result) == 1, "failed get_random_cookie test - should return exactly one cookie"
    assert result[0] in [crumbl_db[i][1] for i in range(6)], "failed get_random_cookie test - cookie not in valid range"
    assert result[0] != ["Crumble is closed!!!"], "failed get_random_cookie test - should not return Sunday"

    # Test get_next_week_lineup
    assert isinstance(get_next_week_lineup([""]), list), "get_next_week_lineup not returning a list"

    # Test search_pa_list


    print("All tests passed! ✅")