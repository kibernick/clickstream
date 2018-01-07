import logging
import time
import random

from kafka import KafkaProducer


class Producer:

    def __init__(self, broker_url='localhost:9092', topic='clickstream'):
        self.producer = KafkaProducer(bootstrap_servers=broker_url)
        # TODO: catch errors like `kafka.errors.NoBrokersAvailable`
        self.topic = topic

    def stream_data(self, row, jitter=True):
        """Stream data to Kafka. Note that `producer.send` is an asynchronous operation.

        :param row: bytes to send
        :param jitter: (bool) whether to introduce random jitter
        """
        self.producer.send(self.topic, row)
        if jitter:
            wait_seconds = int(random.triangular(low=0, high=3, mode=0))  # Simulate random incoming stream.
            time.sleep(wait_seconds)

    def read_file(self, filename, skip_header=True):
        """Read data from file and stream each row to Kafka.

        :param filename: Path to the file to be read
        :param skip_header: (bool) Skip (CSV) header
        """
        count = 0
        with open(filename, 'rb') as f:
            if skip_header:
                next(f)  # Ignore header.
            try:
                for row in f:
                    self.stream_data(row)
                    count += 1
            except KeyboardInterrupt:
                logging.warning("Producer interrupted on row %s" % (count + 1))
            except Exception as e:
                import pdb; pdb.set_trace()
                logging.error(e)
            finally:
                self.producer.flush()
        logging.info("%s rows read." % count)

    def close(self):
        self.producer.close()
