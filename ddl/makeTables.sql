use thriftley_db;

drop table if exists user;
create table user (
   uid int NOT NULL AUTO_INCREMENT,
   email varchar(30),
   name varchar(30),
   password varchar(30),
   primary key (uid)
   );


drop table if exists post;
create table post (
   post_id int NOT NULL AUTO_INCREMENT,
   date_posted TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
   title varchar(30),
   price DECIMAL(19,4),
   details varchar(50),
   image varchar(50),
   delivery_method enum('delivery','pickup'),
   category enum('furniture','jewelry','books','clothes','other'),
   post_status enum('available','sold') ,
   primary key (post_id)
   );
 
-- Removed the following for the time being because seller/buyer dont exist yet
--    foreign key (seller) references user(uid),
--    foreign key (buyer) references user(uid),
-- sample user
insert into user(email,name,password) values ('ar5@wellesley.edu','amish','secure123');

-- sample post
 insert into post(post_id,price,details,delivery_method,category) values (1,10,'This is a sample post','pickup','furniture');
 insert into post(price,title,delivery_method,category) values (50,'Harry Potter','delivery','books');
 