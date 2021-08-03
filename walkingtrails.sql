-- db생성
create database walkdb;

-- 유저(npnc) 생성 및 권한부여
create user npnc@'%' identified by 'npnc';
grant all privileges on walkdb.* to npnc@'%' with grant option;
flush privileges;

-- 산책로 테이블 (walkingtrails) 관련
-- walkingtrails 테이블 추가
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

-- road_final 을 walkingtrails에 추가
-- 해당 경로에 road_final.csv 넣고 아래 쿼리문 입력하면 됨
load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/road_final.csv'
into table walkingtrails
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;

-- windows 환경이 아닌 교수님 서버 환경에서 데이터 추가할 때
load data infile '/var/lib/mysql-files/road_final.csv'
into table walkingtrails
fields terminated by ','
enclosed by '"'
lines terminated by '\n'
ignore 1 rows;