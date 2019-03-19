age = 36
while True:
    print ("Мой возраст. Должен ходить на работу :-(" , age)
    age += 1
    if age > 65:
        print ("Ура! Наконец-то пенсия!")
        break

week_days = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]

for index in range(len(week_days)): # функция len(sequence) возвращает длину (колчество элементов) в sequence
    print (week_day[index])
