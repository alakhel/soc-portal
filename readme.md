## Update your server:
```
sudo apt-get update
sudo apt-get upgrade
```

## Install Nginx:
```
sudo apt-get install nginx
```

## Install MySQL:
```
sudo apt-get install mysql-server
```

## Secure your MySQL installation (follow the prompts):
```
sudo mysql_secure_installation
```

## Install PHP and required PHP extensions:
```
sudo apt-get install php8.1 php8.1-fpm php8.1-mysql php8.1-zip
```

## Install Node.js and npm:
```
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Clone or copy your Laravel project to the server:
```
# If using Git, for example:
git clone https://your-repository-url /var/www/html/your-project-name
```

## Configure Nginx:
Copy the Nginx configuration from your Docker setup to /etc/nginx/sites-available/your-project-name (create a new file).

### Create a symbolic link to the sites-enabled directory:
```
sudo ln -s /etc/nginx/sites-available/your-project-name /etc/nginx/sites-enabled/
```

### Test the Nginx configuration:
```
sudo nginx -t
```

### Reload Nginx:
```
sudo systemctl reload nginx
```

## Configure MySQL:
### Log in to MySQL:
```
sudo mysql -u root -p
```

Create a database and user for your Laravel project (replace your_database_name, your_user_name, and your_password with your desired values):
```
CREATE DATABASE your_database_name;
CREATE USER 'your_user_name'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_user_name'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

## Configure your Laravel project:
Copy .env.example to .env and update the necessary values (e.g., database credentials).
```
cd /var/www/html/your-project-name
cp .env.example .env
```

## Install the Composer dependencies:
```
composer install
```

### Generate an application key:
```
php artisan key:generate
```

### Run any necessary migrations:
```
php artisan migrate
```
## Install npm dependencies for the Vue frontend:
```
cd /var/www/html/your-project-name/frontend-vue
npm install
```

### Build the Vue frontend:
```
npm run build
```

### Update permissions for the storage directory:
```
sudo chown -R www-data:www-data /var/www/html/your-project-name/storage
sudo chmod -R 755 /var/www/html/your-project-name/storage
```

## Restart Nginx and PHP-FPM:
```
sudo systemctl restart nginx
sudo systemctl restart php8.1-fpm
```