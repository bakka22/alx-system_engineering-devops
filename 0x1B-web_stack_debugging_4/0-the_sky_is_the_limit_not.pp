# fix nginx

exec {'fix--for-nginx':

command => "/bin/sed -i 's/15/500/g' /etc/default/nginx && /usr/sbin/service nginx restart",

}
