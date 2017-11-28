FROM gcr.io/tensorflow/tensorflow
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE "5000"
CMD ["python", "app.py"]