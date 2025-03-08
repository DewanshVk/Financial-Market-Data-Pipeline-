FROM apache/airflow:2.7.1-python3.10

USER root

# Install extra packages if needed
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt

USER airflow

# Default command
CMD ["airflow", "standalone"]
