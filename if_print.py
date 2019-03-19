A = int(input()) # Рекомендация спать не менее
B = int(input()) # Рекомендация спать не более
H = int(input()) # Спит
if (H >= A) and (H <= B) and (A <= B):
        print('Это нормально')
if (H < A) and (A <= B):
        print('Недосып')
if (H > B) and (A <= B):
        print('Пересып')

