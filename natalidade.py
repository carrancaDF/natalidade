pais = input("Você deseja calcular a natalidade de qual país? ")
nasc = float(input(f"Qual foi o número de nascidos vivos do último ano no {pais}? "))
# A do Brasil foi de 2619385
pop = float(input(f"Qual a população total do {pais} no último ano? "))
#A do Brasil foi de 213300000 em 2021.
nat = (nasc*1000/pop)
print (f"A taxa de natalidade do {pais} foi de {nat:.2f}.\nOu seja, a cada mil habitantes, nasceram {nat:.2f} bebês.")





