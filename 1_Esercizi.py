#Non serve più adessso funziona anche il file Jupyter
import numpy as np

#1)
lista1 = [1, 2, 3, 4]
lista2 = [2, 3, 4, 5]
lista_in_comune = []
for item in lista1:
    if item in lista2:
        lista_in_comune.append(item)
lista_in_comune

lista_in_comune2 = [item for item in lista1 if item in lista2]
lista_in_comune2

#2)
lista3 = []
for i in range(0,11):
    if i % 3 == 0:
        i = i*i
        lista3.append(i)
lista3

lista3_2 = [i*i for i in range(0,11) if i%3==0]
lista3_2

#3)
lista_result = []

for char in "Test stringa":
    if char == "s":
        lista_result.append(char)
lista_result

lista_result2 = [char for char in "Test stringa" if char == "s"]
lista_result2

arr_primi = np.array([1, 2, 3, 5, 7])
lunghezza = len(arr_primi)
print(arr_primi)
print(len(arr_primi))
#Credo che il dtype del vettore sia int
arr_primi.dtype
print(arr_primi.dtype)
#è int64

arr_primi2 = np.array([i for i in range (0,11) if i ==1 | i ==2 | i == 3 | i ==5 | i == 7])
print(arr_primi2)

a = np.array([1, 2, 3])
b = np.array([char for char in "Test stringa" if char != "a"])
c = a[::-1]

d = a/c
print(d)

a_2 = [1, 2, 3]
b_2 = [char for char in "Test stringa" if char != "a"]
c_2 = a_2[::-1]

#d_2 = a_2/c_2 Non si può fare