import os,csv,random,math


if not os.path.exists('number_file'):
    os.mkdir('number_file')
data_file = open('number_file/'+'number'+'.csv','w',encoding='UTF-8',newline='')
writer = csv.writer(data_file)
writer.writerow(["X","Y","WIDTH","distance","ID"])
X=[2,8.6,15.2]
Y=[2,6.5,11]
i = 1
while i <= 135:
    x = random.choice(X)
    y = random.choice(Y)
    w = random.randint(1,3)
    if i > 1:
        while x == x_pre and y == y_pre:
            x = random.choice(X)
            y = random.choice(Y)
        d = math.sqrt((x - x_pre)**2 + (y - y_pre )**2 )
        ID = math.log(2 * d/w, 2)
    else:
        d = 0
        ID = 0

    x_pre = x
    y_pre = y
    writer.writerow([x,y,w,d,ID])
    i += 1
