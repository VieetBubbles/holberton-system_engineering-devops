# Use Puppet to install Nginx
exec {'bin/bash/env apt get update':}
exec {'bin/bash/env apt-get -y install nginx':}
exec {'bin/bash/env ufw allow "Nginx HTTP"':}
exec {'bin/bash/env echo "Holberton School" > /var/www/html/index.nginx-debian.html':}
exec {'bin/bash/env sed -i "/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default':}
exec {'bin/bash/env service nginx restart':}