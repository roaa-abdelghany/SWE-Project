from app.core.file_singleton import FileManager

def test_singleton():
    f1 = FileManager()
    f2 = FileManager()
    assert f1 is f2