# Use a lightweight mongodb-community-server base image
FROM mongodb/mongodb-community-server:latest

# Utiliser le bon utilisateur (si nécessaire)
USER root

# Mettre à jour et installer python et pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8050

# Define the entrypoint
CMD ["python3", "app/Main.py"]
