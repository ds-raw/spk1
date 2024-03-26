FROM mcr.microsoft.com/windows-cssc/python3
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
CMD python ./app.py
