# Client configuration file (w/ Puppet)
file_line { 'AddHug':
  path => '/etc/ssh/ssh_config',
  line => HostName 34.73.32.179
}

file_line { 'AddBug':
  path => '/etc/ssh/ssh_config',
  line => User ubuntu
}