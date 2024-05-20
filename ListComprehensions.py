
x = int(input())
y = int(input())
z = int(input())
n = int(input())

a = [x for x in  range(x+1)]
b = [y for y in  range(y+1)]
c = [z for z in  range(z+1)]



permutacao = ([[i,j,k] for i in a for j in b for k in c])

resultado = [item for item in permutacao if sum(item) != n]

print(resultado)


