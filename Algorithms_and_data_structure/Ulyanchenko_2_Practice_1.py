"""
Implement a function to calculate the sum of the numerical values in a nested list. For example :
sum_nested([1, [2, [3, [4]]]]) -> 10
"""
to_calculate = [1, 10, [2, [33, [4], [14, [4]]]]]


def sun_nested(data):
    total_sum = 0
    for el in data:
        if isinstance(el, list):
            total_sum += sun_nested(el)
        else:
            total_sum += el
    return total_sum


print(sun_nested(to_calculate))
