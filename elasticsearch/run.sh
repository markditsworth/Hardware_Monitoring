#!/bin/bash
docker network create dnetwork --driver bridge
docker run -d -p 9200:9200 -p 9300:9300 --network dnetwork -v $(pwd)/elasticsearch.yml:/usr/share/elasticsearch/config/elasticsearch.yml --name elasticsearch elasticsearch:7.9.3
