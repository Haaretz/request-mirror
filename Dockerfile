FROM python:3
RUN pip install flask
WORKDIR /WORKSPACE/
COPY . /WORKSPACE/
CMD ["python","main.py"]
