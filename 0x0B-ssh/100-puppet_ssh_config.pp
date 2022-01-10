# set up your client SSH configuration file so that you can connect to a server without typing a password but with private key in filr ~/.ssh/school
include stdlib
file_line { 'Use Private key':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school'
}

file_line { 'TURN OFF Passwd auth':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no'
}

