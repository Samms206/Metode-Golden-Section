# Min X^3 + 2X^2 + 6
# -1 <= X <= 2
# p = 0.382

#MIN X^2 + 3X^2 + 8
#-2 <= X <= 1
#p = 0.138

#diketahui
E = 0.01
#X^3
Xa = 1
XSa = 3
#2X^2
Xb = 2
XSb = 2
#6
Xc = 6

a = -1
b = 2
p = 0.382

#l
l = b - a

#X1
x1 = a + p*l
x1 = round(x1, 3)

#X2
x2 = a + (1 - p)*l
x2 = round(x2, 3)


#Perulangan
i = 1
for i in range(1,6):
    #penyelesaian
    #F(X1)
    fx1 = Xa*(x1)**XSa + Xb*(x1)**XSb + Xc
    fx1 = round(fx1, 3)
    #F(X2)
    fx2 = Xa*(x2)**XSa + Xb*(x2)**XSb + Xc
    fx2 = round(fx2, 3)
    print("f(x1) :", fx1, "| f(x2) :", fx2)
    #Penkondisian f(x1) < f(x2)
    if fx1 < fx2:
        print("Iterasi ke-", i, "f(x1) < f(x2)")
        b = x2
        print("b =", b)
        x2 = x1
        print("x2 =", x2)
        x1 = a + p * (b - a)
        x1 = round(x1, 3)
        print("x1 =", x1)
        result = b - a
        print("result =", round(result, 3))
        if result > E:
            print("")
        elif result < E:
            print("Stop")
            resultX = (a + b)/2
            break
        else:
            print("sudah memenuhi!")     
            break
        
    #Penkondisian f(x1) > f(x2)
    elif fx1 > fx2:
        print("Iterasi ke-", i, "f(x1) > f(x2)")
        a = x1
        print("a =", round(a, 3))
        x1 = x2
        print("x1 =", x1)
        x2 = a + (1 - p) * (b - a)
        print("x2 =", round(x2, 3))
        result = b - a
        print("result =", round(result, 3))
        if result > E:
            print("")
        elif result < E:
            print("Stop")
            resultX = (a + b)/2
            break
        else:
            print("sudah memenuhi!")   
            break
        
    #Penkondisian f(x1) = f(x2)
    elif fx1 == fx2:
        print("Iterasi ke-", i, "f(x1) = f(x2)")
        b = x2
        a = x1
        x1 = a + p * l
        x2 = a + (1 - p) * l
        result = b - a
        if result > E:
            print(round(""))
        elif result < E:
            print("Stop")
            resultX = (a + b)/2
            break
        else:
            print("sudah memenuhi!")   
            break
    else:
        print("Tidak dikethui")
    