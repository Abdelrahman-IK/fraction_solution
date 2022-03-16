FROM postgres:latest
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_USER=user
ENV POSTGRES_DB=postgres
COPY schema.sql /docker-entrypoint-initdb.d/schema.sql