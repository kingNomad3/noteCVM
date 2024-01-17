SET GLOBAL time_zone = '-5:00';

create database db_memo character set utf8 collate utf8_general_ci;

create user memo_user@'localhost' identified by 'AAAaaa111';
grant all on db_memo.* to memo_user@'localhost';

DROP TABLE category;
use db_memo;

CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(40),
    password VARCHAR(255),
    PRIMARY KEY (id)
) ENGINE=InnoDB;

CREATE TABLE category (
    id INT NOT NULL AUTO_INCREMENT,
    id_user INT,
    name VARCHAR(255),
    FOREIGN KEY (id_user) REFERENCES users(id),
    PRIMARY KEY (id),
	UNIQUE INDEX idx_category_name (name)
	UNIQUE INDEX uk_user_name (id_user, name)
) ENGINE=InnoDB;


create table memo(
    id int not null auto_increment,
    id_category int,
    memo TEXT,
    created timestamp,
    foreign key (id_category) references category(id),
    primary key pk_memo(id)
) engine=InnoDB;

select * from memo;

CREATE UNIQUE INDEX uk_user_name on category(id_user,name)





