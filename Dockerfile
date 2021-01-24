FROM python:latest

ADD main.py /main.py
RUN pip install pygithub

CMD ["python", "/main.py"]
