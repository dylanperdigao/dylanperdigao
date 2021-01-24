FROM debian:9.5-slim

ADD main.py /main.py
RUN chmod +x /main.py

ENTRYPOINT ["/main.py"]
