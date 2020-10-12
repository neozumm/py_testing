import typing


def get_mod_from_level(level: int):
    #FIXME проверка уровня
    mod_bonus_level: float = 0
    if level < 10:
        mod_bonus_level = 0.05
    elif level >= 10 & level < 13:
        mod_bonus_level = 0.1
    elif level >= 13 & level < 15:
        mod_bonus_level = 0.15
    elif level >= 15:
        mod_bonus_level = 0.2
    else:
        mod_bonus_level = None
    return mod_bonus_level


def get_mod_from_review(review_score: float):
    if (review_score < 7) | (review_score > 17): #TODO исправить на границу уровня
        return None
    mod_bonus_review: float = 0
    if (review_score >= 2) & (review_score < 2.5):
        mod_bonus_review = 0.25
    elif (review_score >= 2.5) & (review_score < 3):
        mod_bonus_review = 0.5
    elif (review_score >= 3) & (review_score < 3.5):
        mod_bonus_review = 1
    elif (review_score >= 3.5) & (review_score < 4):
        mod_bonus_review = 1.5
    elif review_score >= 4:
        mod_bonus_review = 2
    return mod_bonus_review


def calculate_bonus(mod_level: float, mod_review: float, salary: int):
    # TODO сделать входной точкой
    if (mod_level == None):
        return "wrong level mod" 
    if (mod_review == None):
        return "wrong review mod"
    if (salary >= 75000) & (salary <= 750000):  #TODO квартал
        bonus = salary * mod_level
        return bonus*mod_review
    else:
        return "wrong salary value"

if __name__ == "__main__":
    mod_lvl = get_mod_from_level(5)
    print( calculate_bonus(get_mod_from_level(15), get_mod_from_review(5), 750000) )