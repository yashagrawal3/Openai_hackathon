import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from math import sqrt

from scipy.stats import stats

import os
MYDIR = os.path.dirname(__file__)
dir_path1 = os.path.join(MYDIR,'./student-mat.csv')
dir_path2 = os.path.join(MYDIR,'./college.csv')

data = pd.read_csv(dir_path1)

def fun1():
	val =  "hello"
	val2 = "hi"
	return val,val2

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
		data['sex_male'].iloc[i] = 1

	else :
		data["sex_female"].iloc[i] = 1

features = ['age','sex_male','sex_female','traveltime','studytime','failures','schoolsup',
'Medu','Fedu','famsup','activities','higher','romantic','freetime','goout','Dalc',
'Walc','health','absences','G1','G2']

#positive_features = ['G2','G1','Medu','higher','studytime','age',]
#negative_features = ['failures','goout','romantic','traveltime']
feature_array = ['studytime','traveltime','age','goout','romantic','higher','Medu','G1','G2','failures']

x = data[features]
y = data['G3']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.01,random_state=0)
regressor = RandomForestRegressor(max_depth=10,n_estimators=150, min_samples_split=2)
regressor.fit(x_train,y_train)

def predict(user):
	#print user
	user_data = user
	user = x_train.head(1)
	k = 1
	for i in feature_array:
        	user[i]= user_data[k]
		k = k+1
	user['romantic'].iloc[0] = (user['romantic'].iloc[0]=='yes')*0
	user['higher'].iloc[0] = (user['higher'].iloc[0]=="yes")*1
	user['schoolsup'].iloc[0] = int(x_train["schoolsup"].median())
	user['Fedu'].iloc[0] = user_data[7]
	if user_data[11] == "M":
        	user['sex_male'].iloc[0] = 1
        	user['sex_female'].iloc[0] = 0
	else:
        	user['sex_male'].iloc[0] = 0
        	user['sex_female'].iloc[0]=1
	user['freetime'].iloc[0] = int(x_train["freetime"].median())
	print user
	predict =regressor.predict(user)
	
	college = pd.read_csv(dir_path2)
        data_required = college[['INSTNM','SAT_AVG_ALL']]
        data1 = data_required.dropna()

        data1['z_score']=0
        z_score = stats.zscore(data1['SAT_AVG_ALL'])
        z_score = z_score.round(2)
        data1['z_score'] = z_score

        data_grades = data['G3']
        data_grades = np.append(data_grades,predict[0])
        zscore_student = stats.zscore(data_grades)
        zscore_student = zscore_student.round(2)
	college_suggest = data1['INSTNM'][data1['z_score'] == zscore_student[-1]]

	return predict,college_suggest



