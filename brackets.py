def is_correct_equation(equation):
    bracket_dict = {'}': '{', ')': '('}
    bracket_closed = bracket_dict.keys()
    bracket_opened = bracket_dict.values()
    # list with only {} and () from equation
    brackets_in_equation = [bracket for bracket in equation if bracket in [*bracket_closed, *bracket_opened]]
    if brackets_in_equation[0] in bracket_closed:
        # first bracket is closed bracket - always incorrect
        return False
    while any(bracket in brackets_in_equation for bracket in bracket_closed):
        # as long as closed bracket exists in list
        for i, bracket in enumerate(brackets_in_equation):
            if bracket in bracket_closed:
                if brackets_in_equation[i - 1] != bracket_dict[bracket]:
                    return False
                # matched brackets - remove them from list
                del brackets_in_equation[i - 1 : i + 1]
    # if every brackets were matched, list is empty which return True
    return not brackets_in_equation


assert is_correct_equation('2 * (y^{(x + 2) * 6})') is True
assert is_correct_equation('(2 - 7) + (x - 1) * ({5 * 2} - 1)') is True
assert is_correct_equation('(2 - 7)) + (x - 1) * ({5 * 2} - 1)') is False
assert is_correct_equation('(2 - 7) + (x - 1) * ({5 * 2) - 1)') is False
assert is_correct_equation(')(2 - 7) + (x - 1) * ({5 * 2} - 1)(') is False
assert is_correct_equation('(2 - 7) + (x - 1) * ({5 * 2} - 1)((') is False
