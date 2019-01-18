#!/usr/bin/env python
# -*- coding: utf-8 -*-

constants = {
  'base_url' : 'http://localhost:3000/',
  'static_url' : 'http://localhost:3000/static/',
  'sistema_id': '3',
  'csrf' : {
    'key': 'csrftoken',
    'secret': 'holamundojejejojo18927389127389123'
  },
  'ambiente_static' : 'desarrollo',
  'ambiente_session' : 'inactivo',
  'ambiente_csrf' : 'activo',
  'ambiente_500' : 'activo',
  'ambiente_error_handler' : 'inactivo',
  'key' : 'Fdp6CVxpri1ga8kH',
  'default_language': 'sp',
}

services = {
  'accesos' : {
    'url': 'http://localhost:4000/',
    'key': 'csrf_val',
    'secret': 'PKBcauXg6sTXz7Ddlty0nejVgoUodXL89KNxcrfwkEme0Huqtj6jjt4fP7v2uF4L',
  },
  'ftp' : {
    'dominio' : '192.168.1.51',
    'puerto' : 22,
    'usuario' : 'pepe',
    'contrasenia' : 'kiki123',
    'ruta' : '/home/pepe/Documentos/py2/archivos/static/',
    'public' : 'http://192.168.1.51:3031/'
  },
}
