my_list = [1,2,3,4,5]

iterable = iter(my_list)

sum_of_products = next(iterable, 'there is nothing to iterate :(')

for i in iterable:
    sum_of_products*=i

print(sum_of_products)