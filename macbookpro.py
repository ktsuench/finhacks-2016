import datetime

products = []

with open("macbookpro.txt") as f:
    for line in f:
        products.append(line.split(' '))

for product in products:
    print(product)
    
    



