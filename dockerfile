# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /myscripts.py

# # Clone the source code from the Git repository
# RUN apt-get update && apt-get install -y git
# RUN git clone https://github.com/sowjiterralogicc/repos_test.git
# Clone the source code from the Git repository
RUN apt-get update && apt-get install -y git
RUN git clone https://github.com/Maryterralogic/Python_mesia.git /myscripts.py/python_mesia
RUN ls -la /myscripts.py/python_mesia  # Print the contents of the cloned directory


# Change to the cloned directory
WORKDIR /myscripts.py/python_mesia

# Install system dependencies
RUN apt-get install -y libmariadb-dev pkg-config gcc

# Install pkg-config
RUN apt-get install -y pkg-config

# Copy the requirements file into the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Change back to the root directory
WORKDIR /myscripts.py

# Copy the rest of the application code into the container
COPY . .

# Run the script when the container launches
CMD ["python", "myscripts.py"]
