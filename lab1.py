import typing


def get_mod_from_level(level: int):
    if not (isinstance(level, int)):
        return None
    if (level < 7) | (level > 17):
        return None
    mod_bonus_level: float = 0
    if level < 10:
        mod_bonus_level = 0.05
    elif 10 <= level < 13:
        mod_bonus_level = 0.1
    elif 13 <= level < 15:
        mod_bonus_level = 0.15
    elif level >= 15:
        mod_bonus_level = 0.2
    else:
        mod_bonus_level = None
    return mod_bonus_level


def get_mod_from_review(review_score: float):
    if not (isinstance(review_score, float) or isinstance(review_score, int)):
        return None
    if (review_score < 1) | (review_score > 5):
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


quartal = 3


def calculate_bonus(level: int, review: float, salary: int):
    mod_level = get_mod_from_level(level)
    if (mod_level == None):
        return "wrong level mod"
    mod_review = get_mod_from_review(review)
    if (mod_review == None):
        return "wrong review mod"
    if (salary >= 70000) & (salary <= 750000):
        bonus = quartal * salary * mod_level
        return bonus*mod_review
    else:
        return "wrong salary value"
