import pandas as pd
import numpy as np


def load_data(file_path):
    print("\n--- Задание 1: Загрузка данных ---")
    df = pd.read_csv(file_path, index_col="PassengerId")
    print(f"Данные загружены, {df.shape[0]} строк, {df.shape[1]} столбцов")
    return df

def head_data(df, n=6):
    print(f"\n--- Задание 2: Первые {n} строк ---")
    print(df.head(n))

def describe_data(df):
    print("\n--- Задание 3: Статистика по данным ---")
    print(df.describe(include='all'))


def gender_count(df):
    print("\n--- Задание 4: Количество мужчин и женщин ---")
    print(df['Sex'].value_counts())

def pclass_distribution(df):
    print("\n--- Распределение пассажиров по классам ---")
    print("Общее распределение Pclass:")
    print(df['Pclass'].value_counts())
    
    print("\nРаспределение по полу:")
    print(df.groupby('Sex')['Pclass'].value_counts())
    
    male_2nd_class = df.query("Sex=='male' & Pclass==2").shape[0]
    print(f"\nКоличество мужчин 2-го класса: {male_2nd_class}")


def fare_stats(df):
    median_fare = df['Fare'].median()
    std_fare = df['Fare'].std()
    print("\n--- Задание 5: Медиана и стандартное отклонение Fare ---")
    print(f"Медиана Fare: {median_fare:.2f}")
    print(f"Стандартное отклонение Fare: {std_fare:.2f}")


def survival_by_age(df):
    young_surv = df.loc[df['Age']<30, 'Survived'].mean()
    old_surv = df.loc[df['Age']>60, 'Survived'].mean()
    print("\n--- Задание 6: Выживаемость по возрасту ---")
    print(f"Доля выживших <30 лет: {young_surv:.2f}")
    print(f"Доля выживших >60 лет: {old_surv:.2f}")

def survival_by_gender(df):
    male_surv = df.loc[df['Sex']=='male', 'Survived'].mean()
    female_surv = df.loc[df['Sex']=='female', 'Survived'].mean()
    print("\n--- Задание 7: Выживаемость по полу ---")
    print(f"Мужчины: {male_surv:.2f}")
    print(f"Женщины: {female_surv:.2f}")


def most_popular_male_name(df):
    male_names = df.loc[df['Sex']=='male', 'Name']
    first_names = male_names.apply(lambda x: x.split(',')[1].split('.')[1].strip())
    popular_name = first_names.value_counts().idxmax()
    print("\n--- Задание 8: Самое популярное мужское имя ---")
    print(f"Популярное мужское имя: {popular_name}")


def avg_age_by_class_gender(df):
    print("\n--- Задание 9: Средний возраст по классу и полу ---")
    print(df.groupby(['Pclass','Sex'])['Age'].mean().round(2))

def avg_age_survived(df):
    print("\n--- Задание 10: Средний возраст выживших и погибших ---")
    print(df.groupby('Survived')['Age'].mean().round(2))
    print("\nВывод: В среднем пассажиры 1 класса старше, чем во 2 и 3 классах")


if __name__ == "__main__":
    file_path = "data/titanic.csv"
    df = load_data(file_path)

    head_data(df)
    describe_data(df)
    gender_count(df)
    pclass_distribution(df)
    fare_stats(df)
    survival_by_age(df)
    survival_by_gender(df)
    most_popular_male_name(df)
    avg_age_by_class_gender(df)
    avg_age_survived(df)
