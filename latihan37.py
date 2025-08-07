n = int(input("N = "))
fibo_a = 0
fibo_b = 1

for i in range(n):
    if i <= 1:
        print(i, end = " ")
    else:
        fibo_c = fibo_a + fibo_b
        print(fibo_c, end = " ")
        fibo_a = fibo_b
        fibo_b = fibo_c

print("")