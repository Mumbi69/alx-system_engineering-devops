# changed the ULIMIT to 4096
exec { 'update_nginx_config':
  command  => 'sed -i "s|ULIMIT=\"-n 15\"|ULIMIT=\"-n 10000\"|" /etc/default/nginx && service nginx restart',
  provider => 'shell',
}

