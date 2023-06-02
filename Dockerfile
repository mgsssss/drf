FROM mysql:8.0

ENV MYSQL_USER admin
ENV MYSQL_PASSWORD 1234
ENV MYSQL_ROOT_PASSWORD qweqwe!@
ENV MYSQL_DATABASE service

VOLUME mysql:/var/lib/mysql
EXPOSE 3306


# docker image 만들기
# docker build -t mysql . 

# docker run
# name mydb
# port 3306
# -d 는 detached 모드 : 백그라운드에서 실행
# docker run --name mydb -p 3306:3306 -d mysql