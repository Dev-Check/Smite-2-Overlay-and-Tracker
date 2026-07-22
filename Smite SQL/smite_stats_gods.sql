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
-- Table structure for table `gods`
--

DROP TABLE IF EXISTS `gods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gods` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gods`
--

LOCK TABLES `gods` WRITE;
/*!40000 ALTER TABLE `gods` DISABLE KEYS */;
INSERT INTO `gods` VALUES (1,'Achilles'),(2,'Agni'),(83,'Ah Puch'),(3,'Aladdin'),(4,'Amaterasu'),(5,'Anhur'),(6,'Anubis'),(7,'Aphrodite'),(8,'Apollo'),(9,'Ares'),(10,'Artemis'),(11,'Artio'),(12,'Athena'),(82,'Atlas'),(13,'Awilix'),(14,'Bacchus'),(15,'Baron Samedi'),(85,'Bastet'),(16,'Bellona'),(17,'Cabrakan'),(18,'Cerberus'),(19,'Cernunnos'),(20,'Chaac'),(21,'Charon'),(22,'Chiron'),(86,'Chronos'),(88,'Cu Chulainn'),(23,'Cupid'),(24,'Da Ji'),(25,'Danzaburo'),(26,'Discordia'),(27,'Eset'),(28,'Fenrir'),(29,'Ganesha'),(30,'Geb'),(79,'Gilgamesh'),(31,'Guan Yu'),(32,'Hades'),(33,'Hecate'),(34,'Hercules'),(84,'Horus'),(35,'Hou Yi'),(37,'Hun Batz'),(81,'Ishtar'),(38,'Izanami'),(39,'Janus'),(40,'Jing Wei'),(41,'Jormungandr'),(42,'Kali'),(43,'Khepri'),(44,'Kukulkan'),(45,'Loki'),(46,'Medusa'),(47,'Mercury'),(48,'Merlin'),(49,'Mordred'),(50,'Morgan Le Fay'),(70,'Morrigan'),(36,'Mulan'),(51,'Ne Zha'),(52,'Neith'),(53,'Nemesis'),(54,'Nu Wa'),(55,'Nut'),(56,'Odin'),(57,'Osiris'),(58,'Pele'),(59,'Poseidon'),(60,'Princess Bari'),(61,'Ra'),(62,'Rama'),(80,'Ratatoskr'),(63,'Scylla'),(64,'Sobek'),(65,'Sol'),(66,'Sun Wukong'),(67,'Susano'),(68,'Sylvanus'),(69,'Thanatos'),(71,'Thor'),(72,'Tsukuyomi'),(73,'Ullr'),(74,'Vulcan'),(75,'Xbalanque'),(87,'Xing Tian'),(76,'Yemoja'),(77,'Ymir'),(78,'Zeus');
/*!40000 ALTER TABLE `gods` ENABLE KEYS */;
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
