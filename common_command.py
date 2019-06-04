1. ubuntu 添加桌面快捷方式
#!/usr/bin/env xdg-open
    [Desktop Entry]
    Name=Sublime Text 3
    Comment=Sublime Text 3
    Exec=/usr/local/software/sublime/sublime_text
    Icon=/usr/local/software/sublime/Icon/48x48/sublime_text.png
    Terminal=false
    Type=Application
    Categories=Application;Development;
    StartupNotify=true


 2. mysql 查看数据库大小
	- 进入information_schema 数据库（存放了其他的数据库的信息）
		use information_schema;
	- 查询所有数据的大小：
		select concat(round(sum(data_length/1024/1024),2),'MB') as data from tables;
	- 查看指定数据库的大小：
		比如查看数据库home的大小
		select concat(round(sum(data_length/1024/1024),2),'MB') as data from tables where table_schema='home';
	- 查看指定数据库的某个表的大小
		比如查看数据库home中 members 表的大小
		select concat(round(sum(data_length/1024/1024),2),'MB') as data from tables where table_schema='home' and table_name='members';