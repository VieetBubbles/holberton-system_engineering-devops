# Client configuration file (w/ Puppet)
file_line { 'AddHug':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line { 'AddBug':
  ensure => 'present'
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}