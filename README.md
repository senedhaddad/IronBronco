pip3 install flask \
pip3 install flask_bootstrap \
pip3 install flask_wtf \
pip3 install flask_sqlalchemy \
pip3 install flask_login \
\
#For database: \
pip install flask_script \
pip install flask_migrate \
pip install psycopg2-binary \
\
python manage.py db init \
python manage.py db migrate \
python manage.py db upgrade \
\
#To run program \
python3 app.py db init \
\
https://medium.com/@dushan14/create-a-web-application-with-python-flask-postgresql-and-deploy-on-heroku-243d548335cc