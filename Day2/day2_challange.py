name = input("Please enter your name: ")
sales_amount = input("Please enter the sales amount: ")
commission_rate = 0.13 # 13% commission rate

commission = float(sales_amount) * commission_rate
print(f"Hello, {name}. Your commission is ${round(commission,2)}.")