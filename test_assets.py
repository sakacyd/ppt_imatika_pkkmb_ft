# test_assets.py
import os

def test_assets():
    assert os.path.exists("Logo IMATIKA.png"), "Logo IMATIKA tidak ditemukan"
    assert os.path.exists("Logo Universitas Pancasila.png"), "Logo UP tidak ditemukan"
    assert os.path.exists("assets/css/style.css"), "File style.css belum dibuat"
    with open("assets/css/style.css", "r", encoding="utf-8") as f:
        content = f.read()
    assert "#201e72" in content, "Warna navy IMATIKA tidak ada di style.css"
    assert "#facc15" in content, "Warna gold IMATIKA tidak ada di style.css"
    print("Asset dan CSS test PASSED")

if __name__ == "__main__":
    test_assets()
