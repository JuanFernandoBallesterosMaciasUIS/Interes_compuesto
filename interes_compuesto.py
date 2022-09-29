# Hacer el diagrama de flujo y el codigo en python, que lea un capital "c", y que averigue y imprima en cuantos meses se duplica, si lo colocamos a un interes compuesto de 5% mensual.

#input
c = int(input("Digita el capital inicial: "))

#process
i = 0
c1 = c

while c1 <= c*2:
    c1 = c1 + (c1 * 0.05)
    i = i + 1

#output
print("Para que se duplique",c,"con un interes compuesto de 5%, se necesita",i,"meses, y tendria un capital final de",c1)