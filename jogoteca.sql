-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 18/08/2023 às 16:50
-- Versão do servidor: 8.0.31
-- Versão do PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `jogoteca`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `jogo`
--

DROP TABLE IF EXISTS `jogo`;
CREATE TABLE IF NOT EXISTS `jogo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `categoria` varchar(40) NOT NULL,
  `console` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `jogo`
--

INSERT INTO `jogo` (`id`, `nome`, `categoria`, `console`) VALUES
(1, 'Counter Strike Global Offensivee', 'FPS', 'PC'),
(2, 'Valorant', 'FPS', 'PC');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `nome` varchar(20) NOT NULL,
  `nickname` varchar(8) NOT NULL,
  `senha` varchar(100) NOT NULL,
  PRIMARY KEY (`nickname`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `usuario`
--

INSERT INTO `usuario` (`nome`, `nickname`, `senha`) VALUES
('Leonardo Calheiros', 'lzn', '123'),
('Camila Silva', 'mila', '1234');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
