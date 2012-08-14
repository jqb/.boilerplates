drop database if exists _$project_name$_;
create database _$project_name$_;
use _$project_name$_;

create table users (
    id integer not null primary key,
    name varchar(100) not null
);

create table tags (
    id integer not null primary key,
    name varchar(50) not null unique
);

create table user_tags (
    user_id integer not null,
    tag_id integer not null,
    foreign key (user_id) REFERENCES users(id),
    foreign key (tag_id) REFERENCES tags(id)
);
