FROM mcr.microsoft.com/windows/servercore:ltsc2019
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
CMD python ./app.py
