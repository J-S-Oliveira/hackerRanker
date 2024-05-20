n = int(input())
resto = n % 2

if resto != 0: # numero impar
    print("Weird")

else: # numero par
    if n in range(2,5,2):
        print("Not Weird")

    if n in range(6,21,2):
        print("Weird")
    
    if n > 20 :
        print("Not Weird")


