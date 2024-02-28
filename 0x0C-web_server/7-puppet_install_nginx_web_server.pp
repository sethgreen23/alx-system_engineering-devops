# install nginx and 
# return string "Hello World!" when quering the root
# rediretion must be a "301" move permanentyly

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file_line { 'rewrite redirect'
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'listen 80 default_server;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4;',
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}
