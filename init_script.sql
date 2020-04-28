
DROP TABLE IF EXISTS main.USERS;
CREATE TABLE IF NOT EXISTS main.USERS
(id INTEGER PRIMARY KEY AUTOINCREMENT, telegram_id INTEGER not null, name varchar(20) not null, balance integer);

