
# Final Dockerfile for Render deployment
FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y tesseract-ocr poppler-utils libgl1-mesa-glx && \
    apt-get clean

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ENABLECORS=false

CMD ["streamlit", "run", "ui/app.py"]
