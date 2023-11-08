# Using tmux with strace to debug apache server
exec { 'debug apache':
  command  => 'grep -rl class-wp-locale.phpp *',
  path     => '/var/www/html/wp-settings.php'
}

