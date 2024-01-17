SET GLOBAL time_zone = '-5:00';

drop database bd_jumper;

CREATE DATABASE bd_jumper CHARACTER SET utf8 COLLATE utf8_general_ci;

CREATE USER jumper_user@'localhost' IDENTIFIED BY 'AAAaaa111';
 
GRANT ALL ON bd_jumper.* TO jumper_user@'localhost';

use bd_jumper;

Create table game_logs(
	id int NOT NULL auto_increment,
    playername  VARCHAR(40),
    score INT,
	primary key pk_game_logs(id)
)ENGINE=InnoDB;

create index idx_game_logs_score on game_logs(score);

