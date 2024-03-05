# Ensure nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Configure nginx root page
file { '/var/www/html/index.nginx-debian.html':
  ensure  => present,
  content => "Hello World!\n",
}

# Configure redirect_me
file { '/etc/nginx/sites-enabled/default':
  ensure  => present,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301 http://youtube.com;
    }

    # Other location directives if needed
}
",
}

# Configure custom 404 page
file { '/usr/share/nginx/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page\n",
}

# Add custom HTTP response header to nginx.conf
file_line { 'custom_header_nginx_conf':
  ensure => present,
  line   => '    add_header X-Served-By $HOSTNAME;',
  path   => '/etc/nginx/nginx.conf',
  match  => '^http {',
}

# Add custom HTTP response header to default site configuration
file_line { 'custom_header_default_conf':
  ensure => present,
  line   => '    add_header X-Served-By $HOSTNAME;',
  path   => '/etc/nginx/sites-enabled/default',
  match  => '^server {',
}

# Restart nginx service
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => [File['/etc/nginx/nginx.conf'], File['/etc/nginx/sites-enabled/default']],
}

