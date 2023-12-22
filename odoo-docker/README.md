# Odoo 13 Docker

Clone specific odoo version
```
$ git clone https://github.com/odoo/odoo.git -b 13.0 --depth 1
```

To connect with PgAdmin4
```
$ docker inspect ee9183bfc06e
```

File mode change push

then with ```vim .git/config```, set ```filemode``` option to ```false```
```
[core]
        filemode = false
```

Change permission
```
$ chown -R $(whoami) addons/
$ chown -R $(whoami) config/
$ export GID=${GID}
```

**Logs without odoo.conf**:
```
Attaching to odoo-11-docker_db_1, odoo-11-docker_web_1
db_1   | 
db_1   | PostgreSQL Database directory appears to contain a database; Skipping initialization
db_1   | 
db_1   | 2020-08-27 05:23:26.230 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
db_1   | 2020-08-27 05:23:26.230 UTC [1] LOG:  listening on IPv6 address "::", port 5432
db_1   | 2020-08-27 05:23:26.332 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
db_1   | 2020-08-27 05:23:26.682 UTC [25] LOG:  database system was shut down at 2020-08-27 05:23:08 UTC
db_1   | 2020-08-27 05:23:26.958 UTC [1] LOG:  database system is ready to accept connections
web_1  | grep: /etc/odoo/odoo.conf: No such file or directory
web_1  | grep: /etc/odoo/odoo.conf: No such file or directory
web_1  | grep: /etc/odoo/odoo.conf: No such file or directory
web_1  | grep: /etc/odoo/odoo.conf: No such file or directory
web_1  | 2020-08-27 05:23:34,520 1 INFO ? odoo: Odoo version 11.0-20200826
web_1  | 2020-08-27 05:23:34,522 1 INFO ? odoo: addons paths: ['/var/lib/odoo/.local/share/Odoo/addons/11.0', '/usr/lib/python3/dist-packages/odoo/addons']
web_1  | 2020-08-27 05:23:34,523 1 INFO ? odoo: database: odoo@db:5432
web_1  | 2020-08-27 05:23:34,814 1 INFO ? odoo.service.server: HTTP service (werkzeug) running on a087322baa2b:8069
web_1  | 2020-08-27 05:23:35,871 1 INFO ? odoo.addons.base.ir.ir_actions_report: Will use the Wkhtmltopdf binary at /usr/local/bin/wkhtmltopdf
```

Enter into container
```
$ docker exec -it container_id bash
```