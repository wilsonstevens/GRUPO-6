# Microservicio de Inventario

Este es un microservicio CRUD para gestión de inventario desarrollado con Flask y SQLite, organizado con una arquitectura modular.

## Estructura del Proyecto

```
ms-inventory/
├── app/
│   ├── __init__.py          # Factory de la aplicación Flask
│   ├── config/
│   │   └── __init__.py      # Configuraciones de la aplicación
│   ├── models/
│   │   └── __init__.py      # Modelos de datos (SQLAlchemy)
│   ├── controllers/
│   │   └── __init__.py      # Controladores HTTP
│   ├── services/
│   │   └── __init__.py      # Lógica de negocio
│   └── utils/
│       ├── __init__.py      # Utilidades generales
│       └── validators.py    # Validadores de datos
├── main.py                  # Punto de entrada
├── requirements.txt         # Dependencias
└── README.md               # Documentación
```

## Arquitectura

- **Models**: Definición de entidades y modelos de datos
- **Controllers**: Manejo de peticiones HTTP y respuestas
- **Services**: Lógica de negocio y operaciones de base de datos
- **Utils**: Utilidades, validadores y helpers
- **Config**: Configuraciones de la aplicación

## Entidad Inventory

La entidad tiene los siguientes campos:
- `id`: Identificador único (auto-incremental)
- `country`: País (string)
- `zone`: Zona (string) 
- `product_id`: ID del producto (string)
- `quantity`: Cantidad en inventario (integer)
- `created_at`: Fecha de creación (timestamp)
- `updated_at`: Fecha de última actualización (timestamp)

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Crear la base de datos (opcional - se crea automáticamente al ejecutar):
```bash
python -c "from app import create_app, init_db; app = create_app(); init_db(app); print('Base de datos creada con esquema actualizado')"
```

3. Ejecutar el microservicio:
```bash
python main.py
```

El servicio estará disponible en `http://localhost:5000`

## Endpoints Disponibles

### 1. Crear registro de inventario
- **POST** `/api/inventory`
- **Body** (JSON):
```json
{
    "country": "Colombia",
    "zone": "Bogotá",
    "product_id": "1",
    "quantity": 100
}
```

### 2. Obtener todos los registros
- **GET** `/api/inventory`
- **Parámetros opcionales**:
  - `country`: Filtrar por país
  - `zone`: Filtrar por zona
  - `product_id`: Filtrar por ID de producto

### 3. Obtener registro por ID
- **GET** `/api/inventory/<id>`

### 4. Actualizar registro
- **PUT** `/api/inventory/<id>`
- **Body** (JSON) - campos opcionales:
```json
{
    "country": "Colombia",
    "zone": "Medellín",
    "product_id": "1",
    "quantity": 150
}
```

### 5. Eliminar registro
- **DELETE** `/api/inventory/<id>`

### 6. Buscar registros
- **GET** `/api/inventory/search`
- **Parámetros**:
  - `country`: País a buscar
  - `zone`: Zona a buscar

### 7. Estado del servicio
- **GET** `/health`

## Ejemplos de Uso

### Crear un registro
```bash
curl -X POST http://localhost:5000/api/inventory \
  -H "Content-Type: application/json" \
  -d '{
    "country": "Colombia",
    "zone": "Bogotá",
    "product_id": "1",
    "quantity": 100
  }'
```

### Obtener todos los registros
```bash
curl http://localhost:5000/api/inventory
```

### Buscar por país
```bash
curl "http://localhost:5000/api/inventory/search?country=Colombia"
```

## Base de Datos

El microservicio utiliza SQLite y crea automáticamente la base de datos `inventory.db` en el directorio del proyecto.

### Gestión de la Base de Datos

**Crear/Recrear la base de datos:**
```bash
python -c "from app import create_app, init_db; app = create_app(); init_db(app); print('Base de datos creada con esquema actualizado')"
```

**¿Cuándo usar este comando?**
- Primera instalación del proyecto
- Después de cambios en el modelo de datos
- Resetear la base de datos
- Para verificar que el esquema es correcto

**Nota:** La base de datos se crea automáticamente al ejecutar `python main.py`, pero este comando es útil para crear solo la base de datos sin iniciar el servidor.
