# Ansible playbooks for SysAdmin 2022

## Playbooks

```text
├── handlers
│   └── main.yml
├── inventory
│   ├── hosts
│   └── hosts-exam
├── playbook.yml
├── README.md
└── roles
    ├── 02-etais
    │   └── tasks
    │       └── main.yml
    ├── 04-dns
    │   ├── files
    │   │   └── 70-ipv6.conf
    │   ├── handlers
    │   │   └── main.yml
    │   ├── tasks
    │   │   └── main.yml
    │   └── templates
    │       ├── hostname.j2
    │       ├── hosts.j2
    │       ├── named.conf.j2
    │       ├── resolv.conf.j2
    │       ├── reverse_zone.j2
    │       └── zone_file.j2
    ├── 05-web-apache
    │   ├── files
    │   │   ├── modsecurity_localrules.conf
    │   │   ├── php-fpm.conf
    │   │   ├── proxy.service
    │   │   ├── website.py
    │   │   └── www.conf
    │   ├── handlers
    │   │   └── main.yml
    │   ├── tasks
    │   │   └── main.yml
    │   └── templates
    │       ├── apache_virtual_host.j2
    │       ├── index.j2
    │       ├── proxy_virtual_host.j2
    │       └── wordpress_virtual_host.j2
    ├── 06-email-smtp-imap
    │   ├── files
    │   │   ├── 10-auth.conf
    │   │   ├── 10-logging.conf
    │   │   ├── 10-mail.conf
    │   │   ├── 10-master.conf
    │   │   ├── 10-ssl.conf
    │   │   ├── 15-mailboxes.conf
    │   │   ├── dovecot.conf
    │   │   └── master.cf
    │   ├── handlers
    │   │   └── main.yml
    │   ├── tasks
    │   │   └── main.yml
    │   └── templates
    │       ├── config.inc.php.j2
    │       ├── main.cf.j2
    │       ├── roundcube_web_server_config.j2
    │       └── zone_file.j2
    ├── 07-tls
    │   ├── files
    │   │   ├── 10-ssl.conf
    │   │   ├── cacert.crt
    │   │   ├── master.cf
    │   │   ├── server.crt
    │   │   └── server.key
    │   ├── handlers
    │   │   └── main.yml
    │   ├── tasks
    │   │   └── main.yml
    │   └── templates
    │       ├── apache_virtual_host.j2
    │       ├── main.cf.j2
    │       ├── proxy_virtual_host.j2
    │       └── wordpress_virtual_host.j2
    ├── 08-filesystems
    │   ├── files
    │   │   └── smb.conf
    │   ├── handlers
    │   │   └── main.yml
    │   └── tasks
    │       └── main.yml
    ├── 09a-containers
    │   ├── files
    │   │   ├── Dockerfile
    │   │   └── server.py
    │   ├── handlers
    │   │   └── main.yml
    │   ├── tasks
    │   │   └── main.yml
    │   └── templates
    │       └── proxy_virtual_host.j2
    ├── 09-containers
    │   ├── files
    │   │   └── daemon.json
    │   └── tasks
    │       └── main.yml
    ├── 10-devops
    │   ├── files
    │   │   └── traefik.toml
    │   ├── handlers
    │   │   └── main.yml
    │   └── tasks
    │       └── main.yml
    ├── 11a-k8s-nonidempotent
    │   └── tasks
    │       └── main.yml
    ├── 11-k8s-idempotent
    │   ├── files
    │   │   └── traefik-config.yml
    │   ├── handlers
    │   │   └── main.yml
    │   └── tasks
    │       └── main.yml

57 directories, 58 files
```
