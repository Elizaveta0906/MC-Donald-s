import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('Menu.csv')
df.info()

print(df['Category'].value_counts())
#Каллорий в завтраках больше, чем в десертах
calories = df.groupby(by = 'Category')['Calories'].mean()
cal_break = calories['Breakfast']
cal_dessert = calories['Desserts']

print('Калорий в завтраках', round(calories['Breakfast'], 2))
print('Калорий в десертах', round(calories['Desserts'], 2))

s = pd.Series(data=[cal_break, cal_dessert], index = ['Завтраки', 'Десерты'])
s.plot(kind = 'bar')
plt.show()

#В рыбе протеина больше, чем в салатах
protein = df.groupby(by = 'Category')['Protein'].mean()
prt_fish = protein['Chicken & Fish']
prt_sld = protein['Salads']

print('Протеина в рыбе', round(protein['Chicken & Fish'], 2))
print('Протеина в салатах', round(protein['Salads'], 2))

n = pd.Series(data=[prt_fish, prt_sld], index = ['Рыба', 'Салаты'])
n.plot(kind = 'bar')
plt.show()

sugars = df.groupby(by = 'Category')['Sugars'].mean()
sugars.plot(kind = 'barh')
plt.show()