print()
print("Яку кількість годин ви відпрацювали: ", end="")
hours = int(input())
print()

print("Який розмір вашої заробітньої плати погодинно: ", end="")
payOnHour = int(input())
print()

if hours > 40:
    fullPay = (payOnHour * 1.5) * hours
    print(
        "Розмір вашої заробітної плати складає =",
        fullPay,
    )
    print("Ви молодець!")
    print()
else:
    fullPay = hours * payOnHour
    print("Розмір вашої заробітної плати складає =", fullPay)
    print()
