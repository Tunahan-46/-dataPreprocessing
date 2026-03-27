import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df=pd.read_excel('veri_on_isleme_ve_ozellik_muhendisligi.xlsx')

#boş olan gelir degerlerini ortalamaya göre dolduruyorum
df.fillna(df['Gelir'].mean(),inplace=True)

#Cinsiyet ve Meslek verileeri için tranform işlemi
le=LabelEncoder()
df['Cinsiyet']=le.fit_transform(df['Cinsiyet'])
df['Meslek']=le.fit_transform(df['Meslek'])


X=df[['Yaş','Meslek','Cinsiyet']]
y=df['Gelir']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)



lineer_model=LinearRegression()
lineer_model.fit(X_train,y_train)

lineer_accuracy=lineer_model.score(X_test,y_test)
print(f"lineer modelin dogruluk oranı : %{lineer_accuracy*100:.2f}")

#daha iyi sonuç için RandomForest kullanıcaz

rf_model=RandomForestRegressor(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)
rf_accuracy=rf_model.score(X_test,y_test)
print(f"Random forest modelin dogruluk oranı : %{rf_accuracy*100:.2f}")

#kullanıcıdan veri alalım
yas=int(input('Lütfen yaşınızı giriniz : '))
girilen_meslek=input('Mesleginizi giriniz: ')
girilen_cinsiyet=input('Cinsiyetinizi giriniz: ')

meslek_kod=le.transform([[girilen_meslek]])[0]
cinsiyet_kod=le.transform([[girilen_cinsiyet]])[0]
yeni_veri=pd.DataFrame([[yas,girilen_cinsiyet,girilen_meslek]],columns=['Yaş','Cinsiyet','Meslek'])
yeni_veri_scaled=scaler.transform(yeni_veri)
tahmin=rf_model.predict(yeni_veri_scaled)
print(tahmin)