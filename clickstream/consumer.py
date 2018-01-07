# https://github.com/eBay/Spark/blob/master/examples/src/main/python/streaming/direct_kafka_wordcount.py
import csv

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


class Consumer:

    def __init__(self, broker_url='localhost:9092', topic='clickstream', fetch_interval=10):
        self.broker_url = broker_url
        self.topic = topic
        self.fetch_interval = fetch_interval  # seconds

    def _setup_streaming(self, appName):
        sc = SparkContext('local[2]', appName)
        ssc = StreamingContext(sc, self.fetch_interval)

        kvs = KafkaUtils.createDirectStream(ssc, [self.topic], {
            'metadata.broker.list': self.broker_url
        })
        rows = kvs.map(lambda x: x[1])  # DStream

        return ssc, rows

    def read_topic(self):
        ssc, rows = self._setup_streaming('ReadTopic')

        rows.pprint()  # pyspark.streaming.kafka.KafkaTransformedDStream

        return ssc

    @staticmethod
    def _extract_url(row):
        try:
            reader = csv.reader([row])
            items = next(reader)
            page_urlpath = items[3]
            return page_urlpath.split('/')[2]
        except (TypeError,  # not a valid CSV row
                StopIteration,  # empty row
                IndexError):  # row without enough elements
            return ''

    def categories(self, window_duration, slide_duration):
        ssc, rows = self._setup_streaming('Categories')
        ssc.checkpoint("checkpoint")

        counts = rows.map(self._extract_url) \
            .map(lambda category: (category, 1)) \
            .reduceByKeyAndWindow(lambda x, y: x + y,
                                  lambda x, y: x - y,
                                  windowDuration=window_duration,
                                  slideDuration=slide_duration)
        counts.pprint()

        return ssc
