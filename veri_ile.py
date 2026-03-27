import pandas as pd
from sklearn.preprocessing import LabelEncoder

df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

# print(df.head())
# print(df)
df.fillna(df['Gelir'].mean(),inplace=True)
# print(df)

le=LabelEncoder()
df['Cinsiyet']=le.fit_transform(df['Cinsiyet'])
# print(df)
df.drop('ID' ,axis=1,inplace=True)

df['Gelir_Grubu']=pd.cut(df['Gelir'], bins=[0,3000,5000,7000], labels=['Düşük','Orta','Yüksek'])
df.to_excel('Katagorik_Gelir.xlsx',index=False)