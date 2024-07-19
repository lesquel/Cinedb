-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-07-2024 a las 18:02:40
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cine`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentarios_peli`
--

CREATE TABLE `comentarios_peli` (
  `id` int(11) NOT NULL,
  `comentario` varchar(500) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_pelicula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comentarios_peli`
--

INSERT INTO `comentarios_peli` (`id`, `comentario`, `id_usuario`, `id_pelicula`) VALUES
(3, 'Muy bueno aaaaahhhh siii', 1, 1),
(4, 'Bacan', 1, 1),
(5, 'siiiiii', 2, 1),
(6, 'Esta buy barato', 2, 1),
(7, 'buena peli', 9, 2),
(8, 'batman es el majro', 9, 2),
(9, 'hola', 2, 1),
(10, 'hola', 2, 1),
(11, 'hola', 2, 1),
(12, 'Esta buena la peli y la sala', 2, 1),
(13, 'este es un buena pelicula', 2, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estrenos`
--

CREATE TABLE `estrenos` (
  `id` int(11) NOT NULL,
  `id_pelicula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estrenos`
--

INSERT INTO `estrenos` (`id`, `id_pelicula`) VALUES
(13, 1),
(14, 3),
(3, 4),
(11, 6),
(12, 57);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `funciones`
--

CREATE TABLE `funciones` (
  `id` int(11) NOT NULL,
  `fecha` varchar(25) NOT NULL,
  `id_salas` int(25) NOT NULL,
  `id_peliculas` int(25) NOT NULL,
  `sillas` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`sillas`))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `funciones`
--

INSERT INTO `funciones` (`id`, `fecha`, `id_salas`, `id_peliculas`, `sillas`) VALUES
(1, '07/06/2024 11:00-12:00', 3, 2, '[[2, 2, 2, 2, 1], [2, \"L\", 2, 2, 2], [\"L\", \"L\", 2, 2, 2], [\"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\"]]'),
(2, '05/06/2024  12:00-13:00', 2, 2, '[[\"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", 9, 9], [\"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\"]]'),
(3, '05/06/2024  15:00-16:00', 1, 1, '[[\"L\", 1, 1, 1, \"L\"], [\"L\", 2, 2, 13, \"L\"], [\"L\", \"L\", 2, 2, \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\"]]'),
(5, '05/06/2024  11:00-12:00', 2, 1, '[[\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", 2, \"L\", \"L\", \"L\"], [\"L\", \"L\", 2, 2, \"L\", \"L\"], [\"L\", \"L\", 2, 2, \"L\", \"L\"], [\"L\", \"L\", 2, 2, \"L\", \"L\"]]'),
(7, '07/06/2024  11:00-12:00', 5, 6, '[[\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\", \"L\", \"L\"]]'),
(44, '08/07/2024', 9, 61, '[[\"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\"], [\"L\", \"L\", \"L\", \"L\"]]');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genero`
--

CREATE TABLE `genero` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `genero`
--

INSERT INTO `genero` (`id`, `nombre`) VALUES
(1, 'Drama'),
(2, 'Comedia'),
(3, 'Fantasía'),
(4, 'Action'),
(5, 'Ciencia Ficción'),
(6, 'Historia'),
(7, 'Misterio'),
(8, 'Romance'),
(9, 'Terror'),
(10, 'Tragedia'),
(11, 'Niños'),
(18, 'Comedia Romantica');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pelicula`
--

CREATE TABLE `pelicula` (
  `id` int(11) NOT NULL,
  `nombre` varchar(500) NOT NULL,
  `img` varchar(500) DEFAULT NULL,
  `descri` varchar(500) DEFAULT NULL,
  `dura` varchar(500) DEFAULT NULL,
  `trailers` varchar(255) DEFAULT NULL,
  `genero_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pelicula`
--

INSERT INTO `pelicula` (`id`, `nombre`, `img`, `descri`, `dura`, `trailers`, `genero_id`) VALUES
(1, 'guardianes de la galaxia', 'https://lumiere-a.akamaihd.net/v1/images/lat_2ae5e247.jpeg', '2', '1', '1', 5),
(2, 'Batman', 'https://play-lh.googleusercontent.com/QNJcWaArp784wtqZjjwfmfQqhIpRhjP0EpB4Wcj_wUZElj2Ie4H-nUeUsepmAV_Mibjb7QnhuNxZcaxoTGc', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae facere exercitationem, similique ducimus provident aliquid eaque, mollitia dicta magni laudantium consequuntur quod nulla perspiciatis sint! Dolorem fugit placeat numquam suscipit.', '1', 'https://www.youtube.com/watch?v=sinstLBy9l8', 4),
(3, 'Los Vengadores', 'https://es.web.img3.acsta.net/pictures/14/03/10/10/35/587504.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae facere exercitationem, similique ducimus provident aliquid eaque, mollitia dicta magni laudantium consequuntur quod nulla perspiciatis sint! Dolorem fugit placeat numquam suscipit.', '1', 'https://www.youtube.com/watch?v=yNXfOOL8824', 4),
(4, '¿Qué pasó ayer?', 'https://static.wikia.nocookie.net/doblaje/images/1/1b/320x200_afiche_quepasoayer2.jpg/revision/latest?cb=20110507013344&path-prefix=es', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae facere exercitationem, similique ducimus provident aliquid eaque, mollitia dicta magni laudantium consequuntur quod nulla perspiciatis sint! Dolorem fugit placeat numquam suscipit.', '1', 'https://www.youtube.com/watch?v=wnNgGp1KVWQ', 1),
(5, 'Son como niños', 'https://m.media-amazon.com/images/S/pv-target-images/7b86f2a7e80941d97c265348873a82c73450c0286ed1d1eeb7d86440ec707de5.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae facere exercitationem, similique ducimus provident aliquid eaque, mollitia dicta magni laudantium consequuntur quod nulla perspiciatis sint! Dolorem fugit placeat numquam suscipit.', '1', 'https://www.youtube.com/watch?v=yMEDiKD7cyE', 2),
(6, 'Vacaciones ', 'https://es.web.img3.acsta.net/pictures/15/07/07/10/57/045335.jpg', 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae facere exercitationem, similique ducimus provident aliquid eaque, mollitia dicta magni laudantium consequuntur quod nulla perspiciatis sint! Dolorem fugit placeat numquam suscipit.', '1', 'https://www.youtube.com/watch?v=KS3i1Kt_y7Q', 2),
(57, 'intensamente 2', 'http://localhost:8080/assets/20240713094353_7d9dd59eb9abb04c8e43494f150af4b7.jpg', 'esta es esta pero la de aca no', '2', 'https://youtu.be/xiC2iXTXHxw', 11),
(60, 'black panther', 'http://localhost:8080/assets/20240715193656_MV5BMTg1MTY2MjYzNV5BMl5BanBnXkFtZTgwMTc4NTMwNDI@._V1_.jpg', 'jhzvhjsdvslkkdksjdgbkjd a gidaslgfljsjfsvdljhlhfsdj', '2', 'https://www.youtube.com/watch?v=xjDjIWPwcPU', 5),
(61, 'Amigos imaginarios', 'http://localhost:8080/assets/20240715193958_Amigos_imaginarios-678535343-large.jpg', 'kjhsjkgkjgksgsdkdsgksdjksdsd', '1', 'https://www.youtube.com/watch?v=I1M9T3uJ7TM', 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `salas`
--

CREATE TABLE `salas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(500) NOT NULL,
  `fillas` int(11) NOT NULL,
  `columnas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `salas`
--

INSERT INTO `salas` (`id`, `nombre`, `fillas`, `columnas`) VALUES
(1, '1', 5, 5),
(2, 'Sala 2', 6, 6),
(3, 'Sala 3', 6, 6),
(5, 'Sala 4', 6, 6),
(8, 'Sala 7', 4, 4),
(9, 'sala 8', 4, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `slider`
--

CREATE TABLE `slider` (
  `id` int(11) NOT NULL,
  `id_pelicula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `slider`
--

INSERT INTO `slider` (`id`, `id_pelicula`) VALUES
(1, 1),
(4, 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nombre` varchar(500) NOT NULL,
  `contra` varchar(500) NOT NULL,
  `img` varchar(255) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `admin` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `nombre`, `contra`, `img`, `edad`, `name`, `correo`, `admin`) VALUES
(1, '1', '1', 'http://localhost:8080/assets/IMG-lokpzirf.jpg', 1, '1', '1@hh.com', 1),
(2, '2', '2', 'http://localhost:8080/assets/IMG-ln3wpcps.jpg', 21, 'Leo Rivas', 'b@gmail.com', 0),
(8, '1', '1', '', 2, '1', '1', 0),
(9, '3', '3', 'http://localhost:8080/assets/20240704091308_20240704090921_IMG-looczl92.jpg', 16, 'Less', 'les@aj.a', 0),
(10, 'hola', 'hola', 'http://localhost:8080/assets/20240713095839_blank-whatsapp-profile-photo-cute-260nw-2273582947.jpg', 12, 'Miquel Muliz', 'a@jaa', 0),
(13, '4', '4', 'http://localhost:8080/assets/IMG-20231007-WA0036.jpg', 0, 'les', 'a', 0);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comentarios_peli`
--
ALTER TABLE `comentarios_peli`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Fk_pelicula` (`id_pelicula`),
  ADD KEY `Fk_usuario` (`id_usuario`);

--
-- Indices de la tabla `estrenos`
--
ALTER TABLE `estrenos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Fk_pelicula` (`id_pelicula`);

--
-- Indices de la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_salas` (`id_salas`),
  ADD KEY `FK_peliculas` (`id_peliculas`);

--
-- Indices de la tabla `genero`
--
ALTER TABLE `genero`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pelicula`
--
ALTER TABLE `pelicula`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_genero` (`genero_id`);

--
-- Indices de la tabla `salas`
--
ALTER TABLE `salas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `slider`
--
ALTER TABLE `slider`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Fk_pelicula` (`id_pelicula`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comentarios_peli`
--
ALTER TABLE `comentarios_peli`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `estrenos`
--
ALTER TABLE `estrenos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `funciones`
--
ALTER TABLE `funciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `genero`
--
ALTER TABLE `genero`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `pelicula`
--
ALTER TABLE `pelicula`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT de la tabla `salas`
--
ALTER TABLE `salas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `slider`
--
ALTER TABLE `slider`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `comentarios_peli`
--
ALTER TABLE `comentarios_peli`
  ADD CONSTRAINT `Fk_pelicula` FOREIGN KEY (`id_pelicula`) REFERENCES `pelicula` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `Fk_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `comentarios_peli_ibfk_2` FOREIGN KEY (`id_pelicula`) REFERENCES `pelicula` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `funciones`
--
ALTER TABLE `funciones`
  ADD CONSTRAINT `funciones_ibfk_1` FOREIGN KEY (`id_salas`) REFERENCES `salas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `funciones_ibfk_2` FOREIGN KEY (`id_peliculas`) REFERENCES `pelicula` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `pelicula`
--
ALTER TABLE `pelicula`
  ADD CONSTRAINT `fk_genero` FOREIGN KEY (`genero_id`) REFERENCES `genero` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
