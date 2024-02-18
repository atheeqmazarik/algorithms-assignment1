#100870670
#Atheeq Mazarik

def productData(file_path):
    products = {}

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue

                product_info = [info.strip() for info in line.strip().split(',')]
                product = {
                    'ID': int(product_info[0]),
                    'Name': product_info[1],
                    'Price': float(product_info[2]),
                    'Category': product_info[3]
                }
                products[product['ID']] = product
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    
    return products

def productDataUpdate(products, file_path):
    try:
        with open(file_path, 'w') as file:
            for product_id, product in products.items():
                line = f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}\n"
                file.write(line)
        print(f"'{file_path}' has been updated successfully!")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

def insertProduct(products, new_product):
    products[new_product['ID']] = new_product

def updateProduct(products, product_id, updated_info):
    if product_id in products:
        products[product_id].update(updated_info)
        print(f"Product ID {product_id} has been updated successfully!")
    else:
        print(f"Error: Product with ID {product_id} not found.")

def deleteProduct(products, product_id):
    if product_id in products:
        del products[product_id]
        print(f"Product ID {product_id} has been deleted successfully!")
    else:
        print(f"Error: Product with ID {product_id} not found.")

def searchProduct(products, key, value):
    found_products = [product.copy() for product in products.values() if product.get(key) == value]
    for product in found_products:
        product['Category'] = product['Category'].strip()
    return found_products

def bubbleSortProduct(arr, key='Price', reverse=False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if not reverse and arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            elif reverse and arr[j][key] < arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

while True:
    file_path = 'product_data.txt'
    product_data = productData(file_path)

    print("\nMenu:")
    print("1. Insert a new product")
    print("2. Update a product")
    print("3. Delete a product")
    print("4. Search for products")
    print("5. Sort products by price")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        new_product = {
            'ID': int(input("Enter ID: ")),
            'Name': input("Enter Name: "),
            'Price': float(input("Enter Price: ")),
            'Category': input("Enter Category: ")
        }
        insertProduct(product_data, new_product)
        productDataUpdate(product_data, file_path)

    elif choice == '2':
        product_id = int(input("Enter the product ID to update: "))
        updated_info = {
            'Price': float(input("Enter the updated Price: "))
        }
        updateProduct(product_data, product_id, updated_info)
        productDataUpdate(product_data, file_path)

    elif choice == '3':
        product_id = int(input("Enter the product ID to delete: "))
        deleteProduct(product_data, product_id)
        productDataUpdate(product_data, file_path)

    elif choice == '4':
        search_key = input("Enter search key for products ('ID', 'Name', 'Price', or 'Category'): ")
        search_value = input("Enter the search value for the search key: ")
        found_products = searchProduct(product_data, search_key, search_value)
        print("Found Products:", found_products)

    elif choice == '5':
        sort_order = input("Enter 'asc' to sort by ascending order. Enter 'desc' to sort descending order: ").lower()
        sorted_product_data = bubbleSortProduct(list(product_data.values()), key='Price', reverse=(sort_order == 'desc'))
        print(f"Sorted Product Data by Price ({sort_order}ending order):")
        for product in sorted_product_data:
            print(f"ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}, Category: {product['Category']}")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter a number between 1 and 6.")
