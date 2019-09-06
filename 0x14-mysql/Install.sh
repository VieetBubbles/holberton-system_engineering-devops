# Do not execute file
# this is just the list of statements I used to install mysql into erb serveer 1 and 2
# follow the steps

# Web server 1
sudo apt-get install mysql-server-5.7
sudo service mysql restart
mysql -u root -p
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON * . * TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

show databases;
CREATE DATABASE [IF NOT EXISTS] tyrell_corp;
show databases;
use tyrell_corp;

show tables;
CREATE TABLE IF NOT EXISTS nexus6(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);
show tables;
describe nexus6;

INSERT INTO nexus6(name) VALUES('Leon');

select * from nexus6;
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT REPLICATION SLAVE ON * . * TO 'replica_user'@'%';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

#outside mysql for primary
sudo emacs /etc/mysql/mysql.conf.d/mysqld.cnf
#place inside web-01 and comment out/ do comment bind-address
[mysqld]
server-id  = 1
log_bin        = /var/log/mysql/mysql-bin.log
binlog_do_db  = tyrell_corp

#in web-01 not in web-01 mysql
mysqldump -u root -p --opt tyrell_corp > tyrell_corp.sql
#in terminal
sudo service mysql restart

#log in to web-02 server
#enter mysql
CREATE DATABASE tyrell_corp;
EXIT;

#outside web-02 in terminal use 0-transfer_file from 0x0C-web-ser to transfer tyrell_corp.sql

#outside mysql for replica
sudo emacs /etc/mysql/mysql.conf.d/mysqld.cnf
#place inside web-02 and comment out/ do comment bind-address
[mysqld]
server-id  = 2
relay-log  = /var/log/mysql/mysql-relay-bin.log
log_bin        = /var/log/mysql/mysql-bin.log
binlog_do_db   = tyrell_corp

#in terminal
sudo service mysql restart

#move to web-01 and do:
mysql> show master status;

#in mysql MASTER_HOST='WEB-01' MASTER_LOG_FILE='master status mysql-bin.00000_ number'
CHANGE MASTER TO MASTER_HOST='34.73.32.179', MASTER_USER='replica_user', MASTER_PASSWORD='root', MASTER_LOG_FILE='mysql-bin.000005', MASTER_LOG_POS=  154;

START SLAVE;

SHOW SLAVE STATUS\G

#if you messed up in slave-connection do:
stop slave;
RESET SLAVE ALL;

# repeat change master if you reseted
# make sure to change mysql-bin.000000 number if you reset because it increments by 1 each resert
