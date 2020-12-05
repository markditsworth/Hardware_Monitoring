#!/usr/bin/python3

import serial
import elasticsearch
import json
import argparse

from datetime import datetime

def index_to_es(es, index_name, doc):
        try:
                json_data = json.loads(doc)
                json_data['@timestamp'] = datetime.utcnow()
                print(json_data)
                res = es.index(index_name, json_data)
        except Exception as e:
                print("Failed to index '{}'".format(doc))
                print(type(e))
                print(e)
        

def run(port, baud, host, index_name):
        es = elasticsearch.Elasticsearch(host)
        with(serial.Serial(port,baud)) as mcu_uart:
                while True:
                        try:
                                data = mcu_uart.readline().decode('utf-8').strip()
                                print(data)
                                index_to_es(es, index_name, data)
                        except UnicodeDecodeError:
                                print("Unicode Decode Error on")
                                print(data)

if __name__ == '__main__':
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('--baud', type=int, default=9600,
                    help='baud rate')
        parser.add_argument('--dev', type=str,
                    default='/dev/ttyACM0',
                    help='USB location (default /dev/ttyACM0')
        parser.add_argument('--index', type=str, default='timeseries', help='name of elasticsearch index')
        parser.add_argument('--host', type=str, default='localhost:9200', help='elasticsearch host')

        args = parser.parse_args()

        run(args.dev, args.baud, args.host, args.index)
        
