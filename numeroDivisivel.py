num = int(input("Escolha um numero"))
primo = 0
count = 0
for i in range (1, num+1):
    if num%i == 0:
        print(i)
        count+=1
    else:
        primo += 1
if primo == num-2:
    print("É um numero primo")
print(f"Foi divisivel {count} vezes")

