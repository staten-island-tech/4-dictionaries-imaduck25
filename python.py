
item = {
    "name": "pain au chocolat",
    "price": 4.99,
    "description": "chocolate creme filled pastry"
}
print(item["name"])

item = {
    "name": "tiramisu",
    "price": 10.99,
    "description": "coffee soaked biscuits layered with coffee flavored creme and topped with coffee powder"
}
print(item["name"])

item = {
    "name": "macaroon",
    "price": 7.99,
    "description": "a delicate meringue-based cookie sandwich filled with a ganache, buttercream or jam"
}
print(item["name"])

cart = []
print(input("what would you like to buy? "))
if input == ["pain au chocolat", "tiramisu", "macroon"]:
    cart.append(item)
print((item["price"]))
print("thank you for your purchse")