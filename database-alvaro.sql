CREATE DATABASE escuela;

use escuela;
DESCRIBE curso;




CREATE TABLE IF NOT EXISTS curso (
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(100) NOT NULL,
    descripcion VARCHAR(100)
);



CREATE TABLE estudiante(
id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(100),
correo VARCHAR(100),
edad INT,
direccion VARCHAR(255),
telefono VARCHAR(15),
id_curso INT,
FOREIGN KEY (id_curso)REFERENCES curso (id_curso)
);

insert INTO curso(nombre_curso, descripcion)VALUES
('PROGRAMACION', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('DATO', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('HISTORIA', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('PYTHON', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('SQLN', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('HTML', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('CSS', 'CURSO PARA DESARROLLAR APLICACIONES WEB'),
('JAVA', 'CURSO PARA DESARROLLAR APLICACIONES WEB');




insert INTO estudiante(nombre, correo,edad,direccion,telefono,id_curso)VALUES
('Carlos', 'carlos@email.com', 22, 'Av. Siempre Viva 123', '987654321',1),
('Lucia', 'lucia@email.com', 20, 'Calle Falsa 456', '956789012',2),
('Diego', 'diego@email.com', 25, 'Jr. Central 789', '912345678',3),
('Sofia', 'sofia@email.com', 19, 'Pasaje Lima 321', '978901234',4),
('Jorge', 'jorge@email.com', 21, 'Av. Los Olivos 654', '945678901',5),
('Andrea', 'andrea@email.com', 23, 'Calle Sol 987', '934567890',6),
('Pedro', 'pedro@email.com', 26, 'Jr. Las Flores 741', '923456789',7),
('Fernanda', 'fernanda@email.com', 18, 'Av. Primavera 852', '967890123',8),
('Luis', 'luis@email.com', 24, 'Calle Luna 369', '956123789',7),
('Valeria', 'valeria@email.com', 22, 'Pasaje Central 159', '945612378',6);







SELECT * FROM curso;
SELECT * FROM escuela.estudiante;
SELECT id_estudiante, nombre, edad FROM estudiante;
SELECT id_estudiante, nombre, edad FROM estudiante WHERE edad > 32;
SELECT id_estudiante, nombre, edad, direccion FROM estudiante WHERE nombre LIKE 'A%';


SELECT * FROM estudiante;

COMMIT;




