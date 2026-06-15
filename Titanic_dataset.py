import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report
import joblib
df=pd.read_csv("train.csv")
print(df.head())
print(df.info())
#print(df.isnull())
#print(df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].median())

df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])
df=df.drop("Cabin",axis=1)
#print(df.isnull().sum())
df["Sex"]=df["Sex"].map({"male":0, "female":1
})
df["Embarked"]=df["Embarked"].map({"S":0,"C":1,"Q":2
})
print(df.head())
print(df.info())

X = df[["Pclass", "Sex", "Age", "Fare", "Embarked"]]
y=df["Survived"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


model=LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

#pclass = int(input("Enter Pclass (1/2/3): "))
#sex = input("Enter Sex (male/female): ")
#age = float(input("Enter Age: "))
#fare = float(input("Enter Fare: "))
#embarked = input("Enter Embarked (S/C/Q): ")


#sex = 0 if sex == "male" else 1
#embarked = {"S":0, "C":1, "Q":2}[embarked]


#new_data = pd.DataFrame([[pclass, sex, age, fare, embarked]],
 #                       columns=["Pclass","Sex","Age","Fare","Embarked"])

#predications=model.predict(new_data)
#predications=model.predict(X_test)
#print("Accuracy:", accuracy_score(y_test, predications))
#new_passenger=np.array([[3,1,22,7.25,0]])
#prediction=model.predict(new_passenger)
#if predications[0]==1:
   # print("Survived")
#else:
   # print("Not Survived")

#print(confusion_matrix(y_test,predications))
#print(classification_report(y_test,predications))
joblib.dump(model,"titanic_model.pkl")
print("model  trained and saved ")