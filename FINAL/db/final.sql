-- MySQL Script generated by MySQL Workbench
-- Sun Nov 29 21:31:32 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema final
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `final` ;

-- -----------------------------------------------------
-- Schema final
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `final` DEFAULT CHARACTER SET utf8 ;
USE `final` ;

-- -----------------------------------------------------
-- Table `final`.`stock`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `final`.`stock` ;

CREATE TABLE IF NOT EXISTS `final`.`stock` (
  `idstock` INT NOT NULL AUTO_INCREMENT,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`idstock`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final`.`proveedor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `final`.`proveedor` ;

CREATE TABLE IF NOT EXISTS `final`.`proveedor` (
  `idproveedor` INT NOT NULL AUTO_INCREMENT,
  `direccion` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idproveedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `final`.`producto`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `final`.`producto` ;

CREATE TABLE IF NOT EXISTS `final`.`producto` (
  `idproducto` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NULL,
  `proveedor_idproveedor` INT NOT NULL,
  `stock_idstock` INT NOT NULL,
  PRIMARY KEY (`idproducto`),
  INDEX `fk_producto_proveedor_idx` (`proveedor_idproveedor` ASC) ,
  INDEX `fk_producto_stock1_idx` (`stock_idstock` ASC),
  CONSTRAINT `fk_producto_proveedor`
    FOREIGN KEY (`proveedor_idproveedor`)
    REFERENCES `final`.`proveedor` (`idproveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_producto_stock1`
    FOREIGN KEY (`stock_idstock`)
    REFERENCES `final`.`stock` (`idstock`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
