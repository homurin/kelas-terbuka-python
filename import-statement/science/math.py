def add(*num: float) -> float:
    results = num[0]
    for i in num[1:]:
        results += i
    return results


def substract(*num: float) -> float:
    results = num[0]
    for i in num[1:]:
        results -= i
    return results


def multiply(*num: float) -> float:
    results = num[0]
    for i in num[1:]:
        results *= i
    return results


def divide(*num: float) -> float:
    results = num[0]
    for i in num[1:]:
        results /= i
    return results
