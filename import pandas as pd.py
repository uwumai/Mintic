import pandas as pd
Datos = {
    'Nombre': ['Ana', 'Carlos', 'María', 'Juan', None, 'Laura', 'Pedro', 'Sofía', 'Miguel', 'Elena'],
    'Edad': [25, 32, None, 45, 29, 31, None, 28, 35, 27],
    'Ciudad': ['Bogotá', 'Medellín', None, 'Cali', 'Villavicencio', None, 'Barranquilla', 'Cali', 'Bogotá', None],
    'Departamento': ['Ventas', None, 'IT', 'Ventas', 'RH', 'IT', None, 'Marketing', 'IT', 'Marketing'],
    'Fecha_Contratacion': pd.to_datetime(['15-01-2020', '20-05-2018', None, '10-11-2015', '05-03-2019', 
                                        '15-07-2021', '01-12-2017', None, '20-08-2016', '28-02-2022']),
    'Salario': [30000, 45000, 38000, None, 52000, 41000, 36000, None, 48000, 43000]
}

df = pd.DataFrame(Datos)
print("Identificar valores nulos")
print(df.info())
print("="*100)
print("cantidad de nulos en cada column:")
print(df.isnull().sum())
print("="*100)
print("Elimina los valores nulos:")
print(df.dropna())
print(df.dropna(how="all", inplace=True))
print("▬"*100)
print("Reemplazar valores nulos con valor promedo:")
df["Salario"]=df["Salario"].fillna(df["Edad"].mean())
print(df[["Nombre","Edad"]].head())
print("Reemplazr valores nulos con valor de la mediana")
Mediana= df["Edad"]=df["Edad"].fillna(df["Edad"].median())
print(Mediana)
print("▬"*100)

print("Remplazar valores nulos con valor de la mode:")
df["Salario"]=df["Salario"].fillna(df["Salario"].mode())
print(df[["Nombre","Salario"]].head())
print("▬"*100)





print("▬"*100)
df["Edad"]=df["Edad"].interpolate
print(df)

