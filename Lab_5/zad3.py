def isPalindorm(x):
    return x == x[::-1]
slowo  = input("Podaj słowo")
if isPalindorm(slowo):
    print("Jest palindromem")
else:
    print("Nie jest palindromem")
print(slowo[::-1])