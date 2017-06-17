-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 06-06-2017 a las 19:29:17
-- Versión del servidor: 10.1.21-MariaDB
-- Versión de PHP: 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `FisFinder`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Feedback`
--

CREATE TABLE `Feedback` (
  `ID` int(6) NOT NULL,
  `id_Perfil` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Perfil`
--

CREATE TABLE `Perfil` (
  `ID` varchar(12) CHARACTER SET latin1 COLLATE latin1_spanish_ci NOT NULL,
  `Nro_IMG` int(5) NOT NULL DEFAULT '0',
  `Nro_VIDEO` int(5) NOT NULL DEFAULT '0',
  `Nro_ECC` int(5) NOT NULL DEFAULT '0',
  `Nro_TEXTO` int(5) NOT NULL DEFAULT '0',
  `Min_IMG` int(5) NOT NULL DEFAULT '0',
  `Min_VIDEO` int(5) NOT NULL DEFAULT '0',
  `Min_ECC` int(5) NOT NULL DEFAULT '0',
  `Min_TEXTO` int(5) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Perfil`
--

INSERT INTO `Perfil` (`ID`, `Nro_IMG`, `Nro_VIDEO`, `Nro_ECC`, `Nro_TEXTO`, `Min_IMG`, `Min_VIDEO`, `Min_ECC`, `Min_TEXTO`) VALUES
('ACOMODADOR', 0, 0, 0, 0, 0, 0, 0, 0),
('ASIMILADOR', 4, 0, 0, 89, 0, 0, 0, 0),
('CONVERGENTE', 0, 0, 0, 0, 0, 0, 0, 0),
('DIVERGENTE', 1, 1, 1, 1, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Preferencias_WEB`
--

CREATE TABLE `Preferencias_WEB` (
  `Nombre_Sitio` varchar(30) NOT NULL,
  `Tipo` int(1) NOT NULL,
  `Motivo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `Feedback`
--
ALTER TABLE `Feedback`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `Perfil`
--
ALTER TABLE `Perfil`
  ADD PRIMARY KEY (`ID`) USING BTREE;

--
-- Indices de la tabla `Preferencias_WEB`
--
ALTER TABLE `Preferencias_WEB`
  ADD PRIMARY KEY (`Nombre_Sitio`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
