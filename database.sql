-- SQL script to create database schema for app
CREATE DATABASE IF NOT EXISTS med_craft;
--- table name : med_carft_users
CREATE TABLE IF NOT EXISTS med_craft_users(user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, username VARCHAR(200) NOT NULL, firstname VARCHAR(100) NOT NULL, middle_name VARCHAR(100), lastname VARCHAR(100), password VARCHAR(100) NOT NULL, access_token VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL, phone VARCHAR(100) NOT NULL, is_active INT NOT NULL DEFAULT 1,  created_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, update_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL);
--- table name : organizations 
CREATE TABLE IF NOT EXISTS organizations(organizations_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, organizations_name VARCHAR(200) NOT NULL, org_address TEXT NOT NULL, email VARCHAR(200) NOT NULL, phone VARCHAR(20) NOT NULL, is_active TINYINT(1) NOT NULL DEFAULT 1);
--- table name: 
CREATE TABLE IF NOT EXISTS doctors(doctor_id INT NOT NULL PRIMARY KEY, fullname VARCHAR(200) NOT NULL, phone VARCHAR(20) NOT NULL, specialization VARCHAR(200) NOT NULL,hopital_id INT);
-- table name : hospital 
CREATE TABLE IF NOT EXISTS hospital(hospital_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, hospital_name VARCHAR(200) NOT NULL, hospital_addr TEXT NOT NULL, phone VARCHAR(20) NOT NULL, organizations_id INT);
-- table name: patient. 
CREATE TABLE IF NOT EXISTS patients(patient_id INT PRIMARY KEY, patient_name VARCHAR(200) NOT NULL, patient_addr VARCHAR(200) NOT NULL, phone VARCHAR(20) NOT NULL);
