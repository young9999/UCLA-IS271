/* Yang Guo

When running this .sql file, please input sqlite3 hw5.db, and then copy
all lines in this file and paste them into terminal.
*/

CREATE TABLE bands
(
id int,
name varchar(64),
PRIMARY KEY(id)
);

CREATE TABLE musicians
(
id int,
name varchar(64),
PRIMARY KEY(id)
);

CREATE TABLE members
(
band int,
musician int,
role varchar(64),
FOREIGN KEY(band) REFERENCES bands(id),
FOREIGN KEY(musician) REFERENCES musicians(id),
PRIMARY KEY(band, musician)
);

CREATE TABLE albums
(
id int,
title varchar(128),
year int,
band int,
PRIMARY KEY(id),
FOREIGN KEY(band) REFERENCES bands(id)
);

CREATE TABLE tracks
(
id int,
title varchar(128),
duration varchar(5),
album int,
PRIMARY KEY(id),
FOREIGN KEY(album) REFERENCES albums(id)
);

INSERT INTO bands (id, name) VALUES (1, "Queen");
INSERT INTO bands (id, name) VALUES (2, "Herb Alpert & the Tijuana Brass");
INSERT INTO bands (id, name) VALUES (3, "AC/DC");

INSERT INTO musicians (id, name) VALUES(1, "Feddie Mercury");
INSERT INTO musicians (id, name) VALUES(2, "Brian May");
INSERT INTO musicians (id, name) VALUES(3, "Roger Taylor");
INSERT INTO musicians (id, name) VALUES(4, "John Deacon");
INSERT INTO musicians (id, name) VALUES(5, "Herb Alpert");
INSERT INTO musicians (id, name) VALUES(6, "Bon Scott");
INSERT INTO musicians (id, name) VALUES(7, "Angus Young");
INSERT INTO musicians (id, name) VALUES(8, "Malcolm Young");
INSERT INTO musicians (id, name) VALUES(9, "Mark Evans");
INSERT INTO musicians (id, name) VALUES(10, "Phil Rudd");

INSERT INTO members (band, musician, role) VALUES (1,1,"vocals");
INSERT INTO members (band, musician, role) VALUES (1,2,"guitars");
INSERT INTO members (band, musician, role) VALUES (1,3,"drums");
INSERT INTO members (band, musician, role) VALUES (1,4,"bass");
INSERT INTO members (band, musician, role) VALUES (2,5,"vocals, trumpet");
INSERT INTO members (band, musician, role) VALUES (3,6,"vocals");
INSERT INTO members (band, musician, role) VALUES (3,7,"lead guitar");
INSERT INTO members (band, musician, role) VALUES (3,8,"rhythm guitar");
INSERT INTO members (band, musician, role) VALUES (3,9,"bass");
INSERT INTO members (band, musician, role) VALUES (3,10,"drums");

INSERT INTO albums (id, title, year, band) VALUES (1,"A Night at the Opera",1975,1);
INSERT INTO albums (id, title, year, band) VALUES (2,"Whipped Cream",1965,2);
INSERT INTO albums (id, title, year, band) VALUES (3,"Dirty Deeds Done Dirt Cheap",1976,3);

INSERT INTO tracks (id, title, duration, album) VALUES (1,"Death on Two Legs","3:43",1);
INSERT INTO tracks (id, title, duration, album) VALUES (2,"Lazing on a Sunday Afternoon","1:08",1);
INSERT INTO tracks (id, title, duration, album) VALUES (3,"I'm in Love with My Car","3:05",1);
INSERT INTO tracks (id, title, duration, album) VALUES (4,"You're My Best Friend","2:50",1);
INSERT INTO tracks (id, title, duration, album) VALUES (5,"'39","3:25",1);
INSERT INTO tracks (id, title, duration, album) VALUES (6,"Sweet Lady","4:01",1);
INSERT INTO tracks (id, title, duration, album) VALUES (7,"Seaside Rendezvous","2:13",1);
INSERT INTO tracks (id, title, duration, album) VALUES (8,"The Prophet's Song","8:17",1);
INSERT INTO tracks (id, title, duration, album) VALUES (9,"Love of My Life","3:38",1);
INSERT INTO tracks (id, title, duration, album) VALUES (10,"Good Company","3:26",1);
INSERT INTO tracks (id, title, duration, album) VALUES (11,"Bohemian Rhapsody","5:55",1);
INSERT INTO tracks (id, title, duration, album) VALUES (12,"God Save the Queen","1:11",1);

INSERT INTO tracks (id, title, duration, album) VALUES (13,"A Taste of Honey","2:43",2);
INSERT INTO tracks (id, title, duration, album) VALUES (14,"Green Peppers","1:31",2);
INSERT INTO tracks (id, title, duration, album) VALUES (15,"Tangerine","2:46",2);
INSERT INTO tracks (id, title, duration, album) VALUES (16,"Bittersweet Samba","1:46",2);
INSERT INTO tracks (id, title, duration, album) VALUES (17,"Lemon Tree","2:23",2);
INSERT INTO tracks (id, title, duration, album) VALUES (18,"Whipped Cream","2:33",2);
INSERT INTO tracks (id, title, duration, album) VALUES (19,"Love Potion No. 9","3:02",2);
INSERT INTO tracks (id, title, duration, album) VALUES (20,"El Garbanzo","2:13",2);
INSERT INTO tracks (id, title, duration, album) VALUES (21,"Ladyfingers","2:43",2);
INSERT INTO tracks (id, title, duration, album) VALUES (22,"Butterball","2:12",2);
INSERT INTO tracks (id, title, duration, album) VALUES (23,"Peanuts","2:09",2);
INSERT INTO tracks (id, title, duration, album) VALUES (24,"Lollipops and Roses","2:27",2);

INSERT INTO tracks (id, title, duration, album) VALUES (25,"Dirty Deeds Done Dirt Cheap","3:52",3);
INSERT INTO tracks (id, title, duration, album) VALUES (26,"Love at First Feel","3:12",3);
INSERT INTO tracks (id, title, duration, album) VALUES (27,"Big Balls","2:38",3);
INSERT INTO tracks (id, title, duration, album) VALUES (28,"Rocker","2:50",3);
INSERT INTO tracks (id, title, duration, album) VALUES (29,"Problem Child","5:46",3);
INSERT INTO tracks (id, title, duration, album) VALUES (30,"There's Gonna Be Some Rockin'","3:18",3);
INSERT INTO tracks (id, title, duration, album) VALUES (31,"Ain't No Fun (Waiting Round to Be a Millionaire)","6:54",3);
INSERT INTO tracks (id, title, duration, album) VALUES (32,"Ride On","5:53",3);
INSERT INTO tracks (id, title, duration, album) VALUES (33,"Squealer","5:27",3);

SELECT title FROM albums;
SELECT * FROM albums WHERE  year < 1970;
SELECT tracks.title, tracks.duration, albums.title FROM tracks INNER JOIN albums ON tracks.album = albums.id WHERE albums.title = "Whipped Cream";
SELECT musicians.name FROM musicians INNER JOIN members ON musicians.id = members.musician WHERE members.role ="drums";
SELECT musicians.name FROM musicians INNER JOIN members ON musicians.id = members.musician INNER JOIN bands ON bands.id = members.band WHERE bands.name = "AC/DC";


/*
DROP TABLE bands;
DROP TABLE musicians;
DROP TABLE members;
DROP TABLE albums;
DROP TABLE tracks;
*/
