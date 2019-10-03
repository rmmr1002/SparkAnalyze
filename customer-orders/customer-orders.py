from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MinTemperatures")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    customerID = fields[0]   
    amount= fields[2]
    return (customerID, amount)

lines = sc.textFile("customer-orders.csv")  
parsedLines = lines.map(parseLine)  
custAmounts = parsedLines.map(lambda x: (int(x[0]),float( x[1])))

addAmounts = custAmounts.reduceByKey(lambda x, y: x+y)  
addAmountsSorted = addAmounts.map(lambda x: (x[1], x[0])).sortByKey()
results = addAmountsSorted.collect();

for result in results:
    print(str(result[0]) + "\t"+str(result[1]))
