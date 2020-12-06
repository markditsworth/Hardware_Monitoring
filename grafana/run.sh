#!/bin/bash
docker run -d --network dnetwork -p 3000:3000 --name grafana grafana/grafana
