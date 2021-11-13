FROM python:3.8

RUN apt-get install -y firefox \
    && apt-get -y update \
    && apt-get install -y nano \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["bash"]
