#100870670 #Atheeq Mazarik

import time

def productData(file_path):
    products = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():  # Skip empty lines
                    continue

                productDesc = [info.strip() for info in line.strip().split(',')]
                product = {
                    'ID': int(productDesc[0]),
                    'Name': productDesc[1],
                    'Price': float(productDesc[2]),
                    'Category': productDesc[3]
                }
                products[product['ID']] = product
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.") 
    return products

def loadProductData(products, file_path):
    try:
        with open(file_path, 'w') as file:
            for product_id, product in products.items():
                line = f"{product['ID']}, {product['Name']}, {product['Price']}, {product['Category']}\n"
                file.write(line)
        print(f"'{file_path}' has been updated successfully!")
    except IOError:
        print(f"Error: Unable to write to file '{file_path}'.")

def insertProduct(products, newProduct):
    products[newProduct['ID']] = newProduct

def updateProduct(products, product_id, updatedProductDesc):
    if product_id in products:
        products[product_id].update(updatedProductDesc)
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
    foundProducts = [product.copy() for product in products.values() if product.get(key) == value]
    for product in foundProducts:
        product['ID'] = product['ID']
        product['Name'] = product['Name'].strip()
        product['Price'] = product['Price']
        product['Category'] = product['Category'].strip()
        
    return foundProducts

def bubbleSortProduct(arr, key='Price', reverse=False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            swap = arr[j][key] > arr[j + 1][key] if not reverse else arr[j][key] < arr[j + 1][key]
            if swap:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def printProductList(products):
    print("\nProduct List:")
    for product in products.values():
        print(f"ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}, Category: {product['Category']}")
    print()

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
        newProduct = {
            'ID': int(input("Enter ID: ")),
            'Name': input("Enter Name: "),
            'Price': float(input("Enter Price: ")),
            'Category': input("Enter Category: ")
        }
        insertProduct(product_data, newProduct)
        loadProductData(product_data, file_path)
        print("\nInserted Product:")
        print(newProduct)
        printProductList(product_data)

    elif choice == '2':
        product_id = int(input("Enter the product ID to update: "))
        updatedProductDesc = {
            'ID': int(input("Enter the updated ID: ")),
            'Name': input("Enter the updated Name: "),
            'Price': float(input("Enter the updated Price: ")),
            'Category': input("Enter the updated Category: ")
        }
        updateProduct(product_data, product_id, updatedProductDesc)
        loadProductData(product_data, file_path)
        print("\nUpdated Product:")
        print(product_data[product_id])
        printProductList(product_data)

    elif choice == '3':
        product_id = int(input("Enter the product ID to delete: "))
        deleted_product = product_data.get(product_id, {})
        deleteProduct(product_data, product_id)
        loadProductData(product_data, file_path)
        print("\nDeleted Product:")
        print(deleted_product)
        printProductList(product_data)

    elif choice == '4':
        searchDesc = input("Enter search descriptor for products ('ID', 'Name', 'Price', 'Category'): ")

        if searchDesc == "Name" or searchDesc == "Category":
            searchValue = input("Enter the search value for the chosen descriptor: ")
            foundProducts = searchProduct(product_data, searchDesc, searchValue)
            print("\nFound Products:", foundProducts)
        
        if searchDesc == "ID":
            searchValue = int(input("Enter the search value for the chosen descriptor: "))
            foundProducts = searchProduct(product_data, searchDesc, searchValue)
            print("\nFound Products:", foundProducts)
        
        if searchDesc == "Price":
            searchValue = float(input("Enter the search value for the chosen descriptor: "))
            foundProducts = searchProduct(product_data, searchDesc, searchValue)
            print("\nFound Products:", foundProducts)

    elif choice == '5':
        sortedProductData = list(product_data.values())

        startTime = time.time()
        bubbleSortProduct(sortedProductData, key='Price', reverse=False)
        endTime = time.time()
        
        print(f"\nSorting time for Bubble Sort: {endTime - startTime:.6f} seconds")
        print(f"Sorted Product Data by Price (ascending order):")
        for product in sortedProductData:
            print(f"ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}, Category: {product['Category']}")
                
        startTime = time.time()
        bubbleSortProduct(sortedProductData, key='Price', reverse=True)
        endTime = time.time()

        print(f"\nSorting time for Bubble Sort (Reverse): {endTime - startTime:.6f} seconds")
        print(f"Sorted Product Data by Price (reverse order):")
        for product in sortedProductData:
            print(f"ID: {product['ID']}, Name: {product['Name']}, Price: {product['Price']}, Category: {product['Category']}")

    elif choice == '6':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Enter a number between 1 and 6.")

