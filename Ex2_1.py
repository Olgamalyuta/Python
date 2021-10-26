#номер 4
spisok=[]
n=int(input("Please input quantity of numbers in array "))
for i in range (n):
    spisok.append(int(input()))

x=1
for i in range(n):
    if(i%2)!=0:
        x*=spisok[i]
print("Произведение элементов списка с нечетным индексом " + str(x))

max=max(spisok)
print("Наибольший элемент списка "+str(max) )

spisok.remove(max)
print(spisok)

