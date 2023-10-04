# Ensure Nginx is installed
package { 'nginx':
  ensure => 'installed',
}

# Define a custom fact to get the server's hostname
Facter.add('server_hostname') do
  setcode 'hostname'
}

# Create a custom Nginx configuration file
file { '/etc/nginx/conf.d/custom_header.conf':
  ensure  => 'present',
  content => "add_header X-Served-By $server_hostname;\n",
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/conf.d/custom_header.conf'],
}
