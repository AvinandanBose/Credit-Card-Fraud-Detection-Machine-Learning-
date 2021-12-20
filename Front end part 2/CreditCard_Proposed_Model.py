import pandas as pd
df = pd.read_csv('creditcard.csv')
f_df = df[df['Class']==1]
n_df = df[df['Class']==0]

from sklearn.preprocessing import RobustScaler
rob_scaler = RobustScaler()
df['robust_amount'] = rob_scaler.fit_transform(df['Amount'].values.reshape(-1,1))
df['robust_time'] = rob_scaler.fit_transform(df['Time'].values.reshape(-1,1))


from sklearn.model_selection import StratifiedKFold
import numpy as np
X = df.drop('Class', axis=1)
y = df['Class']
skf = StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
train_unique_label, train_counts_label = np.unique(y_train, return_counts=True)
test_unique_label, test_counts_label = np.unique(y_test, return_counts=True)

train_df = X_train.copy()
train_df['Class'] = y_train


from imblearn.over_sampling import SMOTE
sm = SMOTE()
X_sm, y_sm = sm.fit_resample(X_train, y_train)
train_df_sm = X_sm
train_df_sm['Class'] = y_sm

col_set1=['Time','V1','V2','V3','V4','V5','V6','V7','V8','V9','V10',
'V11','V12','V13','V14','V15','V16','V17','V18','V19','V20','V21','V22','V23','V24','V25','V26','V27','V28',
'Amount']

X_train_smote_robust = train_df_sm[col_set1]
y_train_smote_robust = train_df_sm["Class"]


from sklearn.linear_model import LogisticRegression
classifiers = {
    "LogisticRegression":LogisticRegression(C=1.0,class_weight=None,dual=False,
    fit_intercept=True,intercept_scaling=1,l1_ratio=None,max_iter=1000 ,multi_class='auto',n_jobs=None,
    penalty='l2', random_state=None,solver='lbfgs',tol=0.0001,verbose=0, warm_start=False)   
}

LR_SMOTE_Robust = LogisticRegression(C=1.0,class_weight=None,dual=False,
    fit_intercept=True,intercept_scaling=1 ,l1_ratio=None,max_iter=1000 ,multi_class='auto',n_jobs=None,
    penalty='l2', random_state=None,solver='lbfgs',tol=0.0001,verbose=0, warm_start=False)

LR_PARAM = LR_SMOTE_Robust.fit(X_train_smote_robust,y_train_smote_robust)

import pickle
# Saving model to disk
pickle.dump(LR_PARAM, open('my_model.pkl','wb'))

model=pickle.load(open('my_model.pkl','rb'))

