#compare all the ML method
from sklearn import tree   				#decision tree
from sklearn import svm 				#support vector machine
from sklearn.naive_bayes import GaussianNB	 	#naive bayes
from sklearn.neural_network import MLPClassifier	#neural network
from sklearn.metrics import accuracy_score		#library for find accuracy score
import array						#for creating array
import numpy as np 					#for find maximum array index


# Dataset for the gender prediction
X = [[181,80,44], [177, 70,43], [160,60,38],[154,54,37],[166,65,40],
	 [190,90,47],[175,64,39],
	 [177,70,40],[159,55,37],[171,75,42],[181,85,43]]
Y = ['male','male','female','female','male','male','female','female',
	'female','male','male']

#Classifier	
method =['Decision Tree','Support Vector Machine','Naive Bayes','Neural Network']
clf= [0 for x in range(4)]
clf[0] = tree.DecisionTreeClassifier()
clf[1] = svm.SVC()
clf[2] = GaussianNB()
clf[3] = MLPClassifier(solver='lbfgs',alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1)


#Train the models and print accuracy score of each model
acc=[]
for i in range(len(clf)):
	clf[i].fit(X,Y)
	pred = clf[i].predict(X)
	accurate = accuracy_score(Y, pred) * 100
	acc.append(accuracy_score(Y, pred) * 100)
	print('Accuracy for {}: '.format(method[i]),accurate)

#Pick the best method for this model
print('The most accurate score method for this model is:',method[np.argmax(acc)])

