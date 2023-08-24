def my_function(x,y,z):
    y.extend(z)
    for i in range(0,len(y)):
        for q in range(i+1,len(y)):
            if y[i] + y[q] == x:
                print(True)
                break
            if i==len(y)-1:
                print(False)
my_function(10,[2,6,7,15],[2,5,-5])