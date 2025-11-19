FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./open_synth_fi ./open_synth_fi

CMD ["uvicorn", "open_synth_fi.main:app", "--host", "0.0.0.0", "--port", "8000"]
