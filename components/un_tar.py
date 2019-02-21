import tarfile

class Tar:
    def __init__(self, file_name):
        self.file_name = file_name

    def un_tar_file(self):
        print(f"Opening {self.file_name}.tar.gz file...")
        tar = tarfile.open(self.file_name + ".tar.gz")
        tar.extractall()
        tar.close()
        print("File opened...\n")