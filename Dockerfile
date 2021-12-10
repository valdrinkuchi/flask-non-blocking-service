FROM python:3.8-alpine
ENV PATH="/opt/scripts:${PATH}"

COPY . /opt
WORKDIR /opt
RUN pip install -r requirements.txt
RUN chmod +x /opt/scripts/*
RUN apk --update add bash && \
    apk add dos2unix
RUN apk add nano

CMD ["entrypoint.sh"]