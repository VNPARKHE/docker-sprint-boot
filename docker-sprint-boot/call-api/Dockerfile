FROM python:3-onbuild
COPY . /usr/src/app
RUN pip install requests
EXPOSE 8090
CMD ["python", "/usr/src/app/call-api.py"]