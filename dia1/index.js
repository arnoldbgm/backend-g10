//? En NODE se importa con require

const express = require('express');
const { PrismaClient } = require('@prisma/client');

const prisma = new PrismaClient()

// se  va a copiar toda  la funcion de la libreria
const servidor = express();


// con esto le indico a mi servidor que podra convertir la informacion en JSON
// middleware para convertir la informacion en un formato legible
servidor.use(express.json());

// Creacion de la primera  ruta  en NODE
servidor.get('/', (req, res) => {
  // req -> es la informacion que envia el cliente
  // res -> es la informacion que voy a devolver al cliente
  res.json({
    message: 'Bienvenido a mi API',
  });
});

servidor.post('/productos', (req, res) => {
  console.log(req.body);

  res.json({
    message: 'Producto creado exitosamente',
  });
});

servidor.listen(5000, () => {
  console.log('Servido corriendo exitosamente en el puerto 500');
});
