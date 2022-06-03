tickets = int(input("Введите количество билетов, шт:"))
price = 0
sum = 0
for tickets in range(1, tickets + 1):
    age_for_ticket = int(input("Возраст посетителя:"))
    if age_for_ticket < 18:
        price = 0
        print("Билет бесплатный")
    elif 18 <= age_for_ticket <= 25:
        price += 990
        print("Билет стоит 990 руб.")
    else:
        price += 1390
        print("Билет стоит 1390 руб.")
if tickets > 3:
    sum = price - ((price / 100) * 10)
    print(f'Итого к оплате {sum} руб. с учетом 10%-ой скидки регистрацию больше 3-х человек')
else:
    print(f'Итого к оплате {sum} руб.')