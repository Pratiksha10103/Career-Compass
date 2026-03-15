import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data=pd.read_csv("data/career_dataset.csv")

X=data.drop("career",axis=1)
y=data["career"]

model=DecisionTreeClassifier()
model.fit(X,y)

def predict_career(input_data):
    return model.predict([input_data])[0]
