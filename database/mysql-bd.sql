/* Criar banco de dados */

CREATE DATABASE `TODO` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(120) NOT NULL,
  `description` varchar(40) NOT NULL,
  `done` tinyint(1) DEFAULT NULL,
  `date_start` date DEFAULT NULL,
  `date_stop` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4;
