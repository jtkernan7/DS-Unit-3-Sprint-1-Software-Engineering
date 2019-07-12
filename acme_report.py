from random import randint, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def random_name():
    return choice(ADJECTIVES) + " " + choice(NOUNS)


def random_pw():
    return randint(5, 100)


def random_flame():
    return uniform(0.0, 2.5)


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        products.append(Product(random_name(), random_pw(),
                                random_pw(), random_flame()
                                ))
    return products


def inventory_report(products):
    unique_names = []
    prices = 0
    weights = 0
    flames = 0

    for product in products:
        if product.name not in unique_names:
            unique_names.append(product.name)
        prices += product.price
        weights += product.weight
        flames += product.flammability

    avg_price = prices/len(products)
    avg_weight = weights/len(products)
    avg_flame = flames/len(products)

    print('OFFICIAL ACME INVENTORY REPORT')
    print('INTERNAL USE ONLY')
    print(f'unique product names: {len(unique_names)}')
    print(f'average price: {avg_price}')
    print(f'average weight: {avg_weight}')
    print(f'average flammability: {avg_flame}')


if __name__ == '__main__':
    inventory_report(generate_products())

