primes = list(range(2, 101))
print(primes)
for i in range(1, 101):
    for j in range(2, i-1):
        if i%j == 0:
            primes.remove(i)
            break

print(primes)