#METODO DE ORDENAMIENTO SELECTION SORT
Elemento=int(input("Ingrese el tamaño del vector : "))
vector=[]
for i in range(Elemento):
    itm=int(input(f"ingrese numero {i+1} : "))
    vector.append(itm)
print ("Vector original: ",vector)

for i in range(len(vector)):
    inicio=i
    for j in range(i+1,len(vector)):
        if vector[j]<vector[inicio]:
            inicio=j
    vector[i],vector[inicio]=vector[inicio],vector[i]

print("Vector ordenado: ",vector)