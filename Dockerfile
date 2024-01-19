FROM selenium/standalone-chrome

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN export CHROMEDRIVER=~/chromedriver

RUN sudo apt-get update && sudo apt-get install -y python3-pip && sudo apt-get -y install git
USER root
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "example_script.py"]
