# This manifest file create a file school in tmp folder with content I love Puppet
# persmittion '0744'
# ownder 'www-data'
# group 'www-data'

file { 'school':
  path    => '/tmp/school',
  recurse => false,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
