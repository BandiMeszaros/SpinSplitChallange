

from pyspark.streaming import StreamingContext
import argparse
from pyspark.sql import SparkSession
from pyspark.sql.types import Row
from pyspark import StorageLevel
from pyspark.sql.types import DoubleType
import matplotlib.pyplot as plt

sc = SparkSession.builder.master("local[2]").appName("test").getOrCreate()

HOST = "127.0.0.1"
PORT = 11111

def CLI():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-host", dest="host", help= "Host IP", action="store")
    parser.add_argument("-port", dest="port", action="store", help="Host port number", type=int)
    args = parser.parse_args()
    return args


def clientStreaming(host, port):

    def dataProcess(rdd):
        try:
            rowRdd = rdd.map(lambda w: Row(value=w))
            if rowRdd.count() > 0:
                df = sc.createDataFrame(rowRdd)
                df.withColumn("value", df["value"].cast(DoubleType()))
                df.show()
                pdf = df.toPandas()
                pdf["value"] = list(map(lambda x: float(x), pdf["value"]))
                pdf["x"] = list(pdf.index)
                pdf.plot(kind="scatter", x="x", y="value")
                plt.savefig("graph.png")
                print(df.count())
        except Exception as e:
            print(f"{e}")

    ssc = StreamingContext(sc.sparkContext, 2)
    lines = ssc.socketTextStream(host, port, storageLevel=StorageLevel.MEMORY_AND_DISK)
    lines.foreachRDD(dataProcess)
    ssc.start()
    ssc.awaitTermination()

def main():
    arg = CLI()

    if arg.host is None:
        host = HOST
    else:
        host = arg.host
    if arg.port is None:
        port = PORT
    else:
        port = arg.port

    clientStreaming(host, port)
    return 0
if __name__ == "__main__":
    main()