# 1) Base Python image
FROM python:3.10-slim

# 2) Install system packages needed for GeoDjango/PostGIS
RUN apt-get update && apt-get install -y \
    binutils libproj-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# 3) Set working directory
WORKDIR /app

# 4) Python env tweaks
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 5) Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copy project code into the image
COPY . .

# 7) Expose port (optional but nice for docs)
EXPOSE 8000

# 8) Command to run the app using gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
