Num = int(input('Enter Your Loop: '))
Numtotal = []
for i in range(Num):
    num = int(input('Enter Your Number:'))
    Numtotal  += [num]
print(Numtotal)
print(min(Numtotal))
print(max(Numtotal))
