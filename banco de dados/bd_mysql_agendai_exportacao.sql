CREATE DATABASE  IF NOT EXISTS `agendai` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agendai`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: agendai
-- ------------------------------------------------------
-- Server version	8.0.21

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
-- Table structure for table `agendamentos`
--

DROP TABLE IF EXISTS `agendamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agendamentos` (
  `ID AGENDAMENTO` int NOT NULL AUTO_INCREMENT,
  `SERVIÇO SOLICITADO` varchar(50) NOT NULL,
  `DATA SERVIÇO` date DEFAULT NULL,
  `HORÁRIO SERVIÇO` time NOT NULL,
  `DATAeHORA SOLICITAÇÃO` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `NOME PROFISSIONAL` varchar(50) NOT NULL,
  `ID CLIENTE` int DEFAULT NULL,
  `ID PROFISSIONAL` int DEFAULT NULL,
  PRIMARY KEY (`ID AGENDAMENTO`),
  KEY `ID CLIENTE` (`ID CLIENTE`),
  KEY `ID PROFISSIONAL` (`ID PROFISSIONAL`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agendamentos`
--

LOCK TABLES `agendamentos` WRITE;
/*!40000 ALTER TABLE `agendamentos` DISABLE KEYS */;
INSERT INTO `agendamentos` VALUES (8,'limpeza de pele','2022-02-24','08:00:00','2022-02-22 11:00:00','AMANDA',NULL,NULL),(7,'unhas','2022-02-23','08:00:00','2022-02-22 11:00:00','FLÁVIA',NULL,NULL),(6,'corte cabelo','2022-02-22','08:00:00','2022-02-22 11:00:00','JÉSSICA',NULL,NULL),(9,'corte cabelo','2022-02-25','08:00:00','2022-02-22 11:00:00','JAQUELINE',NULL,NULL),(27,'Corte de cabelo',NULL,'00:00:11','2022-03-02 03:30:52','08:22',NULL,NULL),(26,'Corte de cabelo',NULL,'00:00:11','2022-03-02 03:30:49','08:22',NULL,NULL);
/*!40000 ALTER TABLE `agendamentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `ID CLIENTE` int NOT NULL AUTO_INCREMENT,
  `NOME CLIENTE` varchar(50) NOT NULL,
  `CELULAR CLIENTE` varchar(20) NOT NULL,
  PRIMARY KEY (`ID CLIENTE`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (8,'MARIA','48999754647'),(7,'0','48999754646'),(21,'0','048999684524'),(34,'a','4'),(23,'teste add cliente','77777777777'),(33,'RE','048999684524');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profissionais`
--

DROP TABLE IF EXISTS `profissionais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profissionais` (
  `ID PROFISSIONAL` int NOT NULL AUTO_INCREMENT,
  `NOME PROFISSIONAL` varchar(50) NOT NULL,
  PRIMARY KEY (`ID PROFISSIONAL`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profissionais`
--

LOCK TABLES `profissionais` WRITE;
/*!40000 ALTER TABLE `profissionais` DISABLE KEYS */;
INSERT INTO `profissionais` VALUES (9,'JAQUELINE'),(8,'AMANDA'),(7,'FLÁVIA'),(6,'JÉSSICA');
/*!40000 ALTER TABLE `profissionais` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-02  0:40:16
