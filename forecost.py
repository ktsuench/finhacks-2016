import datetime

products = []

with open("macbookpro.data") as f:
    for line in f:
        products.append(line.split(' '))

for product in products:
    print(product)