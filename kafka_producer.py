import logging
import argparse

from clickstream.producer import Producer


if __name__ == '__main__':
    logging.basicConfig(format='[%(levelname)s] %(message)s',
                        level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv",
                        help="The CSV to read data from.")
    args = parser.parse_args()

    producer = Producer()
    producer.read_file(args.input_csv)
    producer.close()
