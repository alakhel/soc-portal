# Use the official PHP image with FPM
FROM php:8.1-fpm

# Copy the contents of the Laravel project to the image
COPY . /var/www/html/

# Set the working directory to the root of the Laravel project
WORKDIR /var/www/html/

# Install dependencies for Laravel and the Vue frontend
RUN apt-get update && apt-get install -y \
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
