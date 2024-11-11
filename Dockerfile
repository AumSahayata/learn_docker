FROM python:3.11.9

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src ./src
EXPOSE 5000

CMD ["uvicorn", "src:app", "--host", "0.0.0.0", "--port", "5000"]
