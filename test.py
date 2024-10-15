import joblib

model = joblib.load('model.pkl')

Pregnancies = int(input('Pregnancies : '))
Glucose = int(input('Glucose : '))
BloodPressure = int(input('Blood Pressure : '))
SkinThickness = int(input('Skin Thickness : '))
Insulin = int(input('Insulin : '))
BMI = int(input('BMI : '))
DiabetesPedigreeFunction = int(input('Diabetes Pedigree Function : '))
Age = int(input('Age : '))

# result = model.predict([[6, 148, 72, 35, 0, 33.6, 0.627, 50]])
result = model.predict([[
    Pregnancies,
    Glucose,
    BloodPressure,
    SkinThickness,
    Insulin,
    BMI,
    DiabetesPedigreeFunction,
    Age
]])

print(result)