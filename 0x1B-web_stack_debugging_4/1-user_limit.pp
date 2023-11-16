# Giving access to holberton user
exec { 'update_hard_limits_conf':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 4096/" /etc/security/limits.conf',
  provider => 'shell',
}
exec { 'update_soft_limits_conf':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4096/" /etc/security/limits.conf',
  provider => 'shell'
}

