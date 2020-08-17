#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

location="        location \/hbnb_static/ { alias /data/web_static/current/; }"

if ! which nginx > /dev/null 2>&1; then
    sudo apt update && sudo apt-get install -y nginx
fi

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html

if [ -d "data/web_static/releases" ]; then
     cp /data/web_static/releases/test/index.html .
     rm -r /data/web_static/releases/test/
     mkdir -p /data/web_static/releases/test/
     mv index.html /data/web_static/releases/test/
fi

echo "$content" > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/current /data/web_static/releases/test/
chown -R ubuntu /data/ && chgrp -R ubuntu /data/

sudo sed -i "55 i\ $location" /etc/nginx/sites-available/default
# restart nginx
sudo service nginx start
