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
