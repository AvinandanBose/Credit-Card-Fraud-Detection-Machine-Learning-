-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Dec 20, 2021 at 05:06 AM
-- Server version: 8.0.27
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `creditcard`
--

-- --------------------------------------------------------

--
-- Table structure for table `creditcard`
--

DROP TABLE IF EXISTS `creditcard`;
CREATE TABLE IF NOT EXISTS `creditcard` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Amount` varchar(255) DEFAULT NULL,
  `Time` varchar(255) DEFAULT NULL,
  `Status` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `creditcard`
--

INSERT INTO `creditcard` (`id`, `Amount`, `Time`, `Status`) VALUES
(6, '0.92', '98752.0', 'NORMAL'),
(5, '0.92', '98752.0', 'NORMAL'),
(7, '122.68', '148479.0', 'FRAUD'),
(8, '122.68', '148479.0', 'FRAUD'),
(9, '122.68', '148479.0', 'FRAUD'),
(10, '122.68', '148479.0', 'FRAUD'),
(11, '122.68', '148479.0', 'FRAUD'),
(12, '122.68', '148479.0', 'FRAUD'),
(13, '122.68', '148479.0', 'FRAUD');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
