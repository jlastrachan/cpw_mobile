USE jennya+cpw_mobile;

DROP TABLE IF EXISTS events;
CREATE TABLE events
(
  id              int unsigned NOT NULL auto_increment, # Unique ID for the record
  name            varchar(255) NOT NULL,                # Full title of the book
  startTime       varchar(255) NOT NULL,                # The author of the book
  endTime         varchar(255) NOT NULL, 
  location        varchar(255) NOT NULL,
  description     varchar(1024) NOT NULL,
  day             varchar(255) NOT NULL,
  featured        varchar(255) NOT NULL,
  arts            varchar(255) NOT NULL,  
  academic        varchar(255) NOT NULL,
  athletic        varchar(255) NOT NULL,
  tour            varchar(255) NOT NULL,  
  class           varchar(255) NOT NULL,
  dorm            varchar(255) NOT NULL,
  parents         varchar(255) NOT NULL,
  livinggroup     varchar(255) NOT NULL,
  religious       varchar(255) NOT NULL,
  studentorg      varchar(255) NOT NULL,
  minority        varchar(255) NOT NULL, 

  PRIMARY KEY     (id)
);
