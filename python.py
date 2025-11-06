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
        print(index, ":", item["name"], item["price"], item["description"])

def shop():
    cart = []
    print(input["what would you like to buy? type the number of what you want to buy. "])
    if input == (item["name"]):
       cart.append(item)
    print("thank you for your purchase!")
shop()