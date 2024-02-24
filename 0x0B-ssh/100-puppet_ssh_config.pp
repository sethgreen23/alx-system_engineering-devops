# use private key ~/.ssh/school
# refuse to authonticate using a password

file_line { 'use private key':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => 'IdentityFile ~/.ssh/school'
}

file_line { 'refuse authontication using password':
  ensure => present,
  path   => '/etc/ssh/ssh_config'
  line   => 'PasswordAuthentication no'
}
