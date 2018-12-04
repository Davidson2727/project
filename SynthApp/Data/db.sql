CREATE TABLE user (userId VARCHAR(255) NOT NULL,
   userName varchar(255) NOT NULL,
   uPassword varchar(255) NOT NULL,
   email varchar(255) NOT NULL,
   PRIMARY KEY (userId));

CREATE TABLE file (userId varchar(255) NOT NULL,
   userName varchar(255) NOT NULL,
   fileName varchar(255) Not Null,
   createDate varchar(255) NOT NULL,
   type varchar(255) NOT NULL,
   contents varchar(1000) Not NULL,
   activeStatus varchar(255) NOT NULL,
   FOREIGN KEY (userId) REFERENCES user(userId)
   ON DELETE CASCADE);
