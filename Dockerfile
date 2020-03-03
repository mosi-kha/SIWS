FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Set up and activate virtual environment
ENV VIRTUAL_ENV "/venv"
RUN python -m venv $VIRTUAL_ENV
ENV PATH "$VIRTUAL_ENV/bin:$PATH"

EXPOSE 8000

COPY requirements.txt requirements.txt
# Python commands run inside the virtual environment
RUN pip install -r requirements.txt

WORKDIR /usr/src/app
COPY . /usr/src/app

CMD ["python","./main.py"]

