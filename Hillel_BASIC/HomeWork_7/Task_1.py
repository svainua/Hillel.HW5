# 1 Пишемо кредитний калькулятор:
# Потрібен кредитний калькулятор який може прорахувати виплати які потрібно робити клієнту кожного місяця для погашення всього кредиту.
# Кредит береться клієнтом в уставнові під певний процент - 2% в місяць перші 2 роки та 4% в місяць наступні роки. Процент нараховується що місяця на остачу що залишилaся після виплати.
# Програма запитує суму кредиту у клієнта.
# Вивести помісячно суму яку потрібно платити клєнту щоб розрахуватися з кредитом за 1, за 5 років.
# Очікується що вивід буде оформлений в у вигляді симетрично відформатованих стовбців.
# Повино бути присутнім у виводі інформаціі - номер місяця, сума виплати за місяць, та скільки процентів нараховано за місяць.

credit_sum = int(input("What is the amount of the credit (USD)?: \n"))
year_1 = 12
year_5 = 60

interest_rate_2_years = 0.02
interest_rate_3plus_years = 0.04

body_of_credit_1 = credit_sum
body_of_credit_5 = credit_sum

for month in range(1, year_1 + 1):
    month_payment = credit_sum / year_1
    payment = int(month_payment + body_of_credit_1 * interest_rate_2_years)
    body_of_credit_1 -= month_payment
    print(
        f"In month # {month} you should pay {payment} USD with {int(payment - month_payment)} USD as %"
    )

print()

month_count = 0

for month in range(1, year_5 + 1):
    month_payment = credit_sum / year_5
    if month_count < 24:
        payment = int(month_payment + body_of_credit_5 * interest_rate_2_years)
        body_of_credit_5 -= month_payment
        month_count += 1
        print(
            f"In month # {month} you should pay {payment} with {int(payment - month_payment)} USD as %"
        )
    else:
        payment = int(month_payment + body_of_credit_5 * interest_rate_3plus_years)
        body_of_credit_5 -= month_payment
        month_count += 1
        print(
            f"In month # {month} you should pay {payment} with {int(payment - month_payment)} USD as %"
        )
