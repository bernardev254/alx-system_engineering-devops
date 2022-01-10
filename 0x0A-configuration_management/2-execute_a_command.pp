# create a manifest that kills a process named killmenow
exec {'kill':
    path    => ['/usr/bin'],
    command => 'pkill -f killmenow'
}

