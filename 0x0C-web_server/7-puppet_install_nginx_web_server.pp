# Use Puppet to install Nginx
exec {'bin/bash/env apt get update apt-get -y install nginx ufw allow Nginx HTTP echo "Holberton School" > /var/www/html/index.nginx-debian.html sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default service nginx restart':
}