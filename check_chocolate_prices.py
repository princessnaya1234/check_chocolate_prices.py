chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}

# Showing list of items without their prices
print('This is the list of items we have in our store:\n', chocolates.fromkeys(chocolates))

# collecting user item input and outputting its price
item_list = input('Please input an item to check its price:\n')

if item_list == 'white':
   print('The price of', item_list, 'you picked is: {}'.format(chocolates['white']))
elif item_list == 'milk':
   print('The price of', item_list, 'you picked is: {}'.format(chocolates['milk']))
elif item_list == 'dark':
   print('The price of', item_list, 'you picked is: {}'.format(chocolates['dark']))
elif item_list == 'vegan':
   print('The price of', item_list, 'you picked is: {}'.format(chocolates['vegan']))
else:
   print('This item is not in the list')
