#fix the error that make Apache returning a 500 error

exec {'no_phpp':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
