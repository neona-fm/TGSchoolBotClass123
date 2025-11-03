import random

def generate_task(level=1):
    if level == 1:
        # 1 класс — сложение/вычитание до 40
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(["+", "-"])
        if op == "-" and a < b:
            a, b = b, a
        question = f"{a} {op} {b}"
        answer = str(eval(question))

    elif level == 2:
        # 2 класс — до 100, без деления с остатком
        op = random.choice(["+", "-", "*", "/"])
        a = random.randint(10, 99)
        b = random.randint(1, 99)

        if op == "-":
            if a < b:
                a, b = b, a
        elif op == "/":
            b = random.randint(1, 9)
            a = b * random.randint(1, 9)  # чтобы делилось нацело

        question = f"{a} {op} {b}"
        answer = str(int(eval(question)))

    elif level == 3:
        # 3 класс — скобки, двухзначные + однозначные
        a = random.randint(2, 9)
        b = random.randint(10, 99)
        c = random.randint(2, 9)  # однозначное умножение
        op1 = random.choice(["+", "-"])
        expr = f"({a} {op1} {b}) * {c}"
        try:
            result = eval(expr)
            if result > 1000:
                return generate_task(level)  # перегенерация
            answer = str(int(result))
        except:
            return generate_task(level)

        question = expr

    else:
        return generate_task(1)

    return question, answer
