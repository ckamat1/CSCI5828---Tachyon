-- MySQL dump 10.13  Distrib 5.7.15, for Linux (x86_64)
--
-- Host: localhost    Database: student
-- ------------------------------------------------------
-- Server version	5.7.15-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_5675e9a11c08703e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_49dd22144a72e733_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_2d647b8604972d9b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$K8WDe1R6xNgz$gbgmmLoMHQec7h5qjUl3KHmiufUvHB4KCji6D7F7/mA=','2016-10-05 23:48:43',1,'ckamat','','','chka1976@colorado.edu',1,1,'2016-10-05 22:57:49');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_6d2c374e5ff6bf7f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_47bc0bb1150ca4cd_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_3c1448a29bbdc9ba_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissio_user_id_19f94e2789700a9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `avinash`
--

DROP TABLE IF EXISTS `avinash`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `avinash` (
  `test` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avinash`
--

LOCK TABLES `avinash` WRITE;
/*!40000 ALTER TABLE `avinash` DISABLE KEYS */;
/*!40000 ALTER TABLE `avinash` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `djang_content_type_id_4991b409a5a925a0_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_6271a188c8f35f9b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3d86edc9eb5be3af_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-10-03 00:27:16'),(2,'auth','0001_initial','2016-10-03 00:27:17'),(3,'admin','0001_initial','2016-10-03 00:27:17'),(4,'sessions','0001_initial','2016-10-03 00:27:17');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('9f3xmf7ww834oxgi4dllo2b8pw0jzwb1','ODE3NmI5ZTFmY2FiODExN2U2MmFhMWY0YjQwZDg2MTkyYzEyNjU0Nzp7fQ==','2016-10-23 17:10:22'),('g1wgzzucw8ce5st6tj12k0tdqb8vy2ej','ODE3NmI5ZTFmY2FiODExN2U2MmFhMWY0YjQwZDg2MTkyYzEyNjU0Nzp7fQ==','2016-10-26 16:46:40'),('ha0oxtqhkh9xg05sgjin6uuxrw4yyy1a','ODE3NmI5ZTFmY2FiODExN2U2MmFhMWY0YjQwZDg2MTkyYzEyNjU0Nzp7fQ==','2016-10-21 15:29:28'),('vj02sbz7ophvvo6wf9gra0ilyxb5e6x4','MTBiY2YyOWZiMWQ3ZTc3NWJjNDhhNWU0NzY4Y2I5ZTBmZjQwYjFiZDp7Il9hdXRoX3VzZXJfaGFzaCI6IjZkNzQ0OTVmZTYzYTRhMzk3MDA1YTE0NjA0MzU0NGJhNjVlMjVhNGQiLCJfYXV0aF91c2VyX2lkIjoxLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCJ9','2016-10-19 23:48:43');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `faculty` (
  `facultyID` varchar(60) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(40) DEFAULT NULL,
  `department` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `projectID` varchar(10) DEFAULT NULL,
  `faculty_id` varchar(60) DEFAULT NULL,
  `sec_faculty_id` varchar(60) DEFAULT NULL,
  `grad_student_id` varchar(60) DEFAULT NULL,
  `title` varchar(100) DEFAULT NULL,
  `url_link` varchar(200) DEFAULT NULL,
  `special_req` varchar(1500) DEFAULT NULL,
  `long_description` varchar(1500) DEFAULT NULL,
  `depts_applicable` varchar(200) DEFAULT NULL,
  `amount_of_supervision` varchar(200) DEFAULT NULL,
  `supervision_by` varchar(200) DEFAULT NULL,
  `nature_of_work` varchar(200) DEFAULT NULL,
  `prior_work_experience` varchar(200) DEFAULT NULL,
  `desired_studend_id` varchar(200) DEFAULT NULL,
  `speed_type` varchar(200) DEFAULT NULL,
  `accounting_contact` varchar(50) DEFAULT NULL,
  `previous_DLC_exp` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample`
--

DROP TABLE IF EXISTS `sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample` (
  `sample` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample`
--

LOCK TABLES `sample` WRITE;
/*!40000 ALTER TABLE `sample` DISABLE KEYS */;
INSERT INTO `sample` VALUES ('1'),('avinash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash'),('avsgsgash');
/*!40000 ALTER TABLE `sample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `gender` varchar(8) DEFAULT NULL,
  `studentID` varchar(60) DEFAULT NULL,
  `name` varchar(60) DEFAULT NULL,
  `ethnonym` varchar(60) DEFAULT NULL,
  `race` varchar(60) DEFAULT NULL,
  `boulder_phone` varchar(20) DEFAULT NULL,
  `boulder_address` varchar(160) DEFAULT NULL,
  `email_id` varchar(40) DEFAULT NULL,
  `summer_address` varchar(160) DEFAULT NULL,
  `summer_phone` varchar(20) DEFAULT NULL,
  `primary_major` varchar(40) DEFAULT NULL,
  `secondary_major` varchar(40) DEFAULT NULL,
  `gpa` varchar(5) DEFAULT NULL,
  `school_level` varchar(20) DEFAULT NULL,
  `graduation_date` varchar(20) DEFAULT NULL,
  `previous_research_exp` varchar(2) DEFAULT NULL,
  `previous_DLC_apply` varchar(2) DEFAULT NULL,
  `project1` varchar(10) DEFAULT NULL,
  `project2` varchar(10) DEFAULT NULL,
  `project3` varchar(10) DEFAULT NULL,
  `project4` varchar(10) DEFAULT NULL,
  `project5` varchar(10) DEFAULT NULL,
  `background_check` char(2) DEFAULT NULL,
  `DandH_awarness` varchar(2) DEFAULT NULL,
  `SSN` varchar(10) DEFAULT NULL,
  `resume_name` varchar(10) DEFAULT NULL,
  `cover_letter_name` varchar(10) DEFAULT NULL,
  `skills1` varchar(100) DEFAULT NULL,
  `skills2` varchar(100) DEFAULT NULL,
  `skills3` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (' M ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-21  0:01:41
