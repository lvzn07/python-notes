money = input("输入货币")
if money[0] in ['U']:
    RMB = (eval(money[3:])*6.78)
    print("输入货币RMB{:.2f}".format(RMB))
elif money[0] in ['R']:
    USD = (eval(money[3:])/6.78)
    print("输入货币USD{:.2f}".format(USD))