import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 
from sklearn.metrics import mean_absolute_error, mean_squared_error

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
model=LinearRegression()
df=pd.read_csv("Salary_dataset.csv")
df.drop("Unnamed: 0",axis=1,inplace=True)
print(df.columns)
X=df.iloc[:,:-1]
y=df.iloc[:,-1]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)

prediction=model.predict([[5]])
print(prediction)
new_data=pd.DataFrame({"YearsExperience":[3,5,7]})
predictions= model.predict(new_data)
print(predictions)
y_pred=model.predict(X_test)
score=model.score(X_test,y_test)
print("R2 Score=",score)
mae=mean_absolute_error(y_test,y_pred)
print("MAE=",mae)
mse=mean_squared_error(y_test,y_pred)
print("MSE:",mse)
rmse=np.sqrt(mse)
print("RMSE:",rmse)





#plt.scatter(X,y)

#plt.plot(X,model.predict(X))
#plt.xlabel("Years Experience")
#plt.ylabel("Salary")
#plt.title("Salary Prediction")
#plt.show()
print("scope:", model.coef_)
print("intercept:", model.intercept_)

