from counting import sum_of_numbers


def test_of_sum_of_numbers():
    assert sum_of_numbers(1, 1) == 2
    assert sum_of_numbers(-1, -1) == -2
    assert sum_of_numbers(-1, 1) == 0
    assert sum_of_numbers(1, -1) == 0
    assert sum_of_numbers(0, 0) == 0
    return "test_sum_of_numbers() passed"


print(test_of_sum_of_numbers())
