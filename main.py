from google.cloud import storage


def upload_to_gcs(bucket_name, destination_blob_name, source_file_name):
    """
    Sube un archivo a Google Cloud Storage.

    Args:
        bucket_name (str): El nombre del bucket en Google Cloud Storage.
        destination_blob_name (str): El nombre de destino del blob en el bucket.
        source_file_name (str): El nombre del archivo local que se subirá.
    """
    # Crear un cliente de Google Cloud Storage
    client = storage.Client()
    # Obtener el bucket de destino
    bucket = client.bucket(bucket_name)

    # Crear un blob en el bucket con el nombre de destino
    blob = bucket.blob(destination_blob_name)

    # Subir el archivo desde la ruta local especificada
    blob.upload_from_filename(source_file_name)
    return bucket_name
