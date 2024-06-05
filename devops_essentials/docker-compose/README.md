Background
Docker Compose is a tool for defining and running multi-container Docker applications. For this exercise, students will work with PostgreSQL, a powerful open-source relational database, and pgAdmin, a popular open-source administration and management tool for the PostgreSQL database.

Objective
Define two services in a Docker Compose YAML file:

PostgreSQL: A relational database management system.
pgAdmin: A web-based administration tool for PostgreSQL.
The main goals are:

Set up a private network that both containers will use.
Allow public access only from the pgAdmin container.
Ensure pgAdmin can connect and manage the PostgreSQL database.
Explicitly configure the dependency between services, so the PostgreSQL container always starts before pgAdmin.
Resources:
Docker Compose documentation: https://docs.docker.com/compose/
PostgreSQL Docker image documentation: https://hub.docker.com/_/postgres
pgAdmin Docker image documentation: https://hub.docker.com/r/dpage/pgadmin4/
Instructions:
Setup:

Ensure Docker and Docker Compose are installed on your machine.
Create a new directory for this project: mkdir docker-pg-setup && cd docker-pg-setup
PostgreSQL:

You will be using the official Docker image for PostgreSQL. Make sure you understand the required environment variables to initialize a new database.
pgAdmin:

Similarly, you will use the official Docker image for pgAdmin. Understand how to configure the pgAdmin service to connect to the PostgreSQL instance.
Docker Compose:

In the root of your project directory, create a docker-compose.yml file.
Define two services: db and admin.
For the db service:
Use the official PostgreSQL Docker image.
Configure environment variables as necessary for initial setup.
Ensure the service is part of the private network.
For the admin service:
Use the official pgAdmin Docker image.
Set up necessary environment variables or configurations to ensure pgAdmin can connect to PostgreSQL.
Ensure the service is part of the private network.
Ensure this service depends on the db service using the depends_on field.
Define a custom private network and assign it to both services.
Make sure to expose only the necessary port(s) for pgAdmin to allow public access.
Execution:

Run the Docker Compose setup with: docker-compose up
Access pgAdmin via your browser on the exposed port. You should be able to connect and manage the PostgreSQL instance using the credentials provided in the Docker Compose file.
Notes:

Use Docker’s networking and service dependency features to make sure the two containers can communicate and that they start in the right order.
Make sure to handle potential database authentication issues, especially when setting up the pgAdmin connection to PostgreSQL.
Hints:

PostgreSQL default port is 5432, so ensure your pgAdmin configuration targets this port for database operations within the private network.
Remember to specify a volume for PostgreSQL if you want the data to persist across container restarts.
Look into Docker’s networks configuration for creating a private network.
