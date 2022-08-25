import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import matplotlib.pyplot as plt

# import training data
data = pd.read_json("stock-data.json")

# split data in train/test
try:
    trainData,testData = train_test_split(data,test_size=.2,stratify=data["recommendationKey"])
except:
    tooFewRecs = []
    for rec in data["recommendationKey"].unique():
        if len(data[data["recommendationKey"] == rec]) < 2:
            tooFewRecs.append(rec)
    abundantData = data[~data["recommendationKey"].isin(tooFewRecs)]
    trainData,testData = train_test_split(abundantData,test_size=.2,stratify=abundantData["recommendationKey"])
    for rec in tooFewRecs:
        trainData = trainData.append(data[data["recommendationKey"] == rec])

# split into train/test x/y sets
trainX = trainData.drop(["recommendationKey"],axis = True)
trainY = trainData.filter(["recommendationKey"],axis = True)
testX = testData.drop(["recommendationKey"],axis = True)
testY = testData.filter(["recommendationKey"],axis = True)

# iterate through different max_depths to see which has best accuracy
models = {}
for i in range(1,20):
    model = tree.DecisionTreeClassifier(max_depth=i)
    model = model.fit(trainX,trainY)
    preds = model.predict(testX)
    models[f"depth: {i}"] = {"acc": sum(testY["recommendationKey"] == preds)/len(preds), "model": model}

accs = []
for model in models:
    accs.append(models[model]["acc"])

plt.plot(accs)

# iterate through full data set and see best accuracy
fullX = data.drop(["recommendationKey"],axis = True)
fullY = data.filter(["recommendationKey"],axis = True) 

fmodels = {}
for i in range(1,20):
    fmodel = tree.DecisionTreeClassifier(max_depth=i)
    fmodel = fmodel.fit(fullX,fullY)
    fpreds = fmodel.predict(fullX)
    fmodels[f"depth: {i}"] = {"acc": sum(fullY["recommendationKey"] == fpreds)/len(fpreds), "model": fmodel}

faccs = []
for fmodel in fmodels:
    faccs.append(fmodels[fmodel]["acc"])

plt.plot(faccs)
