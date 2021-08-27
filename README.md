# ElasticSearch IK Analyzer Hot Word API

> Description: This is an API interface used for ElasticSearch IK tokenizer.

## Usage:

1. You need a python environment (`Python 3.7` is recommended)
2. Install requirement (`fastapi` and `uvicorn`)
3. Execute the `main.py` file (default port is `9375`, you can edit it in `main.py` file)
4. Add the api url in your ik plugin config (`[YOUR_ES_INSTALL_PATH]/plugins/ik/config/IKAnalyzer.cfg.xml`
5. Then restart the Elastic Server (If you are using docker, just simply called `docker elasticsearch restart`)


## Extra Desciption:

1. You can test your api by accessing `http://localhost:9375/docs` or `http://YOUR_IP:9375/docs`
2. If you want to add word, just simply edit the `data.txt`, and save the file.
3. Then update the header by calling the `update` method: (`http://localhost:9375/update?tag=tag_name`)
4. Then the IK will automatically update those word into the dictionary, no need to restart ES service.


## Future TO-DO
1. Save the dictionary into database (MySQL)
