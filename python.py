shopwrong_items = [
    {
        "name": "Pain au Chocolat",
        "price": 6.75,
        "description": "chocolate creme filled pastry"
    },
    {
        "name": "Tiramisu",
        "price": 10.50,
        "description": "coffee soaked biscuits layered with coffee flavored creme and topped with coffee powder"
    },
    {
        "name": "Macaroon",
        "price": 7.55,
        "description": "a delicate meringue-based cookie sandwich filled with a ganache, buttercream, or jam"
    }
]
for index, item in enumerate(shopwrong_items):
    print("★ ", item["name"])
    print("Price: $", item["price"])
    print("Description:", item["description"])

def shop():
    cart = []
    total = 0.00
    print("★ Welcome to shopwrong!★")
    while True:
        print("What would you like to buy?")
        for item in shopwrong_items:
            print("★ ", item["name"])
        choice = input("Type the name of what you want to buy: ").lower()
        for item in shopwrong_items:
            if item["name"].lower() == choice:
                cart.append(item["name"])
                total += item["price"]
                print("★ ty for your purchase!★")
                break
        again = input("do u wish to continue? (yes/no): ").lower()
        if again != "yes":
            break
    print("your cart:")
    for item in cart:
        print("★ ", item)
    print("Total: $", round(total, 2))
shop()