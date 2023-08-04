gas = "(2186 - 1994) * (3 / 5) * 6"
gas_price = round(eval(gas), 2)
print("燃气费(共3+2=5人):%s = " % gas, gas_price)

water = "(644 - 283) * (2 / 5) * 8"
water_price = round(eval(water), 2)
print("水费(共2+3=5人):%s = " % water, water_price)

print("剩余电费:195")

print("清洁费:100")

price_ = gas_price + water_price - 195 + 100
print(f"总和{gas_price} + {water_price} - 195 + 100=", price_)

print(f"房东应退   2800 - {price_}=", 2800 - price_)

a = 3
b = 2

a = 2
b = 1
c = 1
d = 1