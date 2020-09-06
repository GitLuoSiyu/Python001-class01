/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50730
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50730
File Encoding         : 65001

Date: 2020-09-05 11:40:36
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `p_id` varchar(255) DEFAULT NULL,
  `p_name` varchar(255) DEFAULT NULL,
  `p_type` varchar(255) DEFAULT NULL,
  `add_time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pidone234788` (`p_id`) USING HASH
) ENGINE=InnoDB AUTO_INCREMENT=180 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `p_id` varchar(255) NOT NULL,
  `p_name` varchar(255) NOT NULL,
  `c_id` varchar(255) NOT NULL,
  `n_star` int(11) NOT NULL DEFAULT '0',
  `short` varchar(400) NOT NULL DEFAULT '',
  `c_time` varchar(255) NOT NULL,
  `sentiment` float(12,10) NOT NULL DEFAULT '0.0000000000',
  `add_time` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cid` (`c_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1939 DEFAULT CHARSET=utf8;
