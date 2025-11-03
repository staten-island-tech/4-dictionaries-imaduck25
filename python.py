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
        "description": "a delicate meringue-based cookie sandwich filled with a ganache, buttercream or jam"
    }
]
print(shopwrong_items[0]["name"])
print(shopwrong_items[0]["price"])
print(shopwrong_items[1]["name"])
print(shopwrong_items[1]["price"])
print(shopwrong_items[2]["name"])
print(shopwrong_items[2]["price"])

def store():
    cart = []
    print(input("what would you like to buy? "))
    if input == ["pain au chocolat", "tiramisu", "macroon"]:
        cart.append(shopwrong_items)
    print(shopwrong_items["price"])
"""     print(input("do you wish to continue? (yes/no)"))
    if input == "no":
        print("ty for shopping here")
    if input == "yes":
        print(store) """
store()