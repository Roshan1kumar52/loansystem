import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators = 7, 
                             criterion = 'entropy', 
                             random_state =7)
data = pd.read_csv('D:\loans\loanssystem\machinlearning\LoanApprovalPrediction.csv')


newdata=data.drop('Loan_ID',axis='columns')
#print(newdata.head())
X=newdata.drop('Loan_Status',axis='columns')
Y=data["Loan_Status"]
#print(X.shape,Y.shape)
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=42)

model.fit(X_train,Y_train)
Y_pred = model.predict(X_train)
print(Y_pred) 