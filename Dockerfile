# Use the official PHP image with FPM
FROM php:8.1-fpm

# Add the Nginx repository
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && wget https://nginx.org/keys/nginx_signing.key \
    && apt-key add nginx_signing.key \
    && echo "deb http://nginx.org/packages/mainline/debian/ $(lsb_release -cs) nginx" | tee /etc/apt/sources.list.d/nginx.list

# Copy the contents of the Laravel project to the image
COPY . /var/www/html/

# Copy the Nginx configuration file for Laravel
COPY laravel-nginx.conf /etc/nginx/conf.d/default.conf

# Set the working directory to the root of the Laravel project
WORKDIR /var/www/html/

# Install dependencies for Laravel and the Vue frontend
RUN apt-get update && apt-get install -y \
    nginx \
    npm \
    libzip-dev \
    && docker-php-ext-install zip \
    && rm -rf /var/lib/apt/lists/*

# Install the necessary PHP extensions for Laravel
RUN docker-php-ext-install pdo_mysql

# Install the npm dependencies for the Vue frontend
WORKDIR /var/www/html/frontend-vue
RUN npm install

# Build the Vue frontend
RUN npm run build

# Set the working directory back to the root of the Laravel project
WORKDIR /var/www/html/

# Update permissions for the storage directory
RUN chown -R www-data:www-data /var/www/html/storage \
    && chmod -R 755 /var/www/html/storage
# Add this line after the other COPY and RUN commands
COPY ./www.conf /usr/local/etc/php-fpm.d/www.conf

# Start Nginx and PHP-FPM
CMD ["sh", "-c", "service nginx start; php-fpm"]
