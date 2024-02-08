time_in_minutes = int(input('Введите время в минутах: '))
hours = time_in_minutes // 60

print(f'{time_in_minutes} мин = {hours} час {time_in_minutes - (hours*60)} мин')
# 250 мин = 4 час 10 мин