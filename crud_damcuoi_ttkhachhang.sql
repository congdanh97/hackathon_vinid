-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2018 at 05:51 AM
-- Server version: 5.7.14
-- PHP Version: 7.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crud`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `ttkhachhang` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `monney_amount` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `ttkhachhang` (`id`, `name`, `email`, `phone`,`monney_amount`) VALUES
(3, 'Parwiz', 'parwiz.f@gmail.com', '009378976767','5000000'),
(4, 'John Doe', 'johndoe@gmail.com', '999999999','5000000'),
(5, 'Karimja', 'ka@gmail.com', '7333392','5000000'),
(6, 'Jamal', 'ja@gmail.com', '3434343','5000000'),
(7, 'Nawid', 'na@gmail.com', '343434','5000000'),
(8, 'Tom Logan', 'Tom@gmail.com', '7347374347','5000000'),
(12, 'Tom Logan', 'tom@gmail.com', '11111111111','5000000'),
(13, 'Fawad', 'fa@gmail.com', '347374837483','5000000'),
(14, 'Wahid', 'wa@gmail.com', '4354354345','5000000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `ttkhachhang`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `ttkhachhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;



--
-- Table structure for table `students`
--

CREATE TABLE `history_gift` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `monney_gift` int(11) NOT NULL,
  `comment` varchar(255)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `ttkhachhang` (`id`, `name`, `email`, `phone`,`monney_amount`,`comment`) VALUES
(3, 'Parwiz', 'parwiz.f@gmail.com', '009378976767','5000000',""),
(4, 'John Doe', 'johndoe@gmail.com', '999999999','5000000',""),
(5, 'Karimja', 'ka@gmail.com', '7333392','5000000',""),
(6, 'Jamal', 'ja@gmail.com', '3434343','5000000',""),
(7, 'Nawid', 'na@gmail.com', '343434','5000000',""),
(8, 'Tom Logan', 'Tom@gmail.com', '7347374347','5000000',""),
(12, 'Tom Logan', 'tom@gmail.com', '11111111111','5000000',""),
(13, 'Fawad', 'fa@gmail.com', '347374837483','5000000',""),
(14, 'Wahid', 'wa@gmail.com', '4354354345','5000000',"");

--
-- Indexes for dumped tables
--

--
-- Indexes for table `students`
--
ALTER TABLE `ttkhachhang`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `ttkhachhang`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
