# Using tmux with strace to debug apache server
exec { 'debug_apache':
        command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
