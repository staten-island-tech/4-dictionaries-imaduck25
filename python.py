shopwrong_items = [
    {
        "name": "pain au chocolat",
        "price": 6.75,
        "description": "chocolate creme filled pastry"
    },
    {
        "name": "tiramisu",
        "price": 9.95,
        "description": "coffee soaked biscuits layered with coffee flavored creme and topped with coffee powder"
    },
    {
        "name": "macaroon",
        "price": 7.55,
        "description": "a delicate meringue-based cookie sandwich filled with a ganache, buttercream, or jam"
    }
]
for index, item in enumerate(shopwrong_items):
    print(index, ":", item["name"])
    print(index, ":", item["price"])
    print(index, ":", item["description"])

def store():
    cart = []
    print(input("what would you like to buy? "))
    if input == ["pain au chocolat", "tiramisu", "macroon"]:
        cart.append(shopwrong_items)
    print("thank you for your purchase! your purchase:")
    for shopwrong_items in cart:
        print(cart)
"""     print(input("do you wish to continue? (yes/no)"))
    if input == "no":
        print("ty for shopping here")
    if input == "yes":
        print(store) """
store()