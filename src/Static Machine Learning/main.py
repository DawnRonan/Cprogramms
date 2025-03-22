'''
Created on 2024. márc. 8.

@author: adylaszlo
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def load_data():
    URL_='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    data = pd.read_csv(URL_, header = None)
    print(data)

    # make the dataset linearly separable
    data = data[:100]
    data[4] = np.where(data.iloc[:, -1]=='Iris-setosa', 0, 1)
    data = np.asmatrix(data, dtype = 'float64')
    return data

def show_data(data):
    group0 = [data[:50,0],data[:50,2]]
    group1 = [data[50:,0],data[50:,2]]
    show_dia(group0,group1,'setosa','versicolor')

def show_dia(group0,group1,label0,label1):
    plt.scatter(np.array(group0[0]), np.array(group0[1]), marker='o', label=label0)
    plt.scatter(np.array(group1[0]), np.array(group1[1]), marker='x', label=label1)
    plt.xlabel('petal length')
    plt.ylabel('sepal length')
    plt.legend()
    plt.show()

def show_teaching(num_iter,misclassified_):
    epochs = np.arange(1, num_iter+1)
    plt.plot(epochs, misclassified_)
    plt.xlabel('iterations')
    plt.ylabel('misclassified')
    plt.show()
class Perceptron():

    def __init__(self,w=None):
        self.w = w

    def teach(self,data, num_iter):
        '''
        1. set b = w = 0
        2. for N iterations, or until weights do not change
               (a) for each training example xᵏ with label yᵏ
                   i. if yᵏ — f(xᵏ) = 0, continue
                   ii. else, update wᵢ, △wᵢ = (yᵏ — f(xᵏ)) xᵢ
        '''

        features = data[:, :-1]
        labels = data[:, -1]

        # set weights to zero
        self.w = np.zeros(shape=(1, features.shape[1]+1))

        misclassified_ = []

        for epoch in range(num_iter):
            misclassified = 0
            for x, label in zip(features, labels):
                x = np.insert(x,0,1)
                y = np.dot(self.w, x.transpose())
                target = 1.0 if (y > 0) else 0.0
                #target = self.decision(x)

                delta = (label.item(0,0) - target)

                if(delta): # misclassified
                    misclassified += 1
                    self.w += (delta * x)

            misclassified_.append(misclassified)
        return misclassified_


    def decision(self,inputs):
        x = np.insert(inputs,0,1)
        y = np.dot(self.w, x.transpose())
        target = 1.0 if (y > 0) else 0.0
        return target



if __name__ == '__main__':

    mode = "custom"

    if mode == "flovers_teach":

        # Download teaching datas and teaching

        data = load_data()

        show_data(data)
        num_iter = 10
        perceptron = Perceptron()
        misclassified_ = perceptron.teach(data, num_iter)
        w = perceptron.w
        print("w vector: ",w)
        show_teaching(num_iter, misclassified_)


    elif mode == "flovers":
        data = load_data()
        # Use trained perceptron
        w = [-1, -1.1,-3.6 ,5.2 ,2.2]
        perceptron = Perceptron(w)
        print(perceptron.decision([5.7,2.8,4.1,1.3]))
        print(perceptron.decision([4.3,3  ,1.4,0.1]))

        setosa0 = []
        setosa1 = []
        verticosa0 = []
        verticosa1 = []

        for p in data:

            inputs = [p.flat[0],p.flat[1],p.flat[2],p.flat[3] ]
            print(inputs)
            decision = perceptron.decision(inputs)
            print(decision)
            if decision == 1:
                verticosa0.append(inputs[0])
                verticosa1.append(inputs[2])
            else:
                setosa0.append(inputs[0])
                setosa1.append(inputs[2])

        for s in range(20,35):
            for p in range(40,70):
                inputs = [p/10,2.9,s/10,1.3 ]
                print(inputs)
                decision = perceptron.decision(inputs)
                print(decision)
                if decision == 1:
                    verticosa0.append(inputs[0])
                    verticosa1.append(inputs[2])
                else:
                    setosa0.append(inputs[0])
                    setosa1.append(inputs[2])

        group0 = [setosa0,setosa1]
        group1 = [verticosa0,verticosa1]
        show_dia(group0, group1,'setosa','versicolor')

    elif mode == "custom":

        data =[]
        data.append([1,0,0])
        data.append([0,1,0])
        data.append([1,1,0])

        data.append([3,0,1])
        data.append([3,2,1])
        data.append([2,3,1])
        data.append([0,3,1])



        data = np.asmatrix(data, dtype = 'float64')
        print(data)
        for r in data:
            print(r)

        num_iter = 10
        perceptron = Perceptron()
        misclassified_ = perceptron.teach(data, num_iter)
        w = perceptron.w
        print("w vector: ",w)

        group0 = [[],[]]
        group1 = [[],[]]




        for s in range(0,40):
            for p in range(0,70):
                inputs = [p/10,s/10]
                print(inputs)
                decision = perceptron.decision(inputs)
                print(decision)
                if decision == 1:
                    group1[0].append(inputs[0])
                    group1[1].append(inputs[1])
                else:
                    group0[0].append(inputs[0])
                    group0[1].append(inputs[1])

        show_dia(group0, group1,'group0','vgroup1')


    elif mode == "custom_3group":

        gt0 = []
        gt0.append([5,0,0])
        gt0.append([5,3,0])

        gt1 = []
        gt1.append([2,0,1])
        gt1.append([2,3,1])

        gt2 = []
        gt2.append([-3,0,1])
        gt2.append([-3,3,1])

        data =[]
        for d in gt0:
            data.append(d)
        for d in gt1:
            data.append(d)
        for d in gt2:
            data.append(d)



        data = np.asmatrix(data, dtype = 'float64')
        print(data)
        for r in data:
            print(r)

        num_iter = 10
        perceptron1 = Perceptron()
        misclassified_ = perceptron1.teach(data, num_iter)
        w = perceptron1.w
        print("w vector: ",w)
        show_teaching(num_iter, misclassified_)

        data =[]
        for d in gt1:
            data.append([d[0],d[1],0])
        for d in gt2:
            data.append(d)

        data = np.asmatrix(data, dtype = 'float64')
        print(data)
        for r in data:
            print(r)

        num_iter = 10
        perceptron2 = Perceptron()
        misclassified_ = perceptron2.teach(data, num_iter)
        w = perceptron2.w
        print("w vector: ",w)
        show_teaching(num_iter, misclassified_)

        group0 = [[],[]]
        group1 = [[],[]]
        group2 = [[],[]]

        for s in range(-40,40):
            for p in range(-40,70):
                inputs = [p/10,s/10]
                print(inputs)
                decision1 = perceptron1.decision(inputs)
                print(decision1)
                if decision1 == 1:
                    decision2 = perceptron2.decision(inputs)
                    print(decision2)
                    if decision2 == 1:
                        group2[0].append(inputs[0])
                        group2[1].append(inputs[1])
                    else:
                        group1[0].append(inputs[0])
                        group1[1].append(inputs[1])
                else:
                    group0[0].append(inputs[0])
                    group0[1].append(inputs[1])
        #show_dia(group0, group1,'setosa','versicolor')
        plt.scatter(np.array(group0[0]), np.array(group0[1]), marker='o', label="0")
        plt.scatter(np.array(group1[0]), np.array(group1[1]), marker='x', label="1")
        plt.scatter(np.array(group2[0]), np.array(group2[1]), marker='x', label="2")
        plt.xlabel('0')
        plt.ylabel('1')
        plt.ylabel('2')
        plt.legend()
        plt.show()