import streamlit as st
st.title('IRIS CLASSIFIER')
x1 = st.slider('Sepal length',4.0, 7.9, 0.5)
x2 = st.slider('Sepal width',2.0, 4.4, 0.5)
y1 = st.slider('Petal length',1.0, 6.9, 0.5)
y2 = st.slider('Petal width', 0.1,2.5, 0.5)

from sklearn.datasets import load_iris
iris = load_iris()
from sklearn.trees import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(iris.data,iris.target)
x = model.predict([[x1,x2,y1,y2]])
x = iris.target_names[x[0]]
st.title(x)
