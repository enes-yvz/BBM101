import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iterationList=[]

fig1= plt.figure(figsize=(15,15))
a0=fig1.add_axes([0.3,0.3,0.5,0.5])
fig2,(a1,a2) = plt.subplots(2,1,figsize=(15,15))

dataset = pd.read_csv("breast-cancer-wisconsin.csv")
dataset=dataset.drop(["Code_number"],1)
dataset=dataset.replace(to_replace="?",value=np.nan)
dataset=dataset.dropna(axis="rows")
dataset = dataset.astype(int)

def sigmoid(x):
    return 1 / (1 + np.exp(-0.005*x))

def sigmoid_derivative(x):
    return 0.005 * x * (1 - x )

def read_and_divide_into_train_and_test(dataset):
    training_inputs = dataset.sample(frac=0.8)
    test_inputs = dataset.drop(training_inputs.index)
    heatmap = training_inputs.drop(["Class"],axis=1).corr()
    column_names = list(training_inputs.drop(["Class"],axis=1).columns)
    im= a0.imshow(heatmap, cmap='hot', interpolation='nearest')
    fig1.colorbar(im,ax=a0,pad=0.2)
    a0.set_title("Heatmap Of Pairwise Correlations",fontsize=20,pad=20)
    a0.set_xticks(np.arange(len(column_names)))
    a0.set_xticklabels(column_names,rotation="90",fontsize=8)
    a0.set_yticks(np.arange(len(column_names)))
    a0.set_yticklabels(column_names,fontsize=8)
    for (i, j), z in np.ndenumerate(heatmap):
        a0.text(j, i, '{:0.2f}'.format(z), ha='center', va='center')
    training_inputs=training_inputs.values
    test_inputs = test_inputs.values
    training_labels = training_inputs[:,[9]]
    training_inputs = training_inputs[:,[0,1,2,3,4,5,6,7,8]]
    test_labels = test_inputs[:,[9]]
    test_inputs = test_inputs[:,[0,1,2,3,4,5,6,7,8]]
    return training_inputs, training_labels, test_inputs, test_labels

def run_on_test_set(test_inputs, test_labels, weights):
    tp = 0
    test_outputs= sigmoid(np.dot(test_inputs,weights))
    test_predictions=np.empty((0,1),dtype=int)
    for i in test_outputs:
        if i>0.5:
            test_predictions=np.vstack((test_predictions,[1]))
        else:
            test_predictions = np.vstack((test_predictions,[0]))
    for predicted_val, label in zip(test_predictions, test_labels):
        if predicted_val == label:
            tp += 1
    accuracy= tp/len(test_labels)
    return accuracy

def plot_loss_accuracy(accuracy_array, loss_array):

    a1.plot(iterationList,accuracy_array)
    a1.set_xlabel("Iteration Count")
    a1.set_ylabel("Accuracy Percentage")
    a1.set_title("Accuracy Plot")

    a2.plot(iterationList,loss_array)
    a2.set_xlabel("Iteration Count")
    a2.set_ylabel("Loss Amount")
    a2.set_title("Loss Plot")

def main():
    global iteration_count
    iteration_count = 2500
    np.random.seed(1)
    weights = 2 * np.random.random((9, 1)) - 1
    accuracy_array = []
    loss_array = []
    training_inputs, training_labels, test_inputs, test_labels = read_and_divide_into_train_and_test(dataset)
    for iteration in range(iteration_count):
        outputs = np.dot(training_inputs, weights)
        outputs = sigmoid(outputs)
        loss = training_labels - outputs
        tuning = loss * sigmoid_derivative(outputs)
        weights += np.dot(np.transpose(training_inputs), tuning)
        loss_array.append(np.mean(loss, axis=0))
        run_on_test_set(test_inputs, test_labels, weights)
        accuracy_array.append(run_on_test_set(test_inputs, test_labels, weights)*100)
        iterationList.append(iteration)

    plot_loss_accuracy(accuracy_array, loss_array)   

if __name__ == '__main__':
    main()

plt.subplots_adjust(top=0.95)
plt.show()