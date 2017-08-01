import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from math import sqrt

from scipy.stats import stats

#Training the Model

student_grades   =   pd.read_csv('./hackathon_data/student-mat.csv')
data = student_grades.copy()

data['famsize'] = (data['famsize'] == "GT3")*0
data['romantic'] = (data['romantic'] == "yes")*1
data['higher'] = (data['higher'] == "yes")*1
data['activities'] = (data['activities'] == "yes")*1
data['paid'] = (data['paid'] == "yes")*1
data['famsup'] = (data['famsup'] == "yes")*1
data['schoolsup'] = (data['schoolsup'] == "yes")*1

data['sex_male'] = 0
data['sex_female'] = 0

for i in range (0,len(data['sex'])):
    
	if data['sex'][i] == "M":
		data['sex_male'][i] = 1
           
	else :
		data["sex_female"][i] = 1

#important fields
features = ['age','sex_male','sex_female','traveltime','studytime','failures','schoolsup',
            'Medu','Fedu','famsup','activities','higher','romantic','freetime','goout','Dalc',
            'Walc','health','absences','G1','G2']

x = data[features]
y = data['G3']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.01,random_state=0)
regressor = RandomForestRegressor(max_depth=10,n_estimators=150, min_samples_split=2)
regressor.fit(x_train,y_train)

   
positive_features = ['G2','G1','Medu','higher','studytime','age',]
negative_features = ['failures','goout','romantic','traveltime']
feature_array = ['studytime','traveltime','age','goout','romantic','higher','Medu','G1','G2','failures']

user_data=[]
user_name = input("Welcome!!! Please Enter your name: ")
user_data.append(user_name)
data1 = input("Please mention the nxo. of hours you study : ")

data2 = input("Mention your daily travel time : ")

data3 = input("What is your age : ")
data4 = input("How much of time do you spend with your friends : ")
    
data5 = input("Are you presently in a relationship'(yes or no)'")
data6 = input("Do you wish to pursue higher studies '(yes or no)': ")
data7 = input("On a scale of 1 to 5 what is your family education '(1 being primary to 5 being college degree)' :")
data8 = input("Mention your score in first test : ")
data9 = input("Mention your score in second test : ")
data10 = input("how many test have you failed '(1 ,2 or 3)' : ")
data11 = input("please mention your gender :")
for i in range(1,11):
    data = "data"+str(i)
    user_data.append(globals()[data]) 
  

#user = {'age':user_data[3], 'traveltime':user_data[2],'studytime':user_data[1], 'failures':user_data[10], 'schoolsup':int(x_train["schoolsup"].median()), 'Medu':user_data[7], 'Fedu':user_data[7], 'famsup':int(x_train["famsup"].median()),
 #       'activities':int(x_train["activities"].median()), 'higher':1,'romantic':1,
  #     'freetime':int(x_train["freetime"].median()), 'goout':user_data[4], 'Dalc':int(x_train["Dalc"].median()), 'Walc':int(x_train["Walc"].median()), 'health':int(x_train["health"].median()), 'absences':int(x_train["absences"].median()), 'G1':user_data[8],
   #    'G2':user_data[9]}

user = x_train.head(1)

k=1
for i in feature_array:
    user[i]= user_data[k]
    k = k+1
user['romantic'] = (user['romantic']=='yes')*0
user['higher'] = (user['higher']=="yes")*1
user['schoolsup'] = int(x_train["schoolsup"].median())
user['Fedu'] = user_data[7]
if data11 == "M":
	user['sex_male'] = 1
	user['sex_female'] = 0
else:
	user['sex_male'] = 0
	user['sex_female']=1
user['freetime'] = int(x_train["freetime"].median())
	

predict = regressor.predict(user)
print(user_data[0]," your predicted score is :" , predict)

#Suggesting methods to improve User's Score

score = input("Enter your target score : ")
score1 = int(score)
print(x_train[np.logical_and(y_train>=score1-1,y_train<=score1+1)][["goout","studytime"]])

#College prediction on the basis of students score (v1)

data_college = pd.read_csv('hackathon_data/college.csv')
data_required = data_college[['INSTNM','SAT_AVG_ALL']]
data = data_required.dropna()

data['z_score']=0
z_score = stats.zscore(data['SAT_AVG_ALL'])
z_score = z_score.round(2)
data['z_score'] = z_score

data_grades = student_grades['G3']
data_grades = np.append(data_grades,predict[0])
zscore_student = stats.zscore(data_grades)
zscore_student = zscore_student.round(2)

print("following are the college you can opt for")
print(data['INSTNM'][data['z_score'] == zscore_student[-1]])


