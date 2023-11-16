# Giving access to holberton user
exec { 'update_limits_conf':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/; s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf',
  provider => 'shell',
}

