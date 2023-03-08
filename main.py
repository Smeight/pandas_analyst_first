import pandas as pd

# создаем имитационные данные
data = {
    'product': ['pandas', 'numpy', 'pylost'],
    'sales': [10120, 23422, 12412],
    'profit': [5123, 8120, 7221]
}

# создаем DataFrame из имитационных данных
df = pd.DataFrame(data)

# вычисляем средний объем продаж в месяц
avg_sales = df['sales'].mean()

# находим самый популярный продукт
most_popular_product = df.loc[df['sales'].idxmax()]['product']

# находим продукты с самой высокой и низкой прибылью
max_profit_product = df.loc[df['profit'].idxmax()]['product']
min_profit_product = df.loc[df['profit'].idxmin()]['product']

# выводим результаты
print(f"Средний объем продаж в месяц: {avg_sales}")
print(f"Самый популярный продукт: {most_popular_product}")
print(f"Продукт с самой высокой прибылью: {max_profit_product}")
print(f"Продукт с самой низкой прибылью: {min_profit_product}")
