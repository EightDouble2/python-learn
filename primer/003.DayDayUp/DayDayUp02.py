dayFactor = 0.005
dayUp = pow(1 + dayFactor, 365)
dayDown = pow(1 - dayFactor, 365)
print("向上：{:.2f}，向下：{:.2f}".format(dayUp, dayDown))
