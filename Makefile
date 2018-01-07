zookeeper:
	zkserver start

kafka:
	kafka-server-start ./config/server.properties

sample_data:
	python kafka_producer.py data/sample.csv

check_topic:
	kafka-console-consumer --zookeeper localhost:2181 --topic clickstream --from-beginning

spark_read:
	spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 spark_read_topic.py localhost 9092

purge_topic:
	kafka-topics --zookeeper localhost:2181 --delete --topic clickstream
