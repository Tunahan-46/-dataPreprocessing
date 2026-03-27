import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

df.fillna(df['Gelir'].mean(),inplace=True)

#yaş ve meslek degerlerini 0 1 ... degişkenlerine çevirdik
le=LabelEncoder()

df['Cinsiyet']=le.fit_transform(df['Cinsiyet'])
df['Meslek']=le.fit_transform(df['Meslek'])


#verilerimiz hazır modeli kuruyorum
X=df[['Yaş','Meslek']]
y=df['Gelir']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

lineer_model=LinearRegression()
lineer_model.fit(X_train,y_train)


#girdi alıp test ededelim
yas=int(input('Yas Giriniz: '))
meslek=(input('Mesleginizi Giriniz : '))

#girilen meslek bilgisini label_Encoding yapalım

meslek_kodu=le.transform([meslek])[0]

yeni_veri=pd.DataFrame([[yas,meslek_kodu]], columns=['Yaş','Meslek'])


tahmini_gelir=lineer_model.predict(yeni_veri)
print(f"girilen verilere göre tahmini gelir : {tahmini_gelir[0]:.2f}")




