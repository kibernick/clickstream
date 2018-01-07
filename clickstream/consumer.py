# https://github.com/eBay/Spark/blob/master/examples/src/main/python/streaming/direct_kafka_wordcount.py
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


class Consumer:

    def __init__(self, broker_url='localhost:9092', topic='clickstream', fetch_interval=2):
        self.broker_url = broker_url
        self.topic = topic
        self.fetch_interval = fetch_interval  # seconds

    def _setup_streaming(self):
        sc = SparkContext('local[2]', 'ReadKafkaTopic')
        ssc = StreamingContext(sc, self.fetch_interval)

        kvs = KafkaUtils.createDirectStream(ssc, [self.topic], {
            'metadata.broker.list': self.broker_url
        })
        rows = kvs.map(lambda x: x[1])  # DStream

        return ssc, rows
        #
        # rows.pprint()
        #
        # return ssc

    def read_topic(self):
        ssc, rows = self._setup_streaming()
        rows.pprint()
        return ssc
