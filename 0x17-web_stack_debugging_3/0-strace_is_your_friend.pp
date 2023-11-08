# Using tmux with strace to debug apache server
exec { 'debug_apache':
        command  => 'grep -rl 'phpp' /var/www/html/wp-settings.php',
}
