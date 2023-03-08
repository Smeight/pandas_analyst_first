import pandas as pd


def calculate_statistics(data):
    # создаем DataFrame из данных
    df = pd.DataFrame(data)

    # вычисляем средний объем продаж в месяц
    avg_sales = df['sales'].mean()

    # находим самый популярный продукт
    most_popular_product = df.loc[df['sales'].idxmax()]['product']

    # находим продукты с самой высокой и низкой прибылью
    max_profit_product = df.loc[df['profit'].idxmax()]['product']
    min_profit_product = df.loc[df['profit'].idxmin()]['product']

    # возвращаем результаты в виде словаря
    return {
        'avg_sales': avg_sales,
        'most_popular_product': most_popular_product,
        'max_profit_product': max_profit_product,
        'min_profit_product': min_profit_product
    }


if __name__ == '__main__':
    # создаем имитационные данные
    data = {
        'product': ['pandas', 'numpy', 'plot'],
        'sales': [10120, 23422, 12412],
        'profit': [5123, 8120, 7221]
    }

    # вычисляем статистику по данным
    statistics = calculate_statistics(data)

    # выводим результаты
    print(f"Средний объем продаж в месяц: {statistics['avg_sales']}")
    print(f"Самый популярный продукт: {statistics['most_popular_product']}")
    print(f"Продукт с самой высокой прибылью: {statistics['max_profit_product']}")
    print(f"Продукт с самой низкой прибылью: {statistics['min_profit_product']}")
