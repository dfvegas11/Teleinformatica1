#IMPORTACIÓN DE LAS LIBRERIAS QUE SE UTILIZARÁN
import warnings
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#LECTURA DEL ARCHIVO Y ESTABLECIMIENTO DE LAS VARIABLES OBJETIVO E INDEPENDIENTES
ventas = pd.read_csv("ventas2.csv")
objetivo = "monto"
independientes = ventas.drop(columns=['monto']).columns

#CREACIÓN DEL MODELO Y AJUSTE
modelo = LinearRegression()
warnings.filterwarnings("ignore")
modelo.fit(X=ventas[independientes], y=ventas[objetivo])

#CREACIÓN DE UN CONJUNTO CON LOS DATOS REALES Y LOS DE LA PREDICCIÓN
ventas["ventas_prediccion"] = modelo.predict(ventas[independientes])
preds = ventas[["monto", "ventas_prediccion"]].head(50)

#BUCLE PARA REALIZAR VARIAS PREDICCIONES
opc='Si'
while opc!='No':
    edad = int(input('Ingrese la edad: '))
    acomp = int(input('Numero de acompañantes: '))
    vehiculo = int(input('¿Tiene vehículo propio? (0/1): '))
    pago = int(input('Tipo de pago (efectivo=1;tarjeta=2;debito=3;vales=4): '))
    talvez = modelo.predict([[edad,acomp,vehiculo,pago]]) #PREDICCIÓN
    print ('---RESULTADO DE LA PREDICCIÓN---')
    print ("Tal vez compre: ")
    print ("$","{:.2f}".format(float(talvez)))
    opc = input('¿Desea realizar otra predicción? ')

#GRAFICACIÓN TENIENDO EN CUENTA LOS VALORES DEL CSV
preds.plot(kind='bar',figsize=(18,8))
plt.show()


