FROM mysql:8.0

ENV MYSQL_USER admin
ENV MYSQL_PASSWORD 1234
ENV MYSQL_ROOT_PASSWORD qweqwe!@
ENV MYSQL_DATABASE service

VOLUME mysql:/var/lib/mysql
EXPOSE 3306

# docker build -t mysql .
# docker run --name mydb -p 3306:3306 -d mysql