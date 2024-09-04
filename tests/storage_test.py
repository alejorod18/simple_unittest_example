from unittest.mock import patch, MagicMock
from main import upload_to_gcs

@patch('google.cloud.storage.Client')
def test_upload_to_gcs(mock_storage_client):
    # Configuración del mock
    mock_bucket = MagicMock()
    mock_blob = MagicMock()
    mock_storage_client.return_value.bucket.return_value = mock_bucket
    mock_bucket.blob.return_value = mock_blob

    # Parámetros del archivo
    bucket_name = "my-test-bucket"
    destination_blob_name = "destination/file.txt"
    source_file_name = "local/file.txt"

    # Llamar a la función a probar
    return_value = upload_to_gcs(bucket_name, destination_blob_name, source_file_name)

    # Comprobar que los métodos correctos fueron llamados
    mock_storage_client.assert_called_once()
    mock_storage_client.return_value.bucket.assert_called_once_with(bucket_name)
    mock_bucket.blob.assert_called_once_with(destination_blob_name)
    mock_blob.upload_from_filename.assert_called_once_with(source_file_name)
    assert bucket_name == return_value