import pandas as pd
Empleados=pd.DataFrame({
    "Id_Empleados":[101,102,103,104,105,106,107],
    "Nombre":["Luis Garcia","Ana Martinez","Sofia Lopez","Carlos Roa","Maria Diaz",
              "Pedro Ramirez", "Elena Jimenez"],
    "Edad":[28,30,64,56,26,32,45],
    "Departamento": ["Ventas","TI","RH","RH","Finanzas","Ventas","TI"],
    "Cargo":["Asistente","Analista","Gerente","Coordinador","Contador","Asesor","Analista"],
    "Fecha_Contratacion":['15-01-2020', '20-05-2018', '10-11-2015','20-08-2016',
                                        '15-07-2021', '01-12-2017','28-02-2022'],
    "Salario" :[30000, 45000, 88000,52000, 41000, 36000, 48000 ]                                 
   })
print(Empleados)
print("♥"*100)
print("Indexacion por nombres:")
print(Empleados["Nombre"])
print("♥")
print("Registro 2: ")
print(Empleados.iloc[1])
print("♥"*100)
print("Registro 1: ")
print(Empleados.iloc[0])
print("♥"*100)
print("Registro 1:")
print(Empleados.loc[:,["Nombre","Edad"]])
print("♥"*100)
print(Empleados[Empleados["Edad"]>=50])
print("♥"*100)
print("Imprime 3 registros:")
print(Empleados.iloc[0:2,0:3])
print("♥"*100)
print("Nueva columna de comisión:")
Empleados["Comision"]=Empleados["Salario"]*0.08
Empleados["Salario Total"]=Empleados["Salario"]+Empleados["Comision"]
Empleados.loc[Empleados["Salario"]<=35000,"Salario"]+=2500
print(Empleados)
print(Empleados[["Nombre","Salario","Comision","Salario Total"]])
print("♥"*100)
print("Empleados por cargo")
print(Empleados.loc[:,["Nombre","Cargo"]])
print("▬"*100)
Empleados["Perfil"]=Empleados["Departamento"]+"-"+Empleados["Cargo"]
print(Empleados)
print("▬"*100)
Empleados=Empleados.drop(columns=["Perfil"])
print(Empleados)
Empleados=Empleados.rename(columns={"Id_Empleados":"Id"})
print(Empleados)
