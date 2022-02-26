# Backbone File Server
This project is a simple HTTP file server for upload and downloading Iso files which has been developed with Django.

Here are Django commands to create this project:
~~~~
python -m pip install django 
django-admin startproject fileServer
~~~~

This project has been dockerized so there are some environment varibles for more security and flexebility:
`DJANGO_SECRET_KEY` : to generate this key follow steps below:
* Install Django either in a virtual environment or in your operating system.
* Do following steps:
  * python
  * from django.core.management.utils import get_random_secret_key
  * get_random_secret_key()


`DJANGO_DEBUG`: Define debug mode which could be `true` or `false`. Default value is `false`.

`DB_NAME`: Name of the postgresql database.

`DB_NAME`: Database username.

`DB_PASSWORD`: Database password

`DB_HOST`: Database host

`DB_PORT`: Database port. Default value is `5432`.

Uploaded Iso files are placed in `/file-server/iso/media` directory inside container. A PVC with `ReadWriteMany` access mode is mounted on `/file-server/iso/media` to store Iso files permanently and also Nginx uses this PVC to allow users download what they need. Static files are also in `/file-server/static` inside file server container. 

For better performance Gunicorn is also used in this project to handle request that recieves from Nginx. Nginx is used for authenticating users.

Despite web panel which can be used either for upload, download and deleting Iso file, it is possible to use `curl` command for uploading. Here is a sample command:
~~~~
curl --user username:password -F title=<visible name> -F file=@<iso file> http://yourdomain.com/media/qcow/upload/
~~~~


