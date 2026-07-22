CREATE DATABASE  IF NOT EXISTS `smite_stats` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `smite_stats`;
-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: smite_stats
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `raw_matches`
--

DROP TABLE IF EXISTS `raw_matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `raw_matches` (
  `match_date` date DEFAULT NULL,
  `gamemode` varchar(50) DEFAULT NULL,
  `match_role` varchar(50) DEFAULT NULL,
  `god` varchar(50) DEFAULT NULL,
  `enemy_god` varchar(50) DEFAULT NULL,
  `kills` int DEFAULT NULL,
  `deaths` int DEFAULT NULL,
  `assists` int DEFAULT NULL,
  `game_time` time DEFAULT NULL,
  `win` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `raw_matches`
--

LOCK TABLES `raw_matches` WRITE;
/*!40000 ALTER TABLE `raw_matches` DISABLE KEYS */;
INSERT INTO `raw_matches` VALUES ('2025-01-10','Conquest','Solo','Bellona','Amaterasu',9,5,11,'00:38:36',1),('2025-01-10','Conquest','Solo','Bellona','Mulan',2,5,4,'00:29:12',1),('2025-01-10','Conquest','Solo','Amaterasu','Hades',0,2,0,'00:12:59',1),('2025-01-10','Conquest','Carry','Jing Wei','Ullr',5,8,8,'00:33:37',0),('2025-01-11','Conquest','Jungle','Nemesis','Loki',0,1,0,'00:13:55',1),('2025-01-11','Conquest','Support','Yemoja','Geb',0,5,3,'00:26:10',0),('2025-01-12','Conquest','Solo','Bellona','Nu Wa',5,6,1,'00:26:13',0),('2025-01-12','Conquest','Support','Yemoja','Sobek',3,4,9,'00:24:11',1),('2025-01-12','Conquest','Carry','Jing Wei','Sol',7,6,8,'00:30:36',1),('2025-01-12','Conquest','Middle','Morrigan','Anubis',2,5,1,'00:22:38',0),('2025-01-15','Conquest','Jungle','Pele','Loki',8,12,16,'00:45:09',0),('2025-01-16','Conquest','Support','Hecate','Baron Samedi',0,3,2,'00:15:30',1),('2025-01-16','Conquest','Solo','Bellona','Mulan',8,5,7,'00:31:19',1),('2025-01-16','Conquest','Solo','Bellona','Hercules',11,2,10,'00:39:08',1),('2025-01-16','Conquest','Solo','Bellona','Sol',3,3,3,'00:24:24',1),('2025-01-16','Conquest','Solo','Bellona','Ymir',8,10,14,'00:42:40',0),('2025-01-16','Conquest','Carry','Neith','Neith',3,0,3,'00:15:59',1),('2025-01-16','Conquest','Solo','Bellona','Hercules',3,4,0,'00:27:32',1),('2025-01-16','Conquest','Support','Athena','Sobek',2,12,16,'00:36:05',0),('2025-01-17','Conquest','Support','Aphrodite','Ymir',2,4,4,'00:23:46',1),('2025-01-19','Conquest','Support','Hecate','Hecate',4,7,22,'00:51:37',1),('2025-01-19','Conquest','Solo','Bellona','Chaac',2,1,5,'00:25:38',1),('2025-01-20','Conquest','Solo','Bellona','Amaterasu',4,8,9,'00:33:35',0),('2025-01-20','Conquest','Middle','Morrigan','Agni',6,5,3,'00:22:39',1),('2025-01-20','Conquest','Middle','Nu Wa','Thanatos',0,13,12,'00:48:16',0),('2025-01-20','Conquest','Carry','Neith','Medusa',0,5,0,'00:25:36',0),('2025-01-20','Conquest','Solo','Bellona','Cabrakan',6,7,2,'00:38:59',0),('2025-01-21','Conquest','Middle','Neith','Ra',0,5,3,'00:27:59',0),('2025-01-21','Conquest','Carry','Sol','Anhur',7,3,16,'00:32:54',1),('2025-01-21','Conquest','Solo','Bellona','Hercules',2,6,3,'00:25:28',1),('2025-01-21','Conquest','Carry','Neith','Zeus',3,7,6,'00:38:40',0),('2025-07-15','Conquest','Solo','Bellona','Cabrakan',0,2,1,'00:13:46',0),('2025-07-18','Conquest','Solo','Bellona','Mordred',7,5,13,'00:43:53',0),('2025-07-29','Conquest','Jungle','Awilix','Odin',10,12,14,'00:45:50',1),('2025-07-31','Conquest','Jungle','Pele','Kali',6,6,10,'00:37:00',1),('2025-07-31','Conquest','Support','Aphrodite','Ares',0,11,12,'00:34:39',0),('2025-08-25','Conquest','Solo','Bellona','Nemesis',1,4,1,'00:27:00',0),('2025-08-28','Conquest','Solo','Bellona','Mordred',2,0,0,'00:20:26',1),('2025-08-28','Conquest','Middle','Aphrodite','Anubis',4,9,7,'00:36:27',0),('2025-09-01','Conquest','Support','Jormungandr','Ymir',1,12,10,'00:39:50',0),('2025-09-01','Conquest','Solo','Mulan','Jormungandr',5,9,10,'00:41:12',0),('2025-09-01','Conquest','Solo','Amaterasu','Anubis',5,4,4,'00:34:36',0),('2025-09-01','Conquest','Solo','Amaterasu','Achilles',6,7,16,'00:40:46',1),('2025-09-01','Conquest','Solo','Amaterasu','Jormungandr',0,1,0,'00:12:32',1),('2025-09-01','Conquest','Solo','Mulan','Morrigan',3,11,6,'00:40:17',0),('2025-09-01','Conquest','Support','Cerberus','Ganesha',1,2,1,'00:15:28',0),('2025-09-01','Conquest','Jungle','Awilix','Thanatos',11,6,11,'00:38:24',1),('2025-09-01','Conquest','Solo','Mulan','Amaterasu',11,2,15,'00:40:41',1),('2025-09-01','Conquest','Solo','Mulan','Hercules',6,6,12,'00:40:54',1),('2025-09-01','Conquest','Solo','Mulan','Achilles',6,6,8,'00:43:40',1),('2025-09-01','Conquest','Solo','Mulan','Thor',5,13,11,'00:48:36',0),('2025-09-03','Conquest','Middle','Princess Bari','Janus',0,5,0,'00:18:38',0),('2025-09-05','Conquest','Support','Aphrodite','Khepri',1,9,21,'00:43:03',1),('2025-09-08','Conquest','Solo','Mulan','Bellona',3,5,12,'00:32:52',1),('2025-09-08','Conquest','Support','Aphrodite','Loki',1,5,9,'00:40:52',0),('2025-09-08','Conquest','Solo','Mulan','Bellona',2,5,2,'00:30:51',1),('2025-09-08','Conquest','Solo','Mulan','Hercules',0,2,0,'00:18:17',0),('2025-09-09','Conquest','Support','Aphrodite','Ra',0,10,40,'01:00:55',1),('2025-09-25','Conquest','Support','Aphrodite','Geb',0,4,3,'00:20:00',0),('2025-12-21','Conquest','Jungle','Awilix','Susano',16,12,16,'00:44:49',1),('2025-12-21','Conquest','Solo','Artio','Nu Wa',3,8,27,'00:44:26',1),('2025-12-22','Conquest','Middle','Neith','Awilix',11,8,6,'00:37:34',0),('2025-12-28','Conquest','Support','Yemoja','Jormungandr',0,0,10,'00:20:06',1),('2025-12-28','Conquest','Support','Yemoja','Bacchus',2,2,3,'00:20:21',1),('2025-12-28','Conquest','Carry','Sol','Anhur',11,4,11,'00:37:16',1),('2025-12-28','Conquest','Support','Yemoja','Sobek',1,10,16,'00:41:55',0),('2025-12-30','Conquest','Solo','Mulan','Neith',3,7,3,'00:33:09',0),('2025-12-30','Conquest','Middle','Eset','Anubis',9,8,4,'00:27:17',0),('2025-12-30','Conquest','Support','Yemoja','Nut',1,4,20,'00:40:26',1),('2025-12-30','Conquest','Support','Yemoja','Khepri',0,4,7,'00:20:13',1),('2025-12-30','Conquest','Support','Yemoja','Jormungandr',6,11,17,'00:43:36',0),('2025-12-30','Conquest','Carry','Sol','Izanami',12,3,6,'00:29:21',1),('2025-12-30','Conquest','Carry','Sol','Danzaburo',6,9,10,'00:38:50',0),('2025-12-31','Conquest','Solo','Mulan','Ullr',5,6,15,'00:43:54',1),('2025-12-31','Conquest','Support','Yemoja','Jormungandr',1,0,2,'00:18:31',0),('2025-12-31','Conquest','Solo','Mulan','Nemesis',8,5,3,'00:23:54',1),('2025-12-31','Conquest','Carry','Sol','Neith',16,8,11,'00:44:11',1),('2025-12-31','Conquest','Solo','Mulan','Mordred',0,2,0,'00:12:44',0),('2025-12-31','Conquest','Solo','Mulan','Hercules',3,7,5,'00:31:42',0),('2026-01-01','Conquest','Solo','Mulan','Sun Wukong',1,8,4,'00:27:50',0),('2026-01-01','Conquest','Carry','Sol','Cupid',7,7,12,'00:39:33',1),('2026-01-01','Conquest','Middle','Sol','Neith',0,9,3,'00:37:08',0),('2026-01-02','Conquest','Solo','Mulan','Cerberus',4,10,10,'00:44:17',0),('2026-01-04','Conquest','Solo','Bellona','Mordred',8,7,13,'00:36:57',1),('2026-01-04','Conquest','Solo','Bellona','Artio',3,5,10,'00:33:40',1),('2026-01-07','Conquest','Solo','Bellona','Thor',2,3,1,'00:18:28',1),('2026-01-07','Conquest','Solo','Bellona','Jormungandr',2,5,2,'00:18:51',0),('2026-01-07','Conquest','Carry','Sol','Danzaburo',4,17,7,'00:54:14',0),('2025-01-10','Conquest','Solo','Bellona','Amaterasu',9,5,11,'00:38:36',1),('2025-01-10','Conquest','Solo','Bellona','Mulan',2,5,4,'00:29:12',1),('2025-01-10','Conquest','Solo','Amaterasu','Hades',0,2,0,'00:12:59',1),('2025-01-10','Conquest','Carry','Jing Wei','Ullr',5,8,8,'00:33:37',0),('2025-01-11','Conquest','Jungle','Nemesis','Loki',0,1,0,'00:13:55',1),('2025-01-11','Conquest','Support','Yemoja','Geb',0,5,3,'00:26:10',0),('2026-01-21','Conquest','Carry','Jing Wei','Discordia',6,9,5,'00:38:03',0),('2026-01-22','Conquest','Solo','Bellona','Danzaburo',12,5,13,'00:36:27',1),('2026-01-25','Conquest','Solo','Bellona','Sun Wukong',0,1,1,'00:18:07',1),('2026-01-25','Conquest','Jungle','Bellona','Tsukuyomi',4,7,12,'00:35:56',0),('2026-01-26','Conquest','Solo','Bellona','Osiris',17,5,10,'00:39:48',1),('2026-01-26','Conquest','Middle','Eset','Nu Wa',5,7,7,'00:38:18',0),('2026-01-26','Conquest','Solo','Bellona','Sun Wukong',10,10,11,'00:48:14',1),('2026-01-26','Conquest','Solo','Bellona','Mulan',1,5,0,'00:18:34',0),('2026-01-26','Conquest','Middle','Eset','Danzaburo',1,11,5,'00:36:56',0),('2026-01-27','Conquest','Solo','Bellona','Baron Samedi',14,6,19,'00:43:34',1),('2026-01-27','Conquest','Solo','Bellona','Mulan',2,1,0,'00:13:52',0),('2026-01-27','Conquest','Solo','Bellona','Kukulkan',8,4,6,'00:37:22',1),('2026-01-27','Conquest','Solo','Bellona','Thor',1,1,0,'00:15:13',1),('2026-01-27','Conquest','Solo','Bellona','Cerberus',5,6,12,'00:48:06',1),('2026-01-28','Conquest','Solo','Bellona','Chiron',6,6,14,'00:34:20',1),('2026-01-28','Conquest','Support','Yemoja','Eset',2,0,11,'00:18:07',1),('2026-01-28','Conquest','Solo','Bellona','Chaac',1,2,0,'00:26:07',0),('2026-01-28','Conquest','Support','Yemoja','Khepri',4,5,28,'00:57:27',1),('2026-01-28','Conquest','Support','Yemoja','Sobek',0,4,1,'00:20:38',0),('2026-01-29','Conquest','Solo','Bellona','Amaterasu',3,6,1,'00:37:36',0),('2026-02-02','Conquest','Support','Yemoja','Achilles',2,2,3,'00:19:27',0),('2026-02-02','Conquest','Solo','Bellona','Hou Yi',11,9,16,'00:50:26',1),('2026-02-02','Conquest','Solo','Bellona','Thor',1,7,1,'00:26:24',0),('2026-02-03','Conquest','Support','Yemoja','Khepri',1,3,9,'00:23:02',1),('2026-02-05','Conquest','Solo','Amaterasu','Osiris',1,8,2,'00:35:34',0),('2026-02-10','Conquest','Solo','Mulan','Bellona',6,2,4,'00:25:26',1),('2026-02-10','Conquest','Middle','Hecate','Discordia',2,6,0,'00:22:39',0),('2026-02-10','Conquest','Support','Aphrodite','Ganesha',4,4,18,'00:32:52',1),('2026-02-10','Conquest','Solo','Mulan','Ne Zha',11,6,13,'00:34:01',1),('2026-02-15','Conquest','Support','Aphrodite','Sylvanus',2,3,18,'00:43:55',1),('2026-02-16','Conquest','Support','Aphrodite','Artio',0,8,5,'00:33:09',0),('2026-02-16','Conquest','Solo','Mulan','Ne Zha',1,5,0,'00:18:02',0);
/*!40000 ALTER TABLE `raw_matches` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-22 12:26:05
