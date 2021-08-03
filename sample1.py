import streamlit as st 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# title of the app
st.title("The Machine Learning App")



data=pd.read_csv("C:/Users/Sajan/OneDrive/Documents/Dataset/wine.csv")

content = st.sidebar.selectbox(
    label="Select the content",
    options=['', 'EDA', 'PLOT','Drag and Drop'])
st.header((content))

if content == 'EDA':
    Analysis = st.sidebar.selectbox(
    label = "Select",
    options = ["","Head","Tail","Dimension","Description","Data Cleaning"])
    st.header((Analysis))
			
    if Analysis == "Head":
        try:
            st.write("It shows the First 5 rows of data")
            head = data.head()
            st.write(head)
        except Exception as e:
            print(e)
			
    if Analysis == "Tail":
        try:
            st.write("It shows the last 5 rows of data")
            tail = data.tail()
            st.write(tail)
        except Exception as e:
            print(e)
			
    if Analysis == "Dimension":
        try:
            st.write("It shows the dimension of the data")
            shape = data.shape
            st.write(shape)
        except Exception as e:
            print(e)
            
    if Analysis == "Description":
        try:
            st.write("It shows the description of the data")
            describe = data.describe()
            st.write(describe)
        except Exception as e:
            print(e)
        
    if Analysis == "Data Cleaning":
        try:
            st.write("Null value Handling")
            null = data_missing_columns = (round(((data.isnull().sum()/len(data.index))*100),2).to_frame('null')).sort_values('null', ascending=False)
            st.write(null)
        except Exception as e:
            print(e)
			
			#############################################################





elif content == "PLOT":
	chart = st.sidebar.selectbox(
	label = "Select",
	options = ['',"Bar Plot","Scatter Plot","Line Plot","Histogram","Box Plot"])
	st.header((chart))
	
	if chart == "Bar Plot":
		try:
			
			fig, ax = plt.subplots(figsize = (10,5))
			
			ax = sns.barplot(x="quality", y="residual sugar", data=data)
			st.write(fig)
		except Exception as e:
			print(e)
			
	if chart == "Scatter Plot":
		try:
			fig, ax = plt.subplots(figsize = (10,5))
			ax = sns.scatterplot(data=data, x="pH", y="alcohol", hue="quality", size="quality",sizes=(20, 200), legend="full")
			st.write(fig)
		except Exception as e:
			print(e)
			
	if chart == "Line Plot":
		try:
			fig, ax = plt.subplots(figsize = (10,5))
			ax = sns.lineplot(data=data, x="quality", y="alcohol")
			st.write(fig)
		except Exception as e:
			print(e)
	
	
	if chart == "Histogram":
		try:
			fig, ax = plt.subplots(figsize = (10,5))
			ax = sns.histplot(data=data, x="total sulfur dioxide", hue="quality")
			st.write(fig)
		except Exception as e:
			print(e)
			
	if chart == "Box Plot":
		try:
			fig, ax = plt.subplots(figsize = (10,5))
			ax = sns.boxplot(x="quality", y="fixed acidity", data=data)
			st.write(fig)
		except Exception as e:
			print(e)
			#################################



elif content == "Drag and Drop":
	c = st.sidebar.selectbox(
	label = "Select",
	options = ['',"Numeric","Non Numeric","Drag"])
	st.header((c))
	
	if c == "Numeric":
		try:
			numeric = list(data.select_dtypes(['float','int','float32','int32','float64','int64']).columns)
			numeric = st.sidebar.selectbox("numeric_columns",numeric)
		except Exception as e:
			print (e)
	
	if c == "Non Numeric":
		try:
			non_numeric = list(data.select_dtypes(['object','bool']).columns)
			
			non_numeric = st.sidebar.selectbox("non_numeric_columns",non_numeric)
		except Exception as e:
			print (e)
	
	if c == "Drag":
		try:
			class combo(QComboBox):
				def __init__(self, title, parent):
					super(combo, self).__init__( parent)
					self.setAcceptDrops(True)
					
				def dragEnterEvent(self, e):
					print (e)

					if e.mimeData().hasText():
						e.accept()
					else:
						e.ignore()

				def dropEvent(self, e):
					self.addItem(e.mimeData().text())
			class Example(QWidget):
				def __init__(self):
					super(Example, self).__init__()

					self.initUI()

				def initUI(self):
					lo = QFormLayout()
					lo.addRow(QLabel("Type some text in textbox and drag it into combo box"))
   
					edit = QLineEdit()
					edit.setDragEnabled(True)
					com = combo("Button", self)
					lo.addRow(edit,com)
					self.setLayout(lo)
					self.setWindowTitle('Simple drag and drop')

			def main():
				app = QApplication(sys.argv)
				ex = Example()
				ex.show()
				app.exec_()

			if __name__ == '__main__':
				main()
			
		except Exception as e:
			print(e)
