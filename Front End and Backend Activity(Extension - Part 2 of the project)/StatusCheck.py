#Check fraud transaction
import pandas as pd
data = pd.read_csv('creditcard.csv')
data = data.sample(frac=0.1,random_state=1)
fraud=data[data['Class']==1]
valid=data[data['Class']==0]
print(valid)
