# Google Cloud Storage Upload Example with Pytest

Este proyecto es un ejemplo básico de cómo subir archivos a Google Cloud Storage usando Python, y cómo escribir pruebas unitarias utilizando `pytest` y `unittest.mock` para seguir el principio de Test-Driven Development (TDD).

## Estructura del Proyecto

```
├── main.py                 # Código principal para subir archivos a Google Cloud Storage
├── test_main.py            # Pruebas unitarias para el código principal
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## Requisitos

- Python 3.7 o superior
- Una cuenta de Google Cloud con acceso a Google Cloud Storage

## Instalación

1. Clona el repositorio en tu máquina local:

   ```bash
   git clone https://github.com/tu_usuario/gcs-upload-example.git
   cd gcs-upload-example
   ```

2. Crea un entorno virtual (opcional, pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate   # En Linux/MacOS
   venv\Scripts\activate      # En Windows
   ```

3. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Subir un Archivo a Google Cloud Storage

El código para subir un archivo a Google Cloud Storage se encuentra en `main.py`:

```python
from google.cloud import storage

def upload_to_gcs(bucket_name, destination_blob_name, source_file_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
```

Para usar esta función, asegúrate de haber configurado correctamente las credenciales de Google Cloud en tu entorno. Luego, simplemente llama a la función `upload_to_gcs` con los parámetros apropiados.

### Ejecución de Pruebas

Las pruebas unitarias para este código se encuentran en `test_main.py`. Las pruebas están escritas usando `pytest` y simulan el comportamiento de Google Cloud Storage usando `unittest.mock`.

Para ejecutar las pruebas, utiliza el siguiente comando:

```bash
pytest
```

Esto ejecutará todas las pruebas en el proyecto y mostrará los resultados en la terminal.

## Personalización

Puedes modificar los nombres de los buckets, blobs, y archivos para adaptarlos a tus necesidades específicas.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit de ellos (`git commit -am 'Agrega nueva característica'`).
4. Sube tu rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

```

### Explicación

- **Instalación**: El `README.md` proporciona instrucciones claras sobre cómo instalar y configurar el proyecto.
- **Uso**: Incluye detalles sobre cómo ejecutar la función principal y cómo realizar pruebas.
- **Estructura**: La estructura del proyecto se describe para que otros usuarios puedan entender rápidamente cómo está organizado.
- **Contribuciones**: Proporciona una guía básica para contribuir al proyecto.
- **Licencia**: Menciona que el proyecto está bajo la Licencia MIT, aunque puedes modificar esto según la licencia que prefieras usar.

Este `README.md` debería ayudarte a documentar y compartir tu proyecto de manera efectiva.