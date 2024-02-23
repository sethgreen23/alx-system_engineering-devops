file { 'school':
  path    => '/tmp/school',
  recurse => false,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
