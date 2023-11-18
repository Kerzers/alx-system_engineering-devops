# Fix the limit of request to have 0 request failed

exec {'fix':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/" /etc/default/nginx && sudo service nginx restart',
}
