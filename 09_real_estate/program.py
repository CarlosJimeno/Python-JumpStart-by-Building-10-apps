import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-----------------------------------------')
    print('       REAL ESTATE DATA MINING APP')
    print('-----------------------------------------\n')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            purchases.append(Purchase.create_from_dict(row))

    return purchases


def query_data(data):
    sorted_by_price = sorted(data, key=lambda p: p.price)

    most_expensive = sorted_by_price[-1]
    print("The most expensive house is ${:,} with {} beds and {} baths"
          .format(most_expensive.price, most_expensive.beds, most_expensive.baths))

    least_expensive = sorted_by_price[0]
    print("The least expensive house is ${:,} with {} beds and {} baths"
          .format(least_expensive.price, least_expensive.beds, least_expensive.baths))

    avg_price = statistics.mean([p.price for p in data])
    print("The average price of a house was ${:,}".format(round(avg_price, 2)))

    avg_price_2_bedrooms_home = statistics.mean([p.price for p in data if p.beds == 2])
    print("The average price of a 2 bedroom house was ${:,}".format(round(avg_price_2_bedrooms_home, 2)))

    """
    Generator expressions: 
    
    (p.price for p in data if p.beds == 2) using '( )' instead of '[ ]'
    """


if __name__ == '__main__':
    main()
