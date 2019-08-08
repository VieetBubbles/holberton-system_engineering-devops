# Use Puppet to install Nginx
exec {'bin/bash/env apt get update apt-get -y install nginx ufw allow Nginx HTTP echo "Holberton School" > /var/www/html/index.nginx-debian.html service nginx restart':
}