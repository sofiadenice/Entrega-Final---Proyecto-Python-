CREATE DATABASE  IF NOT EXISTS `myfitapp` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `myfitapp`;
-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: myfitapp
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `cardiovascular`
--

DROP TABLE IF EXISTS `cardiovascular`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cardiovascular` (
  `id_ejercicio` int NOT NULL AUTO_INCREMENT,
  `nombreEjercicio` varchar(45) NOT NULL,
  `caloriasQuemadas` decimal(10,2) NOT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_ejercicio`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cardiovascular`
--

LOCK TABLES `cardiovascular` WRITE;
/*!40000 ALTER TABLE `cardiovascular` DISABLE KEYS */;
INSERT INTO `cardiovascular` VALUES (1,'Pasos altos',14.66,3),(2,'Escalada',13.00,0),(3,'Comba',12.08,0),(4,'Flexiones con sentadillas',10.83,0),(5,'Corrida',11.67,0),(6,'Mountain Climbers',9.00,0),(7,'Bicicleta',6.88,0),(8,'Eliptica',10.83,0),(9,'Aerobicos',11.33,0),(10,'Side Plank',7.00,3),(11,'Pasos altos con caja',15.99,1),(12,'Golpe de gluteos',10.56,0),(13,'Salto de Skater',9.07,0),(14,'Power Skip',10.09,0),(15,'Paso de Sprint',11.00,0),(16,'Salto de Sprint',12.66,0),(17,'Corrida con pecho',11.95,3),(18,'Salto de lado a lado',8.77,0),(19,'Squat adentro y afuera',9.66,5),(20,'Golpe rotatorio',8.50,5),(21,'Sube y baja',9.77,0),(22,'Golpe diagonal',7.88,5),(23,'Corrida de montaña',6.77,0),(24,'Corrida de montaña en semicirculo',8.94,1),(25,'Salto de puntillas',12.77,0),(26,'Mountain climbers (pesas)',10.00,1),(27,'Plank',8.00,0),(28,'Burpees',10.05,0),(29,'Squats',14.50,0),(30,'Lunge',17.66,0);
/*!40000 ALTER TABLE `cardiovascular` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consumoalimento`
--

DROP TABLE IF EXISTS `consumoalimento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consumoalimento` (
  `id_consumoAlimento` int NOT NULL AUTO_INCREMENT,
  `id_producto` int NOT NULL,
  `id_usuario` int NOT NULL,
  `porcion` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id_consumoAlimento`,`id_producto`,`id_usuario`),
  KEY `fk_ConsumoAlimento_Producto1_idx` (`id_producto`),
  KEY `fk_ConsumoAlimento_Usuario1_idx` (`id_usuario`),
  CONSTRAINT `fk_ConsumoAlimento_Producto1` FOREIGN KEY (`id_producto`) REFERENCES `producto` (`id_producto`),
  CONSTRAINT `fk_ConsumoAlimento_Usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=316 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consumoalimento`
--

LOCK TABLES `consumoalimento` WRITE;
/*!40000 ALTER TABLE `consumoalimento` DISABLE KEYS */;
INSERT INTO `consumoalimento` VALUES (1,1,1,2.00,'2020-11-29'),(2,32,1,1.00,'2020-11-25'),(3,9,1,2.00,'2020-11-29'),(4,34,1,1.00,'2020-11-29'),(5,13,1,1.00,'2020-11-25'),(6,18,1,1.00,'2020-11-29'),(7,4,1,1.00,'2020-11-20'),(8,31,1,1.00,'2020-11-20'),(10,15,1,1.00,'2020-11-21'),(11,17,1,3.00,'2020-11-21'),(13,31,1,2.00,'2020-11-19'),(14,8,1,3.00,'2020-11-19'),(16,3,1,2.00,'2020-11-16'),(17,19,1,3.00,'2020-11-16'),(19,15,1,1.00,'2020-11-26'),(20,20,1,1.00,'2020-11-26'),(21,32,1,2.00,'2020-11-26'),(22,33,1,1.00,'2020-11-27'),(23,37,1,1.00,'2020-11-27'),(24,40,1,1.00,'2020-11-27'),(25,45,1,1.00,'2020-11-28'),(26,33,1,1.00,'2020-11-28'),(27,15,1,1.00,'2020-11-28'),(34,22,1,1.00,'2020-11-30'),(35,26,1,1.00,'2020-11-30'),(36,34,1,1.00,'2020-11-30'),(37,16,1,1.00,'2020-12-01'),(38,20,1,1.00,'2020-12-01'),(39,3,1,1.00,'2020-12-01'),(40,7,1,1.00,'2020-12-02'),(41,12,1,1.00,'2020-12-02'),(42,13,1,1.00,'2020-12-02'),(43,31,1,1.00,'2020-12-03'),(44,47,1,1.00,'2020-12-03'),(45,41,1,2.00,'2020-12-03'),(51,18,2,1.00,'2020-11-29'),(52,4,2,1.00,'2020-11-20'),(53,1,2,1.00,'2020-11-20'),(54,9,2,1.00,'2020-11-20'),(55,15,2,1.00,'2020-11-21'),(56,17,2,4.00,'2020-11-21'),(57,12,2,2.00,'2020-11-21'),(58,5,2,2.00,'2020-11-19'),(59,8,2,3.00,'2020-11-19'),(60,10,2,1.00,'2020-11-19'),(61,3,2,2.00,'2020-11-16'),(62,19,2,3.00,'2020-11-16'),(63,18,2,2.00,'2020-11-16'),(64,15,2,1.00,'2020-11-26'),(65,20,2,1.00,'2020-11-26'),(66,5,2,2.00,'2020-11-26'),(67,6,2,1.00,'2020-11-27'),(68,37,2,1.00,'2020-11-27'),(69,40,2,1.00,'2020-11-27'),(70,45,2,1.00,'2020-11-28'),(71,10,2,1.00,'2020-11-28'),(72,15,2,1.00,'2020-11-28'),(73,36,2,1.00,'2020-11-28'),(76,12,2,1.00,'2020-11-29'),(77,27,2,1.00,'2020-11-29'),(78,35,2,1.00,'2020-11-29'),(79,22,2,1.00,'2020-11-30'),(80,26,2,1.00,'2020-11-30'),(81,27,2,1.00,'2020-11-30'),(82,16,2,1.00,'2020-12-01'),(83,20,2,1.00,'2020-12-01'),(84,3,2,1.00,'2020-12-01'),(85,7,2,1.00,'2020-12-02'),(86,12,2,1.00,'2020-12-02'),(87,13,2,1.00,'2020-12-02'),(88,24,2,1.00,'2020-12-03'),(89,47,2,1.00,'2020-12-03'),(90,41,2,2.00,'2020-12-03'),(92,3,2,1.00,'2020-11-25'),(95,13,2,1.00,'2020-11-25'),(101,38,3,4.00,'2020-11-21'),(102,44,3,2.00,'2020-11-21'),(103,5,3,2.00,'2020-11-19'),(104,38,3,3.00,'2020-11-19'),(105,10,3,1.00,'2020-11-19'),(106,3,3,2.00,'2020-11-16'),(107,19,3,3.00,'2020-11-16'),(109,15,3,1.00,'2020-11-26'),(110,39,3,1.00,'2020-11-26'),(111,5,3,2.00,'2020-11-26'),(112,6,3,1.00,'2020-11-27'),(113,37,3,1.00,'2020-11-27'),(114,39,3,1.00,'2020-11-27'),(115,44,3,1.00,'2020-11-28'),(116,10,3,1.00,'2020-11-28'),(117,15,3,1.00,'2020-11-28'),(121,42,3,1.00,'2020-11-29'),(122,27,3,1.00,'2020-11-29'),(123,42,3,1.00,'2020-11-29'),(124,22,3,1.00,'2020-11-30'),(125,26,3,1.00,'2020-11-30'),(126,27,3,1.00,'2020-11-30'),(127,43,3,1.00,'2020-12-01'),(128,20,3,1.00,'2020-12-01'),(129,3,3,1.00,'2020-12-01'),(130,43,3,1.00,'2020-12-02'),(131,12,3,1.00,'2020-12-02'),(132,13,3,1.00,'2020-12-02'),(133,24,3,1.00,'2020-12-03'),(134,47,3,1.00,'2020-12-03'),(135,43,3,2.00,'2020-12-03'),(137,3,3,1.00,'2020-11-25'),(140,39,3,1.00,'2020-11-25'),(141,44,3,1.00,'2020-11-29'),(142,4,3,1.00,'2020-11-20'),(143,38,3,1.00,'2020-11-20'),(144,9,3,1.00,'2020-11-20'),(145,15,3,1.00,'2020-11-21'),(157,6,4,1.00,'2020-11-27'),(158,37,4,1.00,'2020-11-27'),(159,40,4,1.00,'2020-11-27'),(160,45,4,1.00,'2020-11-28'),(161,10,4,1.00,'2020-11-28'),(162,15,4,1.00,'2020-11-28'),(163,36,4,1.00,'2020-11-28'),(166,12,4,1.00,'2020-11-29'),(167,27,4,1.00,'2020-11-29'),(168,35,4,1.00,'2020-11-29'),(169,22,4,1.00,'2020-11-30'),(170,26,4,1.00,'2020-11-30'),(171,27,4,1.00,'2020-11-30'),(172,16,4,1.00,'2020-12-01'),(173,20,4,1.00,'2020-12-01'),(174,3,4,1.00,'2020-12-01'),(175,7,4,1.00,'2020-12-02'),(176,12,4,1.00,'2020-12-02'),(177,13,4,1.00,'2020-12-02'),(178,24,4,1.00,'2020-12-03'),(179,47,4,1.00,'2020-12-03'),(180,41,4,2.00,'2020-12-03'),(201,5,5,2.00,'2020-11-26'),(202,6,5,1.00,'2020-11-27'),(203,37,5,1.00,'2020-11-27'),(204,48,5,1.00,'2020-11-27'),(205,45,5,1.00,'2020-11-28'),(206,10,5,1.00,'2020-11-28'),(207,15,5,1.00,'2020-11-28'),(211,12,5,1.00,'2020-11-29'),(212,49,5,1.00,'2020-11-29'),(214,22,5,1.00,'2020-11-30'),(215,50,5,1.00,'2020-11-30'),(216,27,5,1.00,'2020-11-30'),(217,16,5,1.00,'2020-12-01'),(218,20,5,1.00,'2020-12-01'),(219,3,5,1.00,'2020-12-01'),(220,50,5,1.00,'2020-12-02'),(221,12,5,1.00,'2020-12-02'),(222,13,5,1.00,'2020-12-02'),(223,24,5,1.00,'2020-12-03'),(224,47,5,1.00,'2020-12-03'),(225,41,5,2.00,'2020-12-03'),(226,1,5,2.00,'2020-11-29'),(227,3,5,1.00,'2020-11-25'),(228,50,5,2.00,'2020-11-29'),(230,48,5,1.00,'2020-11-25'),(232,4,5,1.00,'2020-11-20'),(233,46,5,1.00,'2020-11-20'),(234,9,5,1.00,'2020-11-20'),(235,15,5,1.00,'2020-11-21'),(236,17,5,4.00,'2020-11-21'),(237,12,5,2.00,'2020-11-21'),(238,5,5,2.00,'2020-11-19'),(239,8,5,3.00,'2020-11-19'),(241,3,5,2.00,'2020-11-16'),(242,19,5,3.00,'2020-11-16'),(244,48,5,1.00,'2020-11-26'),(245,20,5,1.00,'2020-11-26');
/*!40000 ALTER TABLE `consumoalimento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fuerza`
--

DROP TABLE IF EXISTS `fuerza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fuerza` (
  `id_ejercicio` int NOT NULL AUTO_INCREMENT,
  `nombreEjercicio` varchar(45) NOT NULL,
  `parteDelCuerpo` varchar(45) DEFAULT NULL,
  `id_usuario` int DEFAULT NULL,
  PRIMARY KEY (`id_ejercicio`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fuerza`
--

LOCK TABLES `fuerza` WRITE;
/*!40000 ALTER TABLE `fuerza` DISABLE KEYS */;
INSERT INTO `fuerza` VALUES (1,'Sentadillas','Piernas',0),(2,'Lagartijas','Pectorales y Triceps',0),(3,'Flexion de biceps','biceps',0),(4,'Burppes','Piernas',0),(5,'Mountain climber','Biceps y abdomen',0),(6,'Planks','Hombros y abdomen',0),(7,'Pose de cobra','abdomen',0),(8,'Saltos','Pantorrillas',0),(9,'Remo','Brazos',0),(10,'Estocadas','Piernas',0),(11,'Lagartijas en triangulo','pectorales y triceps',0),(12,'Remo contracorriente','Biceps y cuadriceps',0),(13,'Sentadillas con peso','Gluteos y piernas',0),(14,'Saltitos de conejo','piernas y pantorrillas',0),(15,'Mountain climber con push ups','pectorales, piernas y abdomen',5),(16,'Abductor','Pantorrillas ',0),(17,'Glute bridge','Gluteos',0),(18,'Dumbell Press','Hombros',0),(19,'Crunches','Abdomen',0),(20,'Leg press','Piernas',5),(21,'pec fly','Pectorales',5),(22,'Arnold press','Biceps y Triceps',0),(23,'Bicep Curl','Biceps',1),(24,'Back raise','Espalda',3),(25,'Hip Strech','Caderas',0),(26,'Bench Press','Pechito ricolin',1),(27,'Lat prayer','Abdomen y brazos',0),(28,'scissor kicks','Abdomen',3),(29,'Russian twist','Abdomen',3),(30,'Tricep dip','Triceps y hombros',1);
/*!40000 ALTER TABLE `fuerza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genero`
--

DROP TABLE IF EXISTS `genero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genero` (
  `id_genero` int NOT NULL AUTO_INCREMENT,
  `Genero` varchar(45) NOT NULL,
  PRIMARY KEY (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genero`
--

LOCK TABLES `genero` WRITE;
/*!40000 ALTER TABLE `genero` DISABLE KEYS */;
INSERT INTO `genero` VALUES (1,'Masculino'),(2,'Femenino');
/*!40000 ALTER TABLE `genero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `objetivos`
--

DROP TABLE IF EXISTS `objetivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `objetivos` (
  `id_objetivos` int NOT NULL AUTO_INCREMENT,
  `intensidad` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `parte` varchar(45) NOT NULL,
  `repeticiones` int NOT NULL,
  PRIMARY KEY (`id_objetivos`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `objetivos`
--

LOCK TABLES `objetivos` WRITE;
/*!40000 ALTER TABLE `objetivos` DISABLE KEYS */;
INSERT INTO `objetivos` VALUES (1,1,'Extension de codos','Bicep',10),(2,2,'Extension de codos','Bicep',15),(3,3,'Extension de codos','Bicep',20),(4,1,'Martillo con mancuerna','Bicep',10),(5,2,'Martillo con mancuerna','Bicep',15),(6,3,'Martillo con mancuerna','Bicep',20),(7,1,'Predicador con barra','Bicep',10),(8,2,'Predicador con barra','Bicep',15),(9,3,'Predicador con barra','Bicep',20),(10,1,'Pechadas','Pecho',10),(11,2,'Pechadas','Pecho',15),(12,3,'Pechadas','Pecho',20),(13,1,'Pull Over','Pecho',10),(14,2,'Pull Over','Pecho',15),(15,3,'Pull Over','Pecho',20),(16,1,'Peck deck','Pecho',10),(17,2,'Peck deck','Pecho',15),(18,3,'Peck deck','Pecho',20),(19,1,'Crunch','Abdomen',10),(20,2,'Crunch','Abdomen',15),(21,3,'Crunch','Abdomen',20),(22,1,'Elevaciones de piernas','Abdomen',10),(23,2,'Elevaciones de piernas','Abdomen',15),(24,3,'Elevaciones de piernas','Abdomen',20),(25,1,'Codo a la rodilla','Abdomen',10),(26,2,'Codo a la rodilla','Abdomen',15),(27,3,'Codo a la rodilla','Abdomen',20),(28,1,'Copa','Tricep',10),(29,2,'Copa','Tricep',15),(30,3,'Copa','Tricep',20),(31,1,'Extension de codos','Tricep',10),(32,2,'Extension de codos','Tricep',15),(33,3,'Extension de codos','Tricep',20),(34,1,'Laterales con tronco inclinado','Tricep',10),(35,2,'Laterales con tronco inclinado','Tricep',15),(36,3,'Laterales con tronco inclinado','Tricep',20),(37,1,'Press militar ','Hombros ',10),(38,2,'Press militar ','Hombros ',15),(39,3,'Press militar ','Hombros ',20),(40,1,'Elevacion frontal','Hombros ',10),(41,2,'Elevacion frontal','Hombros ',15),(42,3,'Elevacion frontal','Hombros ',20),(43,1,'Remo al cuello','Hombros ',10),(44,2,'Remo al cuello ','Hombros ',15),(45,3,'Remo al cuello','Hombros ',20),(46,1,'Sentadillas ','Piernas ',10),(47,2,'Sentadillas ','Piernas ',15),(48,3,'Sentadillas ','Piernas ',20),(49,1,'Desplantes','Piernas ',10),(50,2,'Desplantes','Piernas ',15),(51,3,'Desplantes','Piernas ',20),(52,1,'Zancada lateral','Piernas ',10),(53,2,'Zancada lateral','Piernas ',15),(54,3,'Zancada lateral','Piernas ',20),(55,1,'Elevacion de pelvis ','Gluteos',10),(56,2,'Elevacion de pelvis ','Gluteos',15),(57,3,'Elevacion de pelvis ','Gluteos',20),(58,1,'Sentadilla sumo','Gluteos',10),(59,2,'Sentadilla sumo','Gluteos',15),(60,3,'Sentadilla sumo','Gluteos',20),(61,1,'Patada de gluteo en banco','Gluteos',10),(62,2,'Patada de gluteo en banco','Gluteos',15),(63,3,'Patada de gluteo en banco','Gluteos',20);
/*!40000 ALTER TABLE `objetivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `porcion` decimal(10,2) DEFAULT NULL,
  `calorias` decimal(10,4) NOT NULL,
  `grasasTotales` decimal(10,4) NOT NULL,
  `colesterol` decimal(10,4) NOT NULL,
  `sodio` decimal(10,4) NOT NULL,
  `azucares` decimal(10,4) NOT NULL,
  `id_usuario` int DEFAULT '0',
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES (1,'Huevo',50.00,155.0000,10.0000,0.3630,0.0124,1.1000,0),(2,'Carne roja',170.00,130.0000,44.0000,0.8000,0.0397,11.0000,0),(3,'Pollo',150.00,239.0000,14.6000,0.8900,0.0320,0.7000,0),(4,'Aguacate',150.00,160.0000,2.1000,0.0000,0.0700,0.7000,0),(5,'Banano',100.00,122.0000,0.1000,0.0000,0.0400,15.0000,0),(6,'Manzana',80.00,52.0000,0.2000,0.0000,0.0100,10.0000,0),(7,'Pera',90.00,57.0000,0.0000,0.0000,0.0100,10.0000,0),(8,'Melocoton',85.00,39.0000,0.0000,0.0000,0.0000,8.0000,0),(9,'Tortilla maiz',24.00,64.0000,0.5000,0.0000,0.2000,0.2500,0),(10,'Yogurt',227.00,59.0000,0.1000,0.5000,0.0360,3.2000,0),(11,'Avena',40.00,350.0000,6.5200,0.3700,0.0280,4.7000,0),(12,'Brocoli',50.00,7.0000,0.9000,0.2600,0.0700,1.8000,0),(13,'Arroz integral',100.00,111.0000,0.2000,0.0000,0.0500,0.4000,0),(14,'Nueces',30.00,200.0000,13.0000,0.7400,0.0200,4.2000,0),(15,'Pescado',84.00,206.0000,6.0000,0.6300,0.0600,1.2000,0),(16,'Zanahoria',100.00,37.0000,0.2400,0.9300,0.0610,4.2400,0),(17,'Lechuga',30.00,15.0000,0.0000,0.0000,0.0028,0.8000,0),(18,'Pepino',100.00,16.0000,0.0000,0.0000,0.0010,0.5000,0),(19,'Tomate',90.00,18.0000,0.0000,0.0000,0.0050,2.6000,0),(20,'Naranjas',100.00,40.0000,0.1200,0.1100,0.0010,2.3000,0),(21,'Arroz',90.00,200.0000,0.5000,0.0000,0.1000,0.7000,0),(22,'Papa',100.00,70.0000,0.1000,0.0000,0.0400,1.8000,0),(23,'Pizza',100.00,266.0000,4.5000,0.0200,0.5700,3.6000,0),(24,'Hamburguesa',100.00,222.0000,14.0000,0.0200,0.6200,4.2000,0),(25,'Atun',100.00,200.0000,12.0000,0.0400,0.0200,0.0000,0),(26,'Jamon',100.00,240.0000,11.0000,0.0700,0.0100,0.0000,0),(27,'Chocolate',100.00,600.0000,14.0000,0.0000,0.2300,25.0000,0),(28,'Salami',100.00,250.0000,30.0000,0.0900,0.0900,0.0000,0),(29,'Pavo',100.00,104.0000,8.5000,0.0400,0.0100,18.0000,0),(30,'Cerdo',85.00,159.0000,15.0000,0.0900,0.0180,0.0000,0),(31,'Granola',50.00,236.0000,4.0000,0.0000,0.0100,14.5000,1),(32,'Cereales',100.00,120.0000,2.0000,0.0000,0.0000,15.0000,1),(33,'Hongos',45.00,15.0000,0.1700,0.0000,0.0100,0.0000,1),(34,'Pancakes',100.00,368.0000,3.1000,0.0200,0.0010,16.0000,1),(35,'Arandanos',50.00,30.0000,0.0000,0.0000,0.0000,2.0000,0),(36,'Cebolla',45.00,25.0000,0.0000,0.0000,0.0000,0.0000,0),(37,'Remolacha',60.00,15.0000,0.0000,0.0000,0.0000,0.0100,0),(38,'Frambuesas',50.00,40.0000,0.0000,0.0000,0.0000,2.0000,3),(39,'Ciruelas',50.00,55.0000,0.0000,0.0000,0.0000,3.7800,3),(40,'Piña',50.00,60.0000,0.0000,0.0000,0.0000,2.0000,0),(41,'Galletas',100.00,450.0000,1.1000,0.0700,0.9000,11.0000,0),(42,'Pastas',100.00,370.0000,3.5000,0.6700,0.0400,0.0500,3),(43,'Helado',50.00,400.0000,0.7000,0.1000,0.0100,15.0000,3),(44,'Uva',40.00,100.0000,0.0000,0.0000,0.0000,5.0000,3),(45,'Queso Fresco',50.00,120.0000,3.2200,0.6000,0.0900,0.0000,0),(46,'Queso Duro',50.00,150.0000,5.0000,0.5600,0.1500,0.0000,5),(47,'Tocino',70.00,170.0000,9.0000,1.0000,0.0800,0.0000,0),(48,'Tortilla',20.00,40.0000,0.0000,0.0000,0.0500,0.0000,5),(49,'Miel',30.00,100.0000,0.5000,0.0000,0.0000,13.9800,5),(50,'Pan Integral',40.00,90.0000,1.0000,0.0200,0.0100,1.0000,5),(51,'Sushi',100.00,148.0000,14.0000,0.0070,0.0580,2.6800,1),(52,'Fettuccine',100.00,99.0000,2.7000,0.0140,0.1660,1.3000,5),(53,'Paella',400.00,540.0000,20.0000,0.0620,1.2000,10.4000,1),(54,'Tacos',100.00,226.0000,13.0000,0.0280,0.3970,0.9000,5),(55,'Pupusas',100.00,256.0000,13.0000,0.0320,0.4000,1.2000,1),(56,'Lasagna',100.00,135.0000,4.9000,0.0170,0.3730,3.1000,3),(57,'Bagel',100.00,250.0000,1.5000,0.0000,0.4390,6.0000,5),(58,'Ensalada Caecars',100.00,44.0000,2.1000,0.0050,0.0830,2.1000,3),(59,'Lomo relleno',85.00,125.0000,3.4000,0.0620,0.1000,0.0000,3);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrodiario`
--

DROP TABLE IF EXISTS `registrodiario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrodiario` (
  `id_registro` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `pesoActual` decimal(10,2) NOT NULL,
  `cintura` decimal(10,2) NOT NULL,
  `cuello` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id_registro`,`id_usuario`),
  KEY `fk_RegistroDiario_Usuario1_idx` (`id_usuario`),
  CONSTRAINT `fk_RegistroDiario_Usuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrodiario`
--

LOCK TABLES `registrodiario` WRITE;
/*!40000 ALTER TABLE `registrodiario` DISABLE KEYS */;
INSERT INTO `registrodiario` VALUES (1,1,75.00,80.00,34.00,'2020-11-10'),(2,1,74.50,79.00,34.00,'2020-11-13'),(3,1,74.00,79.00,34.00,'2020-11-15'),(4,1,73.60,78.00,33.00,'2020-11-19'),(5,1,74.20,79.00,33.00,'2020-11-21'),(6,1,73.80,78.00,33.00,'2020-11-23'),(7,1,73.20,77.00,32.00,'2020-11-26'),(8,1,72.80,76.00,32.00,'2020-11-28'),(9,1,72.30,76.00,32.00,'2020-12-01'),(10,1,71.90,75.00,31.00,'2020-12-05'),(14,2,80.00,90.00,36.00,'2020-11-10'),(15,2,80.40,90.00,36.00,'2020-11-13'),(16,2,80.10,89.00,36.00,'2020-11-15'),(17,2,80.30,90.00,35.00,'2020-11-19'),(18,2,79.60,89.00,35.00,'2020-11-21'),(19,2,79.10,89.00,35.00,'2020-11-23'),(20,2,78.40,88.00,34.00,'2020-11-26'),(21,2,78.00,87.00,34.00,'2020-11-28'),(22,2,77.20,87.00,34.00,'2020-12-01'),(23,2,76.60,86.00,33.00,'2020-12-05'),(24,3,40.00,50.00,25.00,'2020-11-10'),(25,3,40.20,51.00,25.00,'2020-11-13'),(26,3,40.40,51.00,25.00,'2020-11-15'),(27,3,40.90,51.00,26.00,'2020-11-19'),(28,3,41.30,52.00,26.00,'2020-11-21'),(29,3,41.60,52.00,26.00,'2020-11-23'),(30,3,42.00,52.00,27.00,'2020-11-26'),(31,3,42.30,53.00,27.00,'2020-11-28'),(32,3,42.50,53.00,28.00,'2020-12-01'),(33,3,42.90,54.00,28.00,'2020-12-05'),(34,4,60.00,70.00,31.00,'2020-11-16'),(35,4,60.10,70.00,31.00,'2020-11-17'),(36,4,60.20,71.00,32.00,'2020-11-21'),(37,4,60.10,70.00,31.00,'2020-11-23'),(38,4,60.05,70.00,31.00,'2020-11-26'),(39,4,59.95,69.00,31.00,'2020-11-30'),(40,4,59.90,69.00,31.00,'2020-12-02'),(41,4,59.50,68.00,30.00,'2020-12-03'),(42,4,59.80,69.00,31.00,'2020-12-04'),(43,4,60.10,70.00,31.00,'2020-12-07'),(44,5,110.00,100.00,40.00,'2020-11-10'),(45,5,109.80,100.00,40.00,'2020-11-13'),(46,5,109.40,99.00,40.00,'2020-11-15'),(47,5,109.10,99.00,40.00,'2020-11-19'),(48,5,108.90,98.00,39.00,'2020-11-21'),(49,5,108.50,97.00,39.00,'2020-11-23'),(50,5,108.20,97.00,39.00,'2020-11-26'),(51,5,107.70,97.00,39.00,'2020-11-28'),(52,5,107.30,96.00,38.00,'2020-12-01'),(53,5,106.80,95.00,38.00,'2020-12-05');
/*!40000 ALTER TABLE `registrodiario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrousuarioejerciciocardio`
--

DROP TABLE IF EXISTS `registrousuarioejerciciocardio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrousuarioejerciciocardio` (
  `id_registroUsuarioCardio` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_ejercicio` int NOT NULL,
  `tiempoTotalEmpleado` int NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id_registroUsuarioCardio`,`id_usuario`,`id_ejercicio`),
  KEY `fk_EjercicioUsuario_InformacionUsuario1_idx` (`id_usuario`),
  KEY `fk_EjercicioUsuario_cardio_Cardiovascular1_idx` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_cardio_Cardiovascular1` FOREIGN KEY (`id_ejercicio`) REFERENCES `cardiovascular` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_InformacionUsuario10` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrousuarioejerciciocardio`
--

LOCK TABLES `registrousuarioejerciciocardio` WRITE;
/*!40000 ALTER TABLE `registrousuarioejerciciocardio` DISABLE KEYS */;
INSERT INTO `registrousuarioejerciciocardio` VALUES (1,1,1,5,'2020-11-29'),(2,1,6,10,'2020-11-29'),(3,1,5,5,'2020-11-29'),(4,1,1,3,'2020-11-25'),(5,1,4,5,'2020-11-25'),(6,1,10,4,'2020-11-25'),(7,1,2,2,'2020-11-20'),(8,1,3,5,'2020-11-20'),(9,1,7,20,'2020-11-20'),(10,1,9,10,'2020-11-19'),(11,1,1,5,'2020-11-19'),(12,1,6,5,'2020-11-19'),(13,1,1,10,'2020-11-27'),(14,1,3,10,'2020-11-27'),(15,1,12,10,'2020-11-27'),(16,1,15,5,'2020-11-28'),(17,1,18,10,'2020-11-28'),(18,1,20,10,'2020-11-28'),(19,1,19,15,'2020-11-29'),(20,1,3,10,'2020-11-29'),(21,1,11,10,'2020-11-29'),(22,1,10,5,'2020-11-30'),(23,1,6,5,'2020-11-30'),(24,1,9,10,'2020-11-30'),(25,1,12,5,'2020-12-01'),(26,1,17,5,'2020-12-01'),(27,1,15,10,'2020-12-01'),(28,1,16,10,'2020-12-02'),(29,1,11,5,'2020-12-02'),(30,1,7,5,'2020-12-02'),(31,1,4,5,'2020-12-03'),(32,1,19,10,'2020-12-03'),(33,1,17,5,'2020-12-03'),(34,1,23,5,'2020-12-04'),(35,1,16,5,'2020-12-04'),(36,1,9,10,'2020-12-04'),(37,1,5,25,'2020-12-05'),(38,1,7,20,'2020-12-05'),(39,1,13,15,'2020-12-06'),(40,1,15,25,'2020-12-07'),(41,2,1,5,'2020-11-29'),(42,2,6,10,'2020-11-29'),(43,2,5,5,'2020-11-29'),(44,2,1,3,'2020-11-25'),(45,2,4,5,'2020-11-25'),(46,2,10,4,'2020-11-25'),(47,2,2,2,'2020-11-20'),(48,2,3,5,'2020-11-20'),(49,2,7,20,'2020-11-20'),(50,2,9,10,'2020-11-19'),(51,2,1,5,'2020-11-19'),(52,2,6,5,'2020-11-19'),(53,2,1,10,'2020-11-27'),(54,2,3,10,'2020-11-27'),(55,2,12,10,'2020-11-27'),(56,2,15,5,'2020-11-28'),(57,2,18,10,'2020-11-28'),(58,2,20,10,'2020-11-28'),(59,2,19,15,'2020-11-29'),(60,2,3,10,'2020-11-29'),(61,2,11,10,'2020-11-29'),(62,2,10,5,'2020-11-30'),(63,2,6,5,'2020-11-30'),(64,2,9,10,'2020-11-30'),(65,2,12,5,'2020-12-01'),(66,2,17,5,'2020-12-01'),(67,2,15,10,'2020-12-01'),(68,2,16,10,'2020-12-02'),(69,2,11,5,'2020-12-02'),(70,2,7,5,'2020-12-02'),(71,2,4,5,'2020-12-03'),(72,2,19,10,'2020-12-03'),(73,2,17,5,'2020-12-03'),(74,2,23,5,'2020-12-04'),(75,2,16,5,'2020-12-04'),(76,2,9,10,'2020-12-04'),(77,2,5,25,'2020-12-05'),(78,2,7,20,'2020-12-05'),(79,2,13,15,'2020-12-06'),(80,2,15,25,'2020-12-07'),(81,3,1,5,'2020-11-29'),(82,3,6,10,'2020-11-29'),(83,3,5,5,'2020-11-29'),(84,3,1,3,'2020-11-25'),(85,3,4,5,'2020-11-25'),(86,3,10,4,'2020-11-25'),(87,3,2,2,'2020-11-20'),(88,3,3,5,'2020-11-20'),(89,3,7,20,'2020-11-20'),(90,3,9,10,'2020-11-19'),(91,3,1,5,'2020-11-19'),(92,3,6,5,'2020-11-19'),(93,3,1,10,'2020-11-27'),(94,3,3,10,'2020-11-27'),(95,3,12,10,'2020-11-27'),(96,3,15,5,'2020-11-28'),(97,3,18,10,'2020-11-28'),(98,3,20,10,'2020-11-28'),(99,3,19,15,'2020-11-29'),(100,3,3,10,'2020-11-29'),(101,3,11,10,'2020-11-29'),(102,3,10,5,'2020-11-30'),(103,3,6,5,'2020-11-30'),(104,3,9,10,'2020-11-30'),(105,3,12,5,'2020-12-01'),(106,3,17,5,'2020-12-01'),(107,3,15,10,'2020-12-01'),(108,3,16,10,'2020-12-02'),(109,3,11,5,'2020-12-02'),(110,3,7,5,'2020-12-02'),(111,3,4,5,'2020-12-03'),(112,3,19,10,'2020-12-03'),(113,3,17,5,'2020-12-03'),(114,3,23,5,'2020-12-04'),(115,3,16,5,'2020-12-04'),(116,3,9,10,'2020-12-04'),(117,3,5,25,'2020-12-05'),(118,3,7,20,'2020-12-05'),(119,3,13,15,'2020-12-06'),(120,3,15,25,'2020-12-07'),(121,4,1,5,'2020-11-29'),(122,4,6,10,'2020-11-29'),(123,4,5,5,'2020-11-29'),(133,4,1,10,'2020-11-27'),(134,4,3,10,'2020-11-27'),(135,4,12,10,'2020-11-27'),(136,4,15,5,'2020-11-28'),(137,4,18,10,'2020-11-28'),(138,4,20,10,'2020-11-28'),(139,4,19,15,'2020-11-29'),(140,4,3,10,'2020-11-29'),(141,4,11,10,'2020-11-29'),(142,4,10,5,'2020-11-30'),(143,4,6,5,'2020-11-30'),(144,4,9,10,'2020-11-30'),(145,4,12,5,'2020-12-01'),(146,4,17,5,'2020-12-01'),(147,4,15,10,'2020-12-01'),(148,4,16,10,'2020-12-02'),(149,4,11,5,'2020-12-02'),(150,4,7,5,'2020-12-02'),(151,4,4,5,'2020-12-03'),(152,4,19,10,'2020-12-03'),(153,4,17,5,'2020-12-03'),(154,4,23,5,'2020-12-04'),(155,4,16,5,'2020-12-04'),(156,4,9,10,'2020-12-04'),(157,4,5,25,'2020-12-05'),(158,4,7,20,'2020-12-05'),(159,4,13,15,'2020-12-06'),(160,4,15,25,'2020-12-07'),(161,5,1,5,'2020-11-29'),(162,5,6,10,'2020-11-29'),(163,5,5,5,'2020-11-29'),(164,5,1,3,'2020-11-25'),(165,5,4,5,'2020-11-25'),(166,5,10,4,'2020-11-25'),(167,5,2,2,'2020-11-20'),(168,5,3,5,'2020-11-20'),(169,5,7,20,'2020-11-20'),(170,5,9,10,'2020-11-19'),(171,5,1,5,'2020-11-19'),(172,5,6,5,'2020-11-19'),(173,5,1,10,'2020-11-27'),(174,5,3,10,'2020-11-27'),(175,5,12,10,'2020-11-27'),(176,5,15,5,'2020-11-28'),(177,5,18,10,'2020-11-28'),(178,5,20,10,'2020-11-28'),(179,5,19,15,'2020-11-29'),(180,5,3,10,'2020-11-29'),(181,5,11,10,'2020-11-29'),(182,5,10,5,'2020-11-30'),(183,5,6,5,'2020-11-30'),(184,5,9,10,'2020-11-30'),(185,5,12,5,'2020-12-01'),(186,5,17,5,'2020-12-01'),(187,5,15,10,'2020-12-01'),(188,5,16,10,'2020-12-02'),(189,5,11,5,'2020-12-02'),(190,5,7,5,'2020-12-02'),(191,5,4,5,'2020-12-03'),(192,5,19,10,'2020-12-03'),(193,5,17,5,'2020-12-03'),(194,5,23,5,'2020-12-04'),(195,5,16,5,'2020-12-04'),(196,5,9,10,'2020-12-04'),(197,5,5,25,'2020-12-05'),(198,5,7,20,'2020-12-05'),(199,5,13,15,'2020-12-06'),(200,5,15,25,'2020-12-07');
/*!40000 ALTER TABLE `registrousuarioejerciciocardio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `registrousuarioejerciciofuerza`
--

DROP TABLE IF EXISTS `registrousuarioejerciciofuerza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registrousuarioejerciciofuerza` (
  `id_registroUsuarioFuerza` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_ejercicio` int NOT NULL,
  `repeticiones` int NOT NULL,
  `series` int NOT NULL,
  `pesoAplicado` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL,
  PRIMARY KEY (`id_registroUsuarioFuerza`,`id_usuario`,`id_ejercicio`),
  KEY `fk_EjercicioUsuario_InformacionUsuario1_idx` (`id_usuario`),
  KEY `fk_EjercicioUsuario_Ejercicios1_idx` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_Ejercicios1` FOREIGN KEY (`id_ejercicio`) REFERENCES `fuerza` (`id_ejercicio`),
  CONSTRAINT `fk_EjercicioUsuario_InformacionUsuario1` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=160 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registrousuarioejerciciofuerza`
--

LOCK TABLES `registrousuarioejerciciofuerza` WRITE;
/*!40000 ALTER TABLE `registrousuarioejerciciofuerza` DISABLE KEYS */;
INSERT INTO `registrousuarioejerciciofuerza` VALUES (1,1,1,20,2,5.00,'2020-11-29'),(2,1,7,1,1,0.00,'2020-11-29'),(3,1,10,10,3,10.00,'2020-11-29'),(4,1,4,20,2,10.00,'2020-11-25'),(5,1,8,10,4,2.00,'2020-11-25'),(6,1,9,20,3,20.00,'2020-11-25'),(7,1,4,15,3,10.00,'2020-11-19'),(8,1,5,15,2,15.00,'2020-11-19'),(9,1,6,10,3,10.00,'2020-11-19'),(10,1,9,10,4,10.00,'2020-11-19'),(11,1,3,20,1,5.00,'2020-11-19'),(12,1,10,10,2,10.00,'2020-11-19'),(13,1,6,10,3,10.00,'2020-11-23'),(14,1,8,10,2,10.00,'2020-11-23'),(15,1,7,1,1,0.00,'2020-11-23'),(16,1,4,10,10,5.00,'2020-11-27'),(17,1,14,10,3,2.00,'2020-11-27'),(18,1,13,10,5,10.00,'2020-11-27'),(19,1,10,10,5,5.00,'2020-11-28'),(20,1,9,5,5,0.00,'2020-11-28'),(21,1,8,10,10,2.00,'2020-11-28'),(22,1,8,10,5,2.00,'2020-11-29'),(23,1,12,5,4,5.00,'2020-11-29'),(24,1,10,10,6,4.00,'2020-11-29'),(25,1,11,10,3,1.00,'2020-11-30'),(26,1,5,5,4,5.00,'2020-11-30'),(27,1,7,1,1,0.00,'2020-12-01'),(28,1,9,10,5,2.00,'2020-12-01'),(29,1,4,10,4,2.00,'2020-12-02'),(29,1,10,10,6,5.00,'2020-12-02'),(30,1,7,1,1,0.00,'2020-12-03'),(31,1,15,10,3,4.00,'2020-12-03'),(32,2,1,20,2,5.00,'2020-11-29'),(33,2,7,1,1,0.00,'2020-11-29'),(34,2,10,10,3,10.00,'2020-11-29'),(35,2,4,20,2,10.00,'2020-11-25'),(36,2,8,10,4,2.00,'2020-11-25'),(37,2,9,20,3,20.00,'2020-11-25'),(38,2,4,15,3,10.00,'2020-11-19'),(39,2,5,15,2,15.00,'2020-11-19'),(40,2,6,10,3,10.00,'2020-11-19'),(41,2,9,10,4,10.00,'2020-11-19'),(42,2,3,20,1,5.00,'2020-11-19'),(43,2,10,10,2,10.00,'2020-11-19'),(44,2,6,10,3,10.00,'2020-11-23'),(45,2,8,10,2,10.00,'2020-11-23'),(46,2,7,1,1,0.00,'2020-11-23'),(47,2,4,10,10,5.00,'2020-11-27'),(48,2,14,10,3,2.00,'2020-11-27'),(49,2,13,10,5,10.00,'2020-11-27'),(50,2,10,10,5,5.00,'2020-11-28'),(51,2,9,5,5,0.00,'2020-11-28'),(52,2,8,10,10,2.00,'2020-11-28'),(53,2,8,10,5,2.00,'2020-11-29'),(54,2,12,5,4,5.00,'2020-11-29'),(55,2,10,10,6,4.00,'2020-11-29'),(56,2,11,10,3,1.00,'2020-11-30'),(57,2,5,5,4,5.00,'2020-11-30'),(58,2,7,1,1,0.00,'2020-12-01'),(59,2,9,10,5,2.00,'2020-12-01'),(60,2,4,10,4,2.00,'2020-12-02'),(61,2,10,10,6,5.00,'2020-12-02'),(62,2,7,1,1,0.00,'2020-12-03'),(63,3,15,10,3,4.00,'2020-12-03'),(64,3,1,20,2,5.00,'2020-11-29'),(65,3,7,1,1,0.00,'2020-11-29'),(66,3,10,10,3,10.00,'2020-11-29'),(67,3,4,20,2,10.00,'2020-11-25'),(68,3,8,10,4,2.00,'2020-11-25'),(69,3,9,20,3,20.00,'2020-11-25'),(70,3,4,15,3,10.00,'2020-11-19'),(71,3,5,15,2,15.00,'2020-11-19'),(72,3,6,10,3,10.00,'2020-11-19'),(73,3,9,10,4,10.00,'2020-11-19'),(74,3,3,20,1,5.00,'2020-11-19'),(75,3,10,10,2,10.00,'2020-11-19'),(76,3,6,10,3,10.00,'2020-11-23'),(77,3,8,10,2,10.00,'2020-11-23'),(78,3,7,1,1,0.00,'2020-11-23'),(79,3,4,10,10,5.00,'2020-11-27'),(80,3,14,10,3,2.00,'2020-11-27'),(81,3,13,10,5,10.00,'2020-11-27'),(82,3,10,10,5,5.00,'2020-11-28'),(83,3,9,5,5,0.00,'2020-11-28'),(84,3,8,10,10,2.00,'2020-11-28'),(85,3,8,10,5,2.00,'2020-11-29'),(86,3,12,5,4,5.00,'2020-11-29'),(87,3,10,10,6,4.00,'2020-11-29'),(88,3,11,10,3,1.00,'2020-11-30'),(89,3,5,5,4,5.00,'2020-11-30'),(90,3,7,1,1,0.00,'2020-12-01'),(91,3,9,10,5,2.00,'2020-12-01'),(92,3,4,10,4,2.00,'2020-12-02'),(93,3,10,10,6,5.00,'2020-12-02'),(94,3,7,1,1,0.00,'2020-12-03'),(95,4,15,10,3,4.00,'2020-12-03'),(96,4,1,20,2,5.00,'2020-11-29'),(97,4,7,1,1,0.00,'2020-11-29'),(98,4,10,10,3,10.00,'2020-11-29'),(111,4,4,10,10,5.00,'2020-11-27'),(112,4,14,10,3,2.00,'2020-11-27'),(113,4,13,10,5,10.00,'2020-11-27'),(114,4,10,10,5,5.00,'2020-11-28'),(115,4,9,5,5,0.00,'2020-11-28'),(116,4,8,10,10,2.00,'2020-11-28'),(117,4,8,10,5,2.00,'2020-11-29'),(118,4,12,5,4,5.00,'2020-11-29'),(119,4,10,10,6,4.00,'2020-11-29'),(120,4,11,10,3,1.00,'2020-11-30'),(121,4,5,5,4,5.00,'2020-11-30'),(122,4,7,1,1,0.00,'2020-12-01'),(123,4,9,10,5,2.00,'2020-12-01'),(124,4,4,10,4,2.00,'2020-12-02'),(125,4,10,10,6,5.00,'2020-12-02'),(126,4,7,1,1,0.00,'2020-12-03'),(127,5,15,10,3,4.00,'2020-12-03'),(128,5,1,20,2,5.00,'2020-11-29'),(129,5,7,1,1,0.00,'2020-11-29'),(130,5,10,10,3,10.00,'2020-11-29'),(131,5,4,20,2,10.00,'2020-11-25'),(132,5,8,10,4,2.00,'2020-11-25'),(133,5,9,20,3,20.00,'2020-11-25'),(134,5,4,15,3,10.00,'2020-11-19'),(135,5,5,15,2,15.00,'2020-11-19'),(136,5,6,10,3,10.00,'2020-11-19'),(137,5,9,10,4,10.00,'2020-11-19'),(138,5,3,20,1,5.00,'2020-11-19'),(139,5,10,10,2,10.00,'2020-11-19'),(140,5,6,10,3,10.00,'2020-11-23'),(141,5,8,10,2,10.00,'2020-11-23'),(142,5,7,1,1,0.00,'2020-11-23'),(143,5,4,10,10,5.00,'2020-11-27'),(144,5,14,10,3,2.00,'2020-11-27'),(145,5,13,10,5,10.00,'2020-11-27'),(146,5,10,10,5,5.00,'2020-11-28'),(147,5,9,5,5,0.00,'2020-11-28'),(148,5,8,10,10,2.00,'2020-11-28'),(149,5,8,10,5,2.00,'2020-11-29'),(150,5,12,5,4,5.00,'2020-11-29'),(151,5,10,10,6,4.00,'2020-11-29'),(152,5,11,10,3,1.00,'2020-11-30'),(153,5,5,5,4,5.00,'2020-11-30'),(154,5,7,1,1,0.00,'2020-12-01'),(155,5,9,10,5,2.00,'2020-12-01'),(156,5,4,10,4,2.00,'2020-12-02'),(157,5,10,10,6,5.00,'2020-12-02'),(158,5,7,1,1,0.00,'2020-12-03'),(159,5,15,10,3,4.00,'2020-12-03');
/*!40000 ALTER TABLE `registrousuarioejerciciofuerza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `user` varchar(45) NOT NULL,
  `contra` varchar(45) NOT NULL,
  `id_genero` int NOT NULL,
  `altura` decimal(10,2) NOT NULL,
  `pesoActual` decimal(10,2) NOT NULL,
  `pesoDeseado` decimal(10,2) NOT NULL,
  `nacimiento` date NOT NULL,
  `premium` datetime DEFAULT NULL,
  `intensidad` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id_usuario`,`id_genero`),
  UNIQUE KEY `usuario_UNIQUE` (`user`),
  UNIQUE KEY `correo_UNIQUE` (`correo`),
  KEY `fk_Usuario_Genero1_idx` (`id_genero`),
  CONSTRAINT `fk_Usuario_Genero1` FOREIGN KEY (`id_genero`) REFERENCES `genero` (`id_genero`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Sofia','Gomez','sofia@gmail.com','sofia','12345',2,1.75,71.90,70.00,'2001-03-28','2021-01-07 00:00:00',2),(2,'Alberto','Caceres','caceres@gmail.com','alberto','67890',1,1.70,76.60,70.00,'1999-09-06','2020-11-16 00:00:00',3),(3,'Valeria','Flores','vale@gmail.com','valeria','12345',2,1.50,42.90,48.00,'2000-08-20','2021-01-07 00:00:00',1),(4,'Juan','Ramírez','juan@gmail.com','juan','67890',1,1.60,60.10,60.00,'1997-02-06','2020-11-27 00:00:00',1),(5,'Erick','Olmedo','erick@gmail.com','erick','12345',1,1.80,106.80,82.00,'2000-08-10','2021-01-07 00:00:00',2);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-08 16:10:01
