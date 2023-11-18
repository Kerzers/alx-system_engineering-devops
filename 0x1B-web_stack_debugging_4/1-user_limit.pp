# fix the user files limit

exec {'replace':
  provider => shell,
  command  => "sudo sed -i 's/nofile 5/nofile unlimited/; s/nofile 4/nofile unlimited/' /etc/security/limits.conf"
}
