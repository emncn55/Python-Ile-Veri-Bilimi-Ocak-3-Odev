print("Lütfen Bir Sayı Giriniz: ")
number = int(input())


# FOR Döngüsü
total_for = 0
for i in range(1 , number+1):
    total_for += i

print(f"Total: {total_for}")

# WHİLE Döngüsü
total_while = 0
j = 1
while j <= number:
    total_while += j
    j +=1

print(f"Total: {total_while}")
