"""
Izvadīt visus pirmsskaitļus no 1 līdz 100, izmantojot for un if. something

1) kas ir pirmskaitlis? - naturāls skaitlis kas > 1 un dalās ar sevi un 1
2) apgabals no 1 --> 100
3) pieraksti for un if
"""

def ir_pirmskaitlis(skaitlis):
    if skaitlis <2:
        return False
    for dalitajs in range (2, int(skaitlis**0.5)+1):
        if skaitlis% dalitajs ==0:
            return False
    return True
for skaitlis in range (1, 101):
    if ir_pirmskaitlis(skaitlis):
        print(skaitlis)