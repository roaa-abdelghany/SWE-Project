from app.core.file_singleton import FileManager

def test_csv_read():
    fm = FileManager()
    data = fm.read_csv("data/Products.csv")
    assert isinstance(data, list)