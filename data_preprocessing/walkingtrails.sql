create table walkingtrails(
    category    varchar(50),
    region  varchar(50),
    distance    varchar(50),
    time_required   varchar(50),
    _level  int,
    subway  varchar(255),
    Transportation  varchar(5000),
    course_name varchar(255),
    course_detail   varchar(5000),
    _explain varchar(5000),
    point_number    int not null,
    point_name  varchar(255) not null,
    longitude   decimal(17,14)   not null,
    latitude    decimal(16,14)   not null,
    primary key(point_number)
);

-- load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/road_final.csv'
load data infile '/var/lib/mysql-files/road_final.csv'
load data infile '/var/lib/mysql-files/road_final.csv'
into table walkingtrails
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;