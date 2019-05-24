-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2019-05-16 16:46:15.514

-- tables
-- Table: Evento
CREATE TABLE Evento (
    identificacion varchar(30) NOT NULL CONSTRAINT Evento_pk PRIMARY KEY,
    nombreEvento varchar(20) NOT NULL,
    fecha date NOT NULL,
    lugar varchar(30) NOT NULL
);

-- Table: Organizador
CREATE TABLE Organizador (
    identificacion integer NOT NULL CONSTRAINT Organizador_pk PRIMARY KEY,
    nombre varchar(30) NOT NULL,
    email varchar(30) NOT NULL,
    telefono integer NOT NULL,
    Evento_identificacion varchar(30) NOT NULL,
    CONSTRAINT Organizador_Evento FOREIGN KEY (Evento_identificacion)
    REFERENCES Evento (identificacion)
);

-- Table: Programa
CREATE TABLE Programa (
    codigoRegCalificado varchar(40) NOT NULL CONSTRAINT Programa_pk PRIMARY KEY,
    nombrePrograma varchar(30) NOT NULL,
    duracion integer NOT NULL,
    perfil varchar(30) NOT NULL,
    estadoActual smallint NOT NULL
);

-- Table: Tipo
CREATE TABLE Tipo (
    identificacion integer NOT NULL CONSTRAINT Tipo_pk PRIMARY KEY,
    tipo varchar(25) NOT NULL
);

-- Table: Usuario
CREATE TABLE Usuario (
    identificacion integer NOT NULL CONSTRAINT identificacion PRIMARY KEY,
    nombre varchar(30) NOT NULL,
    email varchar(30) NOT NULL,
    telefono integer NOT NULL,
    contrasena varchar(20) NOT NULL,
    Usuario_identificacion integer NOT NULL,
    CONSTRAINT Usuario_Usuario FOREIGN KEY (Usuario_identificacion)
    REFERENCES Usuario (identificacion)
);

-- Table: Usuario_Evento
CREATE TABLE Usuario_Evento (
    identificacion integer NOT NULL CONSTRAINT Usuario_Evento_pk PRIMARY KEY,
    Usuario_identificacion integer NOT NULL,
    Evento_identificacion varchar(30) NOT NULL,
    CONSTRAINT Usuario_Evento_Usuario FOREIGN KEY (Usuario_identificacion)
    REFERENCES Usuario (identificacion),
    CONSTRAINT Usuario_Evento_Evento FOREIGN KEY (Evento_identificacion)
    REFERENCES Evento (identificacion)
);

-- Table: Usuario_Programa
CREATE TABLE Usuario_Programa (
    identificacion integer NOT NULL CONSTRAINT Usuario_Programa_pk PRIMARY KEY,
    Usuario_identificacion integer NOT NULL,
    Programa_codigoRegCalificado varchar(40) NOT NULL,
    CONSTRAINT Usuario_Programa_Usuario FOREIGN KEY (Usuario_identificacion)
    REFERENCES Usuario (identificacion),
    CONSTRAINT Usuario_Programa_Programa FOREIGN KEY (Programa_codigoRegCalificado)
    REFERENCES Programa (codigoRegCalificado)
);

-- Table: Usuario_Tipo
CREATE TABLE Usuario_Tipo (
    identificacion integer NOT NULL CONSTRAINT Usuario_Tipo_pk PRIMARY KEY,
    Tipo_identificacion integer NOT NULL,
    Usuario_identificacion integer NOT NULL,
    CONSTRAINT Usuario_Tipo_Tipo FOREIGN KEY (Tipo_identificacion)
    REFERENCES Tipo (identificacion),
    CONSTRAINT Usuario_Tipo_Usuario FOREIGN KEY (Usuario_identificacion)
    REFERENCES Usuario (identificacion)
);

-- End of file.

