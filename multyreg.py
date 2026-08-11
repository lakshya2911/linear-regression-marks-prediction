###########multiple regression
import pandas as pd
from sklearn.linear_model import LinearRegression
df=pd.read_csv("cars.csv")
x=df[["age","km","engine","horsepower"]]
y=df["price"]
model=LinearRegression()
model.fit(x,y)
prediction=model.predict([[12,50000, 1500, 100]])
print("the predicted price is==",prediction[0], "lakhs")
