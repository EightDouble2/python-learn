def day_up(df):
    dayUp = 1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayUp = dayUp * (1 - 0.01)
        else:
            dayUp = dayUp * (1 + df)
    return dayUp


dayFactor = 0.01
while day_up(dayFactor) < 37.78:
    dayFactor += 0.001
print("工作日的努力参数是：{:.3f} ".format(dayFactor))
