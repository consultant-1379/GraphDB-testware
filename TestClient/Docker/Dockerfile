FROM python

ARG CONFIG_FILE_ARG="config.json"

ENV CONFIG_FILE=$CONFIG_FILE_ARG

ADD ./TestClient /test_client

WORKDIR /test_client

RUN pip3 install -r requirements.txt

ENTRYPOINT ["./Docker/entrypoint.sh"]