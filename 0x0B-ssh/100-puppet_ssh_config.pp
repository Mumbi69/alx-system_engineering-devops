# set up your client SSH configuration file so that you can
# connect to a server without typing a password.
# Set up server configuration with puppet
file_line{'Set alias name':
  path => '/etc/ssh/ssh_config',
  line => 'Host localhost
    HostName localhost
    User ubuntu
    IdentityFile ~/.ssh/school
    PasswordAuthentication no',
}
