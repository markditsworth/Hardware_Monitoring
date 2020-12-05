#!/bin/bash

docker run -d --name kibana --network dnetwork -v $(pwd)/kibana.yml:/usr/share/kibana/config/kibana.yml -p 5601:5601 kibana:7.9.3
