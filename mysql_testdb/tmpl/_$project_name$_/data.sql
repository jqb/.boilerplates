use _$project_name$_;


-- Data of "USERS"
insert into users values (1, "James");
insert into users values (2, "Agatha");
insert into users values (3, "Paul");
insert into users values (4, "Gabriel");

insert into tags values (1, "java");
insert into tags values (2, "C++");
insert into tags values (3, "python");
insert into tags values (4, "clojure");
insert into tags values (5, "scala");

-- Kuba
insert into user_tags values (1, 1);
insert into user_tags values (1, 2);
insert into user_tags values (1, 3);

-- Pavel
insert into user_tags values (3, 2);
insert into user_tags values (3, 5);
