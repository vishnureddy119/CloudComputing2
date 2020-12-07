from pyspark.mllib.clustering import KMeans, GaussianMixture
from pyspark.sql import SparkSession
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.evaluation import MulticlassMetrics
from pyspark.ml.feature import VectorAssembler
from pyspark.mllib.tree import RandomForest


spark = SparkSession.builder \
   .master("local") \
   .appName("Model") \
   .config("spark.executor.memory", "1gb") \
   .getOrCreate()

#spark

# Loading the Training and Validation Datasets

data = spark.read.format("csv").option('sep',';').option('inferSchema','true').option('header','true').load('TrainingDataset.csv')

#data1 = spark.read.format("csv").option('sep',';').option('inferSchema','true').option('header','true').load('C:\\Users\\mintu\\OneDrive\\Desktop\\ValidationDataset.csv')

rdd_data = data.rdd.map(lambda x:LabeledPoint(x[11], x[0:11]))

#rdd_data1 = data1.rdd.map(lambda x:LabeledPoint(x[11], x[0:11]))

print(rdd_data.collect())

'''
print(rdd_data1.collect())
model = LinearRegressionWithSGD.train(rdd_data)
valuesAndPreds = rdd_data.map(lambda p: (p.label, model.predict(p.features)))
valuesAndPreds.collect()
'''

# Creating the Model
#model = NaiveBayes.train(rdd_data, 0.4)

model = RandomForest.trainClassifier(rdd_data, numClasses=10, categoricalFeaturesInfo={},numTrees=3)

#predictions = model.predict(rdd_data.map(lambda x: x.features))
#labels_and_predictions = rdd_data.map(lambda x: x.label).zip(predictions)
#acc = labels_and_predictions.filter(lambda x: x[0] == x[1]).count() / float(rdd_data.count())
#print("Model accuracy: %.3f%%" % (acc * 100))


'''
# Prediction for NaiveBayes
predictionAndLabel = rdd_data.map(lambda p: (model.predict(p.features), p.label))
print(predictionAndLabel.collect())
#Calculating the accuracy
accuracy = 1.0 * predictionAndLabel.filter(lambda pl: pl[0] == pl[1]).count() / rdd_data.count()
print(accuracy)
'''

#saving the model
#model.save(spark.sparkContext,'model')

spark.stop()