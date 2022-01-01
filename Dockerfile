FROM tiangolo/uvicorn-gunicorn:python3.8

COPY ./ /party_finder

WORKDIR /party_finder


RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
