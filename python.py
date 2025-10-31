
item = {
    "name": "pain au chocolat",
    "price": 7.55,
    "description": "chocolate creme filled pastry"
}
print(item["name"])

item = {
    "name": "tiramisu",
    "price": 7.55,
    "description": "coffee soaked biscuits layered with coffee flavored creme and topped with coffee powder"
}
print(item["name"])

item = {
    "name": "macaroon",
    "price": 7.55,
    "description": "a delicate meringue-based cookie sandwich filled with a ganache, buttercream or jam"
}
print(item["name"])


def store():
    cart = []
    print(input("what would you like to buy? "))
    if input == ["pain au chocolat", "tiramisu", "macroon"]:
        cart.append(item)
    print(item["price"])
    print(input("do you wish to continue? (yes/no)"))
    if input == "no":
        print("ty for shopping here")
    if input == "yes":
        print(store)
store()