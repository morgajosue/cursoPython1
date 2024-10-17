blocks = int(input("Ingresa el número de bloques: "))
minus = 1
height = 0

while(blocks >= minus):
  blocks -= minus
  minus += 1
  height += 1

print("La altura de la pirámide:", height)
