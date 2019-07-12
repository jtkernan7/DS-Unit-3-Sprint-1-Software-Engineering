from random import randint, uniform, sample
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def random_name():
    return sample(ADJECTIVES, 1) + " " + sample(NOUNS, 1)


def random_pw():
    return randint(5, 100)


def random_flame():
    return uniform(0.0, 2.5)


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        products.append(Product(random_name, random_pw(),
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
    print(f'The inventory has {len(unique_names)} unique product names.')
    print(f'The average price of products is: {avg_price}')
    print(f'The average weight of products is: {avg_weight}')
    print(f'the average flammability of products is: {avg_flame}')


if __name__ == '__main__':
    inventory_report(generate_products())

