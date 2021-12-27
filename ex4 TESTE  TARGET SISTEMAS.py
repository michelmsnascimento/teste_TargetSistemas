"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
"""


SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

total_mensal = SP+RJ+MG+ES+Outros
print("Total Mensal = R$ ",total_mensal)

percSp = (SP*100)/total_mensal
percRj = (RJ*100)/total_mensal
percMg = (MG*100)/total_mensal
percEs = (ES*100)/total_mensal
percOutros = (Outros*100)/total_mensal

print("SP = ",round(percSp, 2),"%\n","RJ = ",round(percRj, 2),"%\n","Mg = ",round(percMg, 2)
      ,"%\n","Es = ",round(percEs, 2),"%\n","Outros = ",round(percOutros, 2),"%\n",)
