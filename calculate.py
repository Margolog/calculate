def calculate_bonus(years_worked, has_sick_leave, annual_income):
    if years_worked > 3:
        bonus_percentage = 0.30
    elif 1.5 <= years_worked <= 3:
        bonus_percentage = 0.25
    elif 0.25 <= years_worked < 1.5:
        bonus_percentage = 0.15
    else:
        return 0

    if not has_sick_leave:
        bonus_percentage += 0.03

    bonus_amount = annual_income * bonus_percentage
    return bonus_amount

