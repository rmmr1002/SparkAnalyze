# SparkAnalyze
Python Scripts using Spark to analyze datasets

## Prerequisites:
Linux

Install Java, Scala, and Spark according to the particulars of your specific OS. A good starting point is http://www.tutorialspoint.com/apache_spark/apache_spark_installation.htm (but be sure to install Spark 2.0 or newer)
Install the latest Enthought Canopy for Python 3.5 from https://store.enthought.com/downloads/#default 3. Test it out!

  Open up a terminal
  
  cd into the directory you installed Spark, and do an ls to see what’s in there.
  
  Look for a text file we can play with, like README.md or CHANGES.txt
  
  Enter pyspark
  
  At this point you should have a >>> prompt. If not, double check the steps above.
  
  Enter rdd = sc.textFile(“README.md”) (or whatever text file you’ve found) Enter rdd.count()
  
  You should get a count of the number of lines in that file! Congratulations, you just ran your first Spark program!
  
  Enter quit() to exit the spark shell, and close the console window

More at https://sundog-education.com/spark-python/

## Dataset:
https://grouplens.org/datasets/movielens/

100K data set being used here


