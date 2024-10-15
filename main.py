import math

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score

import pandas as pd
import numpy as np

##################### load dataset #####################

data = pd.read_csv('dataset/diabetes.csv')
# print(data.columns)
# print(data.head())

zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in zero_not_accepted:
    data[col] = data[col].replace(0, np.NaN)
    mean = int(data[col].mean(skipna=True))
    data[col] = data[col].replace(np.NaN, mean)

x = data.iloc[:, :8]
y = data.iloc[:, 8]

##################### split train and test #################

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

##################### feature scaling ######################

# print(x_train)

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.fit_transform(x_test)

# print(x_train)

##################### train model ######################

# print(len(y_test)) # 154
# print(math.sqrt(len(y_test))) # 12.409673645990857

model = KNeighborsClassifier(n_neighbors=11, p=2, metric='euclidean')

model.fit(x_train, y_train)

###################### test model ######################

y_pred = model.predict(x_test)

print(confusion_matrix(y_test, y_pred))
print(f1_score(y_test, y_pred))
print(accuracy_score(y_test, y_pred))

# import joblib
# joblib.dump(model, 'model.pkl')