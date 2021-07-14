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
    longitude   float   not null,
    latitude    float   not null,
    primary key(point_number)
);