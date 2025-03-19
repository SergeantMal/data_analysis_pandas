import pandas as pd

# Создаем DataFrame с оценками учеников по 5 предметам
data = {
    'Student': ['Student 1', 'Student 2', 'Student 3', 'Student 4', 'Student 5',
                'Student 6', 'Student 7', 'Student 8', 'Student 9', 'Student 10'],
    'Math': [4, 5, 4, 1, 4, 2, 1, 1, 3, 5],
    'Science': [3, 5, 4, 1, 1, 2, 1, 4, 2, 1],
    'English': [3, 2, 4, 3, 5, 3, 1, 3, 1, 3],
    'History': [4, 5, 5, 1, 3, 3, 1, 2, 2, 2],
    'Art': [2, 1, 1, 2, 2, 1, 4, 3, 2, 4]
}

df = pd.DataFrame(data)

# Выводим таблицу
print(df.head()) # Выводим первые 5 строк

# Вычисляем среднюю оценку по каждому предмету
average_scores = df.drop('Student', axis=1).mean()

# Выводим средние оценки по предметам
print(f"\nСредние оценки по предметам:\n{average_scores}")

# Вычисляем медианную оценку по каждому предмету
median_scores = df.drop('Student', axis=1).median()

# Выводим медианные оценки по предметам
print(f"\nМедианные оценки по предметам:\n{median_scores}")

# Вычисляем квартили для предмета "Math"

Q1_math = df['Math'].quantile(0.25)

Q3_math = df['Math'].quantile(0.75)

# Вычисляем межквартильный размах

IQR_math = Q3_math - Q1_math

print("\nПервый квартиль по математике:", Q1_math,
      "\nТретий квартиль по математике:", Q3_math,
      "\nМежквартильный размах по математике:", IQR_math)


# Вычисляем стандартное отклонение для предмета "Math"
std_dev_math = df['Math'].std()

# Выводим стандартное отклонение
print("\nСтандартное отклонение по математике:", std_dev_math)