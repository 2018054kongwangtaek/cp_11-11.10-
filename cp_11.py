import random

def lotto():
    results = []
    while len(results) < 6:
        number = random.randint(1, 45)
        if number not in results:
            results.append(number)
    results.sort()
    return results
a = lotto()
print("생성된 로또 번호는 ", a, "입니다")



