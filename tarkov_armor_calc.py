import pandas as pd
Durability = input('耐久値を入力\n')
Material = int(input('材質を入力\n1.Aramid 2.UHMWPE 3.Combined Materials\n4.Titan 5.Alminium 6.Steel\n7.Ceramic 8.Glass\n'))
Armor_Material = ['Aramid','UHMWPE','Combined Materials','Titan','Alminium','Steel','Ceramic','Glass']
Chosen_Material = Armor_Material[Material-1]
Destractibilities = [0.25,0.45,0.5,0.55,0.6,0.7,0.8,0.8]
Armor_Destractibility_Data = pd.DataFrame(list(zip(Armor_Material,Destractibilities)),columns=['Armor Material','Destractibility']).set_index('Armor Material')
Chosen_Destractibility = Armor_Destractibility_Data['Destractibility'][Chosen_Material]
Effective_durability = int(Durability) / float(Chosen_Destractibility)
print(Effective_durability)