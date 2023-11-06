"""
Aprēķināt noteiktas skaitļu summu no 1 līdz n, kur n ir lietotāja ievadīts skaitlis.
"""

n = int(input("Ievadi skaitli 'n': ")) #liek lietotājam ievadīt skaitli

summa = 0 

for skaitlis in range (1, n+1):
    summa += skaitlis

print (f"Skaitļu no 1 līdz {n} summa ir {summa}")