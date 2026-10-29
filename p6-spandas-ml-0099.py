import pandas as pd
import numpy as np
# Anais Medina NC 0099 fecha 28 octubre 2026
serie_amigos = ["Anais", "Alexia", "Jazmin", "Astrid", "Eiza", "Aliah", "Sebastian"]
print("---- Serie listado de amigo   NC 0099 ----")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20,50,100,200,500,1000]
print("---- Serie listado de billetes MX  NC 0099 ----")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes = [20,50,100,200,500,1000]
serie_bletras=["veinte","cincuenta","cien","doscientos","quinientos","mil"]
print("---- Serie listado nombres y valor de billetes MX  NC 0099 ----")
tablabilletes=pd.Series(serie_billetes,serie_bletras)
print(tablabilletes)

# diccionario dataframe 
# diccionario de valor monedas y nombre
print("datos de diccionario a DataFrame en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["veinte","cincuenta","cien","doscientos","quinientos","mil"]
} 

tablabilletes=pd.DataFrame(dic_monedas, index=["A","B","C","D","E","F"])
print(tablabilletes)
print("Casa de cambio de Anais MEWdina NC 0099")
print("Anais Medina NC 0099")