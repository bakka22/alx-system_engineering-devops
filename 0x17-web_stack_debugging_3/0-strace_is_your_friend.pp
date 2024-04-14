# fix wp-settings.php

exec {'fix-wordpress':

command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php && /usr/bin/service apache2 restart",

}
