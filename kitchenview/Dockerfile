#use python runtime
FROM python:3.9-slim
#set the working directory
WORKDIR /app
#copy the requirements
COPY requirements.txt .
#install depencies
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
