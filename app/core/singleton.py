import csv

class FileManager:
    _instance = None

    def _new_(cls):
        if cls._instance is None:
            cls.instance = super().new_(cls)
            cls._instance.file_path = "data/Products.csv"
        return cls._instance

    def read_csv(self, path=None):
        path = path or self.file_path
        with open(path, newline='') as f:
            return list(csv.DictReader(f))