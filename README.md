# Flask_website
Creating a small website using flask . The database setup ( SQL Lite and Postgresql) . Hashing Algorithm as werkzueg . Including the Authorization and logging .  





$ sudo curl https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo apt-key add



$ sudo sh -c 'echo "deb https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/$(lsb_release -cs) pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'


$ sudo apt install pgadmin4


$ sudo /usr/pgadmin4/bin/setup-web.sh








$ sudo service postgresql-9.3 initdb


$ sudo apt-get install wget ca-certificates


$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -


$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ 'lsb_release -cs'-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
-cs-pgdg main" >> /etc/apt/sources.list.d/pgdg.list: 1: -cs-pgdg main" >> /etc/apt/sources.list.d/pgdg.list: Syntax error: Unterminated quoted string


$ sudo apt update


$ sudo apt install postgresql postgresql-contrib


$ sudo -i -u postgres






postgres@maanzai-H470-HD3:~$ psql


postgres=# ALTER USER postgres PASSWORD 'myPassword';


postgres=# SHOW data_directory;


root@maanzai-H470-HD3:/var/lib/postgresql/10/main#



http://127.0.0.1/pgadmin4/browser/


#LInks
https://stackoverflow.com/questions/43657126/flask-alchemy-psycopg2-operationalerror-fatal-password-authentication-fai

https://blog.theodo.com/2017/03/developping-a-flask-web-app-with-a-postresql-database-making-all-the-possible-errors/

https://postgresapp.com/documentation/configuration-python.html

#Best for installation

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

https://phoenixnap.com/kb/how-to-install-postgresql-on-ubuntu


