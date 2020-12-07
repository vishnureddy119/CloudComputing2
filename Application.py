from pyspark.mllib.tree import RandomForestModel
from pyspark.sql import SparkSession
from pyspark.mllib.regression import LabeledPoint, LinearRegressionWithSGD
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.evaluation import MulticlassMetrics, MultilabelMetrics
import sys
#from sklearn.metrics import f1_score
spark = SparkSession.builder \
        .appName("Linear Regression Model") \
        .getOrCreate()


output_dir = 'model'

data1 = spark.read.format("csv").option('sep',';').option('inferSchema','true').option('header','true').load(sys.argv[1])
rdd_data1 = data1.rdd.map(lambda x:LabeledPoint(x[11], x[0:11]))

#sameModel = NaiveBayesModel.load(spark, output_dir)
#predictionAndLabel = rdd_data1.map(lambda p: (sameModel.predict(p.features), p.label))

sameModel = RandomForestModel.load(spark.sparkContext, output_dir)
predictionAndLabel = sameModel.predict(rdd_data1.map(lambda x: x.features))
labels_and_predictions = rdd_data1.map(lambda x: x.label).zip(predictionAndLabel)

#print(labels_and_predictions.collect())

#acc = labels_and_predictions.filter(lambda x: x[0] == x[1]).count() / float(rdd_data1.count())
#print("Model accuracy: %.3f%%" % (acc * 100))

#print(predictionAndLabel.collect())
metrics=MulticlassMetrics(labels_and_predictions)
#x_axis = labels_and_predictions.map(lambda x:x[0])
#y_axis=labels_and_predictions.map(lambda x:x[1])
#x_axis = list(x_axis.collect())
#y_axis = list(y_axis.collect())

#f1score = f1_score(y_axis,x_axis,average='weighted')

print('fl score is : ', metrics.weightedFMeasure())
spark.stop()
