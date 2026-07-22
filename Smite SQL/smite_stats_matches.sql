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
-- Table structure for table `matches`
--

DROP TABLE IF EXISTS `matches`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matches` (
  `id` int NOT NULL AUTO_INCREMENT,
  `match_date` date DEFAULT NULL,
  `gamemode` varchar(50) DEFAULT NULL,
  `match_role` varchar(50) DEFAULT NULL,
  `player_god_id` int DEFAULT NULL,
  `enemy_god_id` int DEFAULT NULL,
  `kills` int DEFAULT NULL,
  `deaths` int DEFAULT NULL,
  `assists` int DEFAULT NULL,
  `game_time` time DEFAULT NULL,
  `win` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `player_god_id` (`player_god_id`),
  KEY `enemy_god_id` (`enemy_god_id`),
  CONSTRAINT `matches_ibfk_1` FOREIGN KEY (`player_god_id`) REFERENCES `gods` (`id`),
  CONSTRAINT `matches_ibfk_2` FOREIGN KEY (`enemy_god_id`) REFERENCES `gods` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=127 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matches`
--

LOCK TABLES `matches` WRITE;
/*!40000 ALTER TABLE `matches` DISABLE KEYS */;
INSERT INTO `matches` VALUES (1,'2025-01-10','Conquest','Solo',16,4,9,5,11,'00:38:36',1),(2,'2025-01-10','Conquest','Solo',16,36,2,5,4,'00:29:12',1),(3,'2025-01-10','Conquest','Solo',4,32,0,2,0,'00:12:59',1),(4,'2025-01-10','Conquest','Carry',40,73,5,8,8,'00:33:37',0),(5,'2025-01-11','Conquest','Jungle',53,45,0,1,0,'00:13:55',1),(6,'2025-01-11','Conquest','Support',76,30,0,5,3,'00:26:10',0),(7,'2025-01-12','Conquest','Solo',16,54,5,6,1,'00:26:13',0),(8,'2025-01-12','Conquest','Support',76,64,3,4,9,'00:24:11',1),(9,'2025-01-12','Conquest','Carry',40,65,7,6,8,'00:30:36',1),(10,'2025-01-12','Conquest','Middle',70,6,2,5,1,'00:22:38',0),(11,'2025-01-15','Conquest','Jungle',58,45,8,12,16,'00:45:09',0),(12,'2025-01-16','Conquest','Support',33,15,0,3,2,'00:15:30',1),(13,'2025-01-16','Conquest','Solo',16,36,8,5,7,'00:31:19',1),(14,'2025-01-16','Conquest','Solo',16,34,11,2,10,'00:39:08',1),(15,'2025-01-16','Conquest','Solo',16,65,3,3,3,'00:24:24',1),(16,'2025-01-16','Conquest','Solo',16,77,8,10,14,'00:42:40',0),(17,'2025-01-16','Conquest','Carry',52,52,3,0,3,'00:15:59',1),(18,'2025-01-16','Conquest','Solo',16,34,3,4,0,'00:27:32',1),(19,'2025-01-16','Conquest','Support',12,64,2,12,16,'00:36:05',0),(20,'2025-01-17','Conquest','Support',7,77,2,4,4,'00:23:46',1),(21,'2025-01-19','Conquest','Support',33,33,4,7,22,'00:51:37',1),(22,'2025-01-19','Conquest','Solo',16,20,2,1,5,'00:25:38',1),(23,'2025-01-20','Conquest','Solo',16,4,4,8,9,'00:33:35',0),(24,'2025-01-20','Conquest','Middle',70,2,6,5,3,'00:22:39',1),(25,'2025-01-20','Conquest','Middle',54,69,0,13,12,'00:48:16',0),(26,'2025-01-20','Conquest','Carry',52,46,0,5,0,'00:25:36',0),(27,'2025-01-20','Conquest','Solo',16,17,6,7,2,'00:38:59',0),(28,'2025-01-21','Conquest','Middle',52,61,0,5,3,'00:27:59',0),(29,'2025-01-21','Conquest','Carry',65,5,7,3,16,'00:32:54',1),(30,'2025-01-21','Conquest','Solo',16,34,2,6,3,'00:25:28',1),(31,'2025-01-21','Conquest','Carry',52,78,3,7,6,'00:38:40',0),(32,'2025-07-15','Conquest','Solo',16,17,0,2,1,'00:13:46',0),(33,'2025-07-18','Conquest','Solo',16,49,7,5,13,'00:43:53',0),(34,'2025-07-29','Conquest','Jungle',13,56,10,12,14,'00:45:50',1),(35,'2025-07-31','Conquest','Jungle',58,42,6,6,10,'00:37:00',1),(36,'2025-07-31','Conquest','Support',7,9,0,11,12,'00:34:39',0),(37,'2025-08-25','Conquest','Solo',16,53,1,4,1,'00:27:00',0),(38,'2025-08-28','Conquest','Solo',16,49,2,0,0,'00:20:26',1),(39,'2025-08-28','Conquest','Middle',7,6,4,9,7,'00:36:27',0),(40,'2025-09-01','Conquest','Support',41,77,1,12,10,'00:39:50',0),(41,'2025-09-01','Conquest','Solo',36,41,5,9,10,'00:41:12',0),(42,'2025-09-01','Conquest','Solo',4,6,5,4,4,'00:34:36',0),(43,'2025-09-01','Conquest','Solo',4,1,6,7,16,'00:40:46',1),(44,'2025-09-01','Conquest','Solo',4,41,0,1,0,'00:12:32',1),(45,'2025-09-01','Conquest','Solo',36,70,3,11,6,'00:40:17',0),(46,'2025-09-01','Conquest','Support',18,29,1,2,1,'00:15:28',0),(47,'2025-09-01','Conquest','Jungle',13,69,11,6,11,'00:38:24',1),(48,'2025-09-01','Conquest','Solo',36,4,11,2,15,'00:40:41',1),(49,'2025-09-01','Conquest','Solo',36,34,6,6,12,'00:40:54',1),(50,'2025-09-01','Conquest','Solo',36,1,6,6,8,'00:43:40',1),(51,'2025-09-01','Conquest','Solo',36,71,5,13,11,'00:48:36',0),(52,'2025-09-03','Conquest','Middle',60,39,0,5,0,'00:18:38',0),(53,'2025-09-05','Conquest','Support',7,43,1,9,21,'00:43:03',1),(54,'2025-09-08','Conquest','Solo',36,16,3,5,12,'00:32:52',1),(55,'2025-09-08','Conquest','Support',7,45,1,5,9,'00:40:52',0),(56,'2025-09-08','Conquest','Solo',36,16,2,5,2,'00:30:51',1),(57,'2025-09-08','Conquest','Solo',36,34,0,2,0,'00:18:17',0),(58,'2025-09-09','Conquest','Support',7,61,0,10,40,'01:00:55',1),(59,'2025-09-25','Conquest','Support',7,30,0,4,3,'00:20:00',0),(60,'2025-12-21','Conquest','Jungle',13,67,16,12,16,'00:44:49',1),(61,'2025-12-21','Conquest','Solo',11,54,3,8,27,'00:44:26',1),(62,'2025-12-22','Conquest','Middle',52,13,11,8,6,'00:37:34',0),(63,'2025-12-28','Conquest','Support',76,41,0,0,10,'00:20:06',1),(64,'2025-12-28','Conquest','Support',76,14,2,2,3,'00:20:21',1),(65,'2025-12-28','Conquest','Carry',65,5,11,4,11,'00:37:16',1),(66,'2025-12-28','Conquest','Support',76,64,1,10,16,'00:41:55',0),(67,'2025-12-30','Conquest','Solo',36,52,3,7,3,'00:33:09',0),(68,'2025-12-30','Conquest','Middle',27,6,9,8,4,'00:27:17',0),(69,'2025-12-30','Conquest','Support',76,55,1,4,20,'00:40:26',1),(70,'2025-12-30','Conquest','Support',76,43,0,4,7,'00:20:13',1),(71,'2025-12-30','Conquest','Support',76,41,6,11,17,'00:43:36',0),(72,'2025-12-30','Conquest','Carry',65,38,12,3,6,'00:29:21',1),(73,'2025-12-30','Conquest','Carry',65,25,6,9,10,'00:38:50',0),(74,'2025-12-31','Conquest','Solo',36,73,5,6,15,'00:43:54',1),(75,'2025-12-31','Conquest','Support',76,41,1,0,2,'00:18:31',0),(76,'2025-12-31','Conquest','Solo',36,53,8,5,3,'00:23:54',1),(77,'2025-12-31','Conquest','Carry',65,52,16,8,11,'00:44:11',1),(78,'2025-12-31','Conquest','Solo',36,49,0,2,0,'00:12:44',0),(79,'2025-12-31','Conquest','Solo',36,34,3,7,5,'00:31:42',0),(80,'2026-01-01','Conquest','Solo',36,66,1,8,4,'00:27:50',0),(81,'2026-01-01','Conquest','Carry',65,23,7,7,12,'00:39:33',1),(82,'2026-01-01','Conquest','Middle',65,52,0,9,3,'00:37:08',0),(83,'2026-01-02','Conquest','Solo',36,18,4,10,10,'00:44:17',0),(84,'2026-01-04','Conquest','Solo',16,49,8,7,13,'00:36:57',1),(85,'2026-01-04','Conquest','Solo',16,11,3,5,10,'00:33:40',1),(86,'2026-01-07','Conquest','Solo',16,71,2,3,1,'00:18:28',1),(87,'2026-01-07','Conquest','Solo',16,41,2,5,2,'00:18:51',0),(88,'2026-01-07','Conquest','Carry',65,25,4,17,7,'00:54:14',0),(89,'2025-01-10','Conquest','Solo',16,4,9,5,11,'00:38:36',1),(90,'2025-01-10','Conquest','Solo',16,36,2,5,4,'00:29:12',1),(91,'2025-01-10','Conquest','Solo',4,32,0,2,0,'00:12:59',1),(92,'2025-01-10','Conquest','Carry',40,73,5,8,8,'00:33:37',0),(93,'2025-01-11','Conquest','Jungle',53,45,0,1,0,'00:13:55',1),(94,'2025-01-11','Conquest','Support',76,30,0,5,3,'00:26:10',0),(95,'2026-01-21','Conquest','Carry',40,26,6,9,5,'00:38:03',0),(96,'2026-01-22','Conquest','Solo',16,25,12,5,13,'00:36:27',1),(97,'2026-01-25','Conquest','Solo',16,66,0,1,1,'00:18:07',1),(98,'2026-01-25','Conquest','Jungle',16,72,4,7,12,'00:35:56',0),(99,'2026-01-26','Conquest','Solo',16,57,17,5,10,'00:39:48',1),(100,'2026-01-26','Conquest','Middle',27,54,5,7,7,'00:38:18',0),(101,'2026-01-26','Conquest','Solo',16,66,10,10,11,'00:48:14',1),(102,'2026-01-26','Conquest','Solo',16,36,1,5,0,'00:18:34',0),(103,'2026-01-26','Conquest','Middle',27,25,1,11,5,'00:36:56',0),(104,'2026-01-27','Conquest','Solo',16,15,14,6,19,'00:43:34',1),(105,'2026-01-27','Conquest','Solo',16,36,2,1,0,'00:13:52',0),(106,'2026-01-27','Conquest','Solo',16,44,8,4,6,'00:37:22',1),(107,'2026-01-27','Conquest','Solo',16,71,1,1,0,'00:15:13',1),(108,'2026-01-27','Conquest','Solo',16,18,5,6,12,'00:48:06',1),(109,'2026-01-28','Conquest','Solo',16,22,6,6,14,'00:34:20',1),(110,'2026-01-28','Conquest','Support',76,27,2,0,11,'00:18:07',1),(111,'2026-01-28','Conquest','Solo',16,20,1,2,0,'00:26:07',0),(112,'2026-01-28','Conquest','Support',76,43,4,5,28,'00:57:27',1),(113,'2026-01-28','Conquest','Support',76,64,0,4,1,'00:20:38',0),(114,'2026-01-29','Conquest','Solo',16,4,3,6,1,'00:37:36',0),(115,'2026-02-02','Conquest','Support',76,1,2,2,3,'00:19:27',0),(116,'2026-02-02','Conquest','Solo',16,35,11,9,16,'00:50:26',1),(117,'2026-02-02','Conquest','Solo',16,71,1,7,1,'00:26:24',0),(118,'2026-02-03','Conquest','Support',76,43,1,3,9,'00:23:02',1),(119,'2026-02-05','Conquest','Solo',4,57,1,8,2,'00:35:34',0),(120,'2026-02-10','Conquest','Solo',36,16,6,2,4,'00:25:26',1),(121,'2026-02-10','Conquest','Middle',33,26,2,6,0,'00:22:39',0),(122,'2026-02-10','Conquest','Support',7,29,4,4,18,'00:32:52',1),(123,'2026-02-10','Conquest','Solo',36,51,11,6,13,'00:34:01',1),(124,'2026-02-15','Conquest','Support',7,68,2,3,18,'00:43:55',1),(125,'2026-02-16','Conquest','Support',7,11,0,8,5,'00:33:09',0),(126,'2026-02-16','Conquest','Solo',36,51,1,5,0,'00:18:02',0);
/*!40000 ALTER TABLE `matches` ENABLE KEYS */;
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
