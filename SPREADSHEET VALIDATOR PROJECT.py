import pandas as pd 
import numpy as np 


planilha_correta = []
contratos_faltantes = []

def comparador(x, y):
    for i in range(len(x)):
        for j in range(len(y)):
                if x[i][0] == y[j][0]:  
                    planilha_correta.append(x[i][0])
                    

#w será a planilha de placas_finalizadas
#q será a planilha de placas corretas

def confirmador(w,q):
    #definiria que a planilha q seria um set de placas corretas e posteriormente usaria o not in para verificar as faltantes 
    placas_corretas = set(q)
    for l in w:
        #não preciso explicitar a linha pois como o for é l in w e não l in len(w), o l já e dado como a própria linha, logo a cada loop, ela vai ser a próxima linha
        placa = l[0]
        if placa not in placas_corretas:
            contratos_faltantes.append(placa)

a = pd.read_excel(
    'placas_finalizadas.xlsx',
    usecols = 'A'
)

b = pd.read_excel(
    'placas (1).xlsx',
    usecols = 'A'
)
matriz = a.to_numpy()
matriz2 = b.to_numpy()
 
comparador(matriz,matriz2)
confirmador(matriz,planilha_correta)
print(len(planilha_correta))
print((contratos_faltantes))