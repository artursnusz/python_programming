import random as rd

random = rd.randint(1, 50)
gramy = "tak"

podane = []
wylosowane = []
# ewwew
# rwwrwwrwtwwt
# eteteteyeyeyy
# while gramy == "tak":
for i in range(6):
    podane.append(int(input("Podaj liczbę numer " + str(i + 1) + ": ")))
    while random not in wylosowane:
        wylosowane.append(random)
    while random in wylosowane:
        random = rd.randint(1, 50)
trafione = 0
for z in podane:
    for j in wylosowane:
        if z == j:
            trafione = trafione + 1

print("Twój wynik to: " + str(trafione))
print("Wylosowane liczby:")
print("Wylosowane liczby:")
#etetet
#rwrwrwrrrw
for i in wylosowane:
    print(i)
podane.clear()
wylosowane.clear()
gramy = input("Czy chcesz zagrać jeszcze raz? (tak/nie) ")
