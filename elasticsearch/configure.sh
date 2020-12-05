#!/bin/bash

curl -X PUT "localhost:9200/_index_template/timeseries_template?pretty" -H 'Content-Type: application/json' -d @templates/timeseries_template.json

curl -X PUT "localhost:9200/_ilm/policy/timeseries_policy?pretty" -H 'Content-Type: application/json' -d @timeseries_policy.json
