#NUMEROS PRIMOS

# Solicitud de datos
limite = int(input('>>> Dame un mumero: '))
 
for numero in range(1, limite + 1):
    creo_que_es_primo = True
    for divisor in range(2,numero):
        if numero % divisor == 0:
            creo_que_es_primo = False
            break
 
    if creo_que_es_primo:
            print(numero)




def criba_eratostenes(n):
    primes = []
    candidates = list(range(2, n * 10))
    while len(primes) < n:
        p = candidates[0]
        primes.append(p)
        candidates = [x for x in candidates if x % p != 0]
    return primes
