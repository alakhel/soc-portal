#!/bin/bash

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install nginx
sudo apt-get install mysql-server
sudo mysql_secure_installation
sudo apt update && sudo apt install -y software-properties-common 
sudo add-apt-repository ppa:ondrej/php 
sudo apt update
sudo apt-get install php8.1 php8.1-fpm php8.1-mysql php8.1-zip
sudo apt install curl
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo apt install git
sudo git clone https://github.com/alakhel/soc-portal /var/www/html/soc-portal
sed -i 's/web/localhost/' /var/www/html/soc-portal/nginx.conf
sudo cp /var/www/html/soc-portal/nginx.conf /etc/nginx/nginx.conf
sudo cp /var/www/html/soc-portal/nginx.conf /etc/nginx/sites-available/soc-portail/nginx.conf
sudo ln -s /etc/nginx/sites-available/soc-portal /etc/nginx/sites-enabled/
sudo nginx -t
