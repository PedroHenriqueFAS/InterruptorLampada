n = int(input())
l1=False
l2 = False
lista=[]
for i in range(n):
    a =  int(input())
    lista.append(a)

for el  in lista:
    if el ==1:
        if l1:
            l1 = False
        else:
            l1 = True
    if el ==2:
        if l1:
            l1 = False
        else:
            l1 = True
        if l2:
            l2 = False
        else:
            l2 = True
            
print(int(l1))
print(int(l2))