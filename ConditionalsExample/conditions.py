from datetime import date


def check_validity_to_vote(birth_year):
    today = date.today()
    age = today.year - int(birth_year)
    if age >= 18:
        return "Congrats. You are allowed to vote"
    else:
        return "Sorry. You are too young to vote"

