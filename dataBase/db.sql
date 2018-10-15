CREATE TABLE users (userId int NOT NULL AUTO_INCREMENT,
   userName varchar(255) NOT NULL,
   password varchar(255) NOT NULL,
   email varchar(255) NOT NULL,
   PRIMARY KEY (userId));

CREATE TABLE profiles(userId int NOT NULL,
  FOREIGN KEY (userId) REFERENCES users(userId));
