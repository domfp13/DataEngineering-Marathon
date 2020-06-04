
import logging
from google.cloud import storage
from os.path import basename
from source.GeneralFunctions import getPath

def marathon_execution(event, context)->None:
    """Trigger by a change in a cloud storage bucket

    Args:
        event (dict): Event payload
        context (google.cloud.functions.context): Metadata
    """
    try:
        logging.info('Start Processing')

        file_name = basename(event['name'])
        
        client = storage.Client()

        path = getPath(file_name)
        
        with getPath(file_name).open('wb+') as file:
            client.bucket(event['bucket']).get_blob(event['name']).download_to_file(file)

        logging.info("File Downloaded")

    except Exception as e:
        logging.exception(e)
    
    