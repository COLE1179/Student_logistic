import pandas as pd
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
st.header('Students Performance App Created By Cole')
st.subheader('Logistic Regression Project')

dg = pd.read_csv(r"C:\Users\HP\Documents\NEW COLE\student-mat.csv", delimiter=';')
st.dataframe(dg)

df = dg[['school', 'sex', 'Walc', 'absences', 'failures']].dropna()

encoder = LabelEncoder()
df['sex'] = encoder.fit_transform(df['sex'])
df['school'] = encoder.fit_transform(df['school'])

x = df[['school', 'sex', 'Walc', 'absences']]
y = df[['failures']]

#20% of the dataset is for testing and 70% of the dataset is for training
feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression()
model.fit(feature_train, target_train)

#student portal features which will be written on the sidebar
st.sidebar.title('Performance Features')
school =st.sidebar.selectbox('School', ['GP', 'MS'])
sex = st.sidebar.selectbox('Gender', ['Male', 'Female'])
Walc = st.sidebar.slider('Alcohol_rate', min_value=0, max_value=5)
absences = st.sidebar.slider('absences', min_value=0, max_value=60)

if sex == 'Male':
    sex = 1
else:
    sex = 0

if school == 'GP':
    school = 1
else:
    school = 0

total = {
         'school': [school],
         'sex': [sex],
         'Walc': [Walc],
         'absences': [absences]}

#print(total)
st.write('Performance Details')
st.dataframe(total, width=700)
pf = pd.DataFrame(total)

st.write('1 - means failure')
st.write('0 - means pass')


if st.button('Check Prediction'):
    prediction = model.predict(pf)
    #st.write('The possibility of failing is', prediction)
    st.write(f'The possibility value is: {prediction[0]}')


