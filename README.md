# python-microservice
Web app microservice built using React, Django and Flask using this <a href="https://www.youtube.com/watch?v=0iB5IPoTDts&pp=ygUUcHl0aG9uIG1pY3Jvc2VydmljZXM%3D">video</a> by Freecodecamp

Tech stack:

Python, REACT, Docker, RabbitMQ, Flask, Django

## Changes made:


## Issues:

- needed to install Docker and upgrade WSL

- had to use this command to create mysql db within docker -> command: --innodb_use_native_aio=0

- to fix mysql module error  -> pip install mysqlclient 

- if run into wsl error with docker use in cmd as admin -> sc config LxssManager start=auto

- WITH DOCKER DO NOT ACCEPT POPUP FROM KASPERSKY ABOUT LINUX NAME ERROR AS IT WILL PREVENT WSL AND DOCKER RUNNING


## Resources used:

https://www.youtube.com/watch?v=0iB5IPoTDts&pp=ygUUcHl0aG9uIG1pY3Jvc2VydmljZXM%3D

Original repos -> https://github.com/scalablescripts/python-microservices

https://github.com/scalablescripts/react-crud

https://www.toptal.com/developers/gitignore/

https://www.w3schools.com/django/django_install_django.php

https://www.django-rest-framework.org/

https://www.youtube.com/watch?v=pg19Z8LL06w

https://stackoverflow.com/questions/50222972/docker-compose-not-finding-my-files

https://stackoverflow.com/questions/76103836/docker-compose-is-not-a-docker-command-under-windows-10-but-docker-cli-is-w

https://www.geeksforgeeks.org/how-to-install-docker-on-windows/

https://stackoverflow.com/questions/49958895/how-to-set-up-docker-compose-to-initialize-mysql-database-on-windows-10

https://stackoverflow.com/questions/15312732/django-core-exceptions-improperlyconfigured-error-loading-mysqldb-module-no-mo

https://www.tutorialspoint.com/how-do-i-install-mysqldb-in-python

https://pypi.org/project/django-cors-headers/

https://stackoverflow.com/questions/54030469/host-x-is-not-allowed-to-connect-to-this-mysql-server

https://stackoverflow.com/questions/65369567/import-rest-framework-could-not-be-resolved-but-i-have-installed-djangorestfr

https://stackoverflow.com/questions/65583150/wsl-set-default-version-2-the-service-cannot-be-started-either-because-it-is

https://github.com/Microsoft/WSL/issues/3815

https://pypi.org/project/Flask-Cors/1.10.3/

https://stackoverflow.com/questions/68527489/cant-import-migratecommand-from-flask-migrate

https://www.cloudamqp.com/