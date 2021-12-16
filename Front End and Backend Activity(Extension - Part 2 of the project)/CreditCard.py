import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('creditcard.csv')
data = data.sample(frac=0.1,random_state=1)
fraud=data[data['Class']==1]
valid=data[data['Class']==0]
outlier_fraction = len(fraud)/float(len(valid))
print(outlier_fraction)
print('Fraud Cases:{}'.format(len(fraud)))
print('Valid Cases:{}'.format(len(valid)))
corrmat = data.corr()
fig=plt.figure(figsize=(12,9))
sns.heatmap(corrmat,vmax=0.8 ,square=True)
columns = data.columns.tolist()
columns = [c for c in columns if c not in ["Class"]]
target = 'Class'
X=data[columns]
Y=data[target]
print(X.shape)
print(Y.shape)

from sklearn.metrics import classification_report , accuracy_score
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
state = 1
classifiers ={
    "Isolation Forest" : IsolationForest(max_samples=len(X),
    contamination= outlier_fraction,
    random_state= state),

    "Local Outlier Factor": LocalOutlierFactor(n_neighbors=20, contamination=outlier_fraction,novelty=True)

}
import pickle
model_file = 'Credit_Fraud_Detection.pkl'
n_outliers = len(fraud)

for i,(clf_name,clf) in enumerate(classifiers.items()):
    clf.fit(X)
    with open(model_file, 'wb') as file:
        pickle.dump(clf,file)
    s= clf.decision_function(X)
    y_pred = clf.predict(X)

print(len(y_pred))
print(np.array(y_pred))