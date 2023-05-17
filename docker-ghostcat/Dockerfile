# 베이스 이미지
FROM tomcat:9.0.29-jdk8-openjdk
# MariaDB 설치
RUN echo "deb http://archive.debian.org/debian stretch main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y mariadb-server
RUN service mysql start
# JDBC 드라이버 다운로드 및 설치
ADD https://repo1.maven.org/maven2/org/mariadb/jdbc/mariadb-java-client/2.7.2/mariadb-java-client-2.7.2.jar /usr/local/tomcat/lib/
# 데이터베이스 초기화 스크립트 추가
COPY init.sql /docker-entrypoint-initdb.d/
# JSP 파일 추가
COPY index.jsp /usr/local/tomcat/webapps/ROOT/
# 포트 포워딩
EXPOSE 8080
# 컨테이너 실행 시 실행될 명령어
CMD ["catalina.sh", "run"]
