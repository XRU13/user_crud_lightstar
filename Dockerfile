FROM python:3.12-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry==1.8.3

# Copy poetry files
COPY pyproject.toml poetry.lock* ./

# Configure poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy application code
COPY . .

# Run the application
CMD ["python", "-m", "uvicorn", "app.asgi:app", "--host", "0.0.0.0", "--port", "8000"] 
