stock=[
    ["Laptop", 50000, 5],
    ["Mobile", 20000, 10],
    ["Headphones", 2000, 15],
    ["Mouse", 500, 20]
]
cart=[]
def view_stock():
    print("\nAvailable Stock")
    for item in stock:
        print(f"{item[0]} - ₹{item[1]} - Stock:{item[2]}")
def add_product(product, quantity):
    for item in stock:
        if item[0].lower() == product.lower():
            if item[2] >= quantity:
                cart.append([item[0], item[1], quantity])
                item[2] -= quantity
                print(f"{product} is added to cart")
            else:
                print("Insufficient Stock")
            break
    else:
        print("Product not found in stock")
def view_cart(cart):
    if len(cart)==0:
        print("Cart is empty")
    else:
        total=0
        print("\nProducts in Cart")
        for item in cart:
            sub=item[1]*item[2]
            total+=sub
            print(f"{item[0]} - ₹{item[1]}- Quantity: {item[2]}")
        print(f"Total Bill:₹{total}\n")
def remove_product(product, remove_quantity):
    for item in cart:
        if item[0].lower() == product.lower():
            for s in stock:
                if s[0].lower() == product.lower():
                    if remove_quantity >= item[2]:
                        s[2] += item[2]
                        cart.remove(item)
                        print(f"{product} is removed from cart")
                    else:
                        item[2] -= remove_quantity
                        s[2] += remove_quantity
                        print(f"{remove_quantity} {product} removed from cart")
                    break
            break
    else:
        print("Product not found")
def search_product(product):
    for item in cart:
        if item[0].lower()==product.lower():
            print(f"Product:{item[0]}")
            print(f"Price:₹{item[1]}")
            print(f"Qunatity:{item[2]}")
            break
    else:
        print("Product not found")
def clear_cart(cart):
    cart.clear()
    print("Cart Cleared")
def total_bill(cart):
    total = 0
    for item in cart:
        total += item[1] * item[2]
    print(f"Total Bill: ₹{total}")
if __name__=="__main__":
    while True:
        print("----SHOPPING CART SYSTEM----")
        print(" 1.View Stock\n 2.Add Product to Cart\n 3.Remove Product from Cart\n 4.View Cart\n 5.Search Product in Cart\n 6.Clear Cart\n 7.View total bill\n 8.Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            view_stock()
        elif choice==2:
            product=input("Enter product name:")
            quantity=int(input("Enter quantity:"))
            add_product(product,quantity)
        elif choice==3:
            product = input("Enter product name to remove:")
            remove_quantity=int(input("Enter quantity to remove:"))
            remove_product(product,remove_quantity)
        elif choice ==4:
            view_cart(cart)
        elif choice==5:
            product=input("Enter product name:")
            search_product(product)
        elif choice==6:
            clear_cart(cart)
        elif choice==7:
            total_bill(cart)
        elif choice==8:
            exit(0)
        else:
            print("Select your choice in between 1-8")
        