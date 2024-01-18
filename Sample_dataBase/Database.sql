-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



--
--
CREATE DATABASE IF NOT EXISTS `hang_man` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `hang_man`;

-- --------------------------------------------------------

--
-- Table structure for table `player_data`
--

CREATE TABLE `player_data` (
  `player_name` varchar(30) NOT NULL,
  `play_date` date DEFAULT NULL,
  `play_time` time DEFAULT NULL,
  `word` varchar(20) DEFAULT NULL,
  `turns_provided` int(2) DEFAULT NULL,
  `turns_used` int(2) DEFAULT NULL,
  `status` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `player_data`
--

INSERT INTO `player_data` (`player_name`, `play_date`, `play_time`, `word`, `turns_provided`, `turns_used`, `status`) VALUES
('Induranga', '2021-12-15', '05:32:41', 'speaker', 7, 0, 'WON'),
('Induranga', '2021-12-15', '05:33:09', 'laptop', 6, 6, 'LOST'),
('Kawishwara', '2021-12-15', '05:37:56', 'pencil', 6, 6, 'LOST');
COMMIT;

