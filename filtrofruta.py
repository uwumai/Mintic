import pandas as pd
Fruts=pd.DataFrame({"Producto":["Manzanas","Peras","Bananas","Naranjas"],
                    "Precio":[2.5,3,1.8,2.2],
                     "Cantidad":[100,150,200,80],
                      "Mes":["Enero","Enero","Febrero","Febrero"] }) 

print(Fruts[Fruts["Mes"]=="Enero"])
print("▬"*100)
print(Fruts)
print("▬"*100)
print(Fruts.loc[:,["Producto","Cantidad"]])
print("▬"*100)
Fruts["Precio"]=Fruts["Precio"]*1.10
print(Fruts)
print("▬"*100)
Fruts["Ingresos"] = Fruts["Precio"] * Fruts["Cantidad"]
print(Fruts)