CREATE TABLE users (u_id varchar(255) NOT NULL, u_name varchar(255) NOT NULL, u_pass varchar(255) NOT NULL, email varchar(255) NOT NULL, PRIMARY KEY (u_id));

CREATE TABLE profiles(u_id varchar(255) NOT NULL, FOREIGN KEY (u_id) REFERENCES users(u_id));
