# Servicio de comprobación de vocales en Render

Este proyecto es un ejemplo sencillo de despliegue de un servicio Python
en la plataforma cloud **Render**.

## Descripción
El servicio recibe un carácter por URL y determina si es una vocal
o no, devolviendo la respuesta en formato JSON.

## Ejemplos de uso

- Vocal:
  /comprobar?caracter=a

- Consonante:
  /comprobar?caracter=b

## Tecnologías usadas
- Python
- Flask
- Render (PaaS)

## Objetivo
Demostrar cómo adaptar un programa de consola a un servicio cloud
sin gestionar infraestructura.
