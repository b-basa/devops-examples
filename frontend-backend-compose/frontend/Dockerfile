FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir dash

COPY frontend.py .

RUN apt update
RUN apt install bind9-dnsutils -y
RUN apt install net-tools -y
RUN apt install iputils-tracepath -y
RUN apt install iputils-ping -y
RUN apt install curl -y
RUN apt install wget -y
RUN apt install whois -y

EXPOSE 8050
CMD ["python", "frontend.py"]