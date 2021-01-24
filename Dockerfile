FROM python:latest

ADD main.py /main.py
RUN pip install pygithub

ENTRYPOINT ["/main.py"]
