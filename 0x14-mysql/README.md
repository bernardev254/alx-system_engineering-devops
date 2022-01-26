# 0x14-mysql

##task 0
install mysql v5.7.37 on web-01 and web-02 servers
sudo apt update
wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
sudo apt update
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
sudo apt update
sudo apt-cache policy mysql-server
sudo apt install -f mysql-community-client=5.7.37-1ubuntu18.04
sudo apt install -f mysql-community-server=5.7.37-1ubuntu18.04
sudo apt install mysql-server

##task 1
create user
grant permissions

