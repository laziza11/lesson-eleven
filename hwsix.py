all_products = {'The whole storage': {}}
korzina = []

admin = input('Enter action: ')

product_name = input('Enter product name: ')
product_count = input('Enter quantity: ')
all_products['The whole storage'][product_name] = product_count

print(all_products)

what_to_buy = input()

while True:
    action = input('Enter action add, edit, delete: ')

    if action == 'add':
        korzina.append(what_to_buy)
        print(korzina)
    elif action == 'edit':
        print(korzina)
        product_to_edit = input('Select product to edit: ')
        new_product_name = input('Enter new product name: ')
        korzina[korzina.index(product_to_edit)] = new_product_name
        print("Cart after editing:", korzina)
    elif action == 'delete':
        product_to_delete = input('Enter the product name you want to delete: ')
        if product_to_delete in korzina:
            korzina.remove(product_to_delete)
            print("Cart after deletion:", korzina)
    else:
        print(f'Product "{product_to_delete}" not found in the cart.')

    print("Final cart:", korzina)

