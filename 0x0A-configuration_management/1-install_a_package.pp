# using puppet install flask and pip3

package { 'python3-pip':
  ensure => 'installed',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}
