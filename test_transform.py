import sys
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataTransformationConfig
from src.components.data_transformation import DataTransformation

ingest = DataIngestionArtifact(
    trained_file_path='artifact/02_25_2026_02_22_00/data_ingestion/ingested/train.csv',
    test_file_path='artifact/02_25_2026_02_22_00/data_ingestion/ingested/test.csv'
)
valid = DataValidationArtifact(validation_status=True, message='', validation_report_file_path='')
config = DataTransformationConfig()
print('Starting DataTransformation...')
dt = DataTransformation(ingest, config, valid)
print('Init done. Calling initiate_data_transformation...')
result = dt.initiate_data_transformation()
print('Done:', result)
