import tarfile, os, logging

logger = logging.getLogger(__name__)

class Tar:
    def __init__(self, file_name):
        self.file_name = file_name

    def un_tar_file(self):
        logging.getLogger(__name__).info(f"Opening file: {self.file_name}.tar.gz")
        tar = tarfile.open(self.file_name + ".tar.gz")
        tar.extractall()
        tar.close()
        logging.getLogger(__name__).info(f"{self.file_name} opened.")