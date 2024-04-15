# fix holberton user

exec { 'change-os-configuration-for-holberton-user':

command => '/bin/sed -r -i "s/holberton\s+(hard|soft)\s+nofile\s+[0-9]+/holberton\t\1\tnofile\t750/g" /etc/security/limits.conf',

}
