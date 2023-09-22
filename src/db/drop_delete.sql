USE sherlock;

LOCK TABLES `film` WRITE;
DELETE FROM `film` WHERE release_year < 2006;
UNLOCK TABLES;

DROP TABLE `inventory`;