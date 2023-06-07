FROM python
WORKDIR D:/College-Management/
COPY . .
RUN pip install -r Requirements.txt  
CMD [ "python", "Backend/app.py", "&", "python", "-m" ,"http.server" ]
EXPOSE 8080