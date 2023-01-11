def prime_factors(n):
    factors = []
    # Sieb des Eratosthenes zum Erstellen einer Liste von Primzahlen bis zu n
    primes = sieve_of_eratosthenes(n)
    # Durchlaufe die Primzahlen
    for prime in primes:
        # Wenn der Faktor der Zahl teilbar ist, füge es zur Faktorliste hinzu
        while n % prime == 0:
            factors.append(prime)
            n = n // prime
    return factors

def sieve_of_eratosthenes(n):
    # Erstelle eine Liste von True-Werten bis zu n
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    # Markiere alle nicht-primzahlen als False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i ** 2, n + 1, i):
                primes[j] = False
    return [i for i in range(len(primes)) if primes[i]]

# Beispielaufruf
number = 60
print(f"Primfaktorzerlegung von {number} : {prime_factors(number)}")
input ("Belibige Taste drücken.")