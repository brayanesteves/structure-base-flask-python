# --------- <ENGLISH: MODULE. PERSONS / SPANISH: MÓDULO. PERSONAS> ----------- #
CREATE TABLE IF NOT EXISTS `MIPSS_`.`0_Personas` (
    `Rfrnc`             INT(255)     NOT NULL AUTO_INCREMENT COMMENT 'Rfrnc (English: Reference / Spanish: Referencia)',
    `cedula`            VARCHAR(20)  NOT NULL                COMMENT '',
    `nombres`           VARCHAR(255) NOT NULL                COMMENT '',
    `apellidos`         VARCHAR(255) NOT NULL                COMMENT '',
    `fechaDeNacimiento` DATE         NOT NULL                COMMENT '',
    PRIMARY KEY (`Rfrnc`)
) ENGINE='InnoDB' DEFAULT CHARSET='utf8' COLLATE='utf8_bin' COMMENT='';