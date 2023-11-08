# Using tmux with strace to debug apache server
exec { 'debug_apache':
        command  => 'grep -q 'phpp' /var/www/html/wp-settings.php',
}
