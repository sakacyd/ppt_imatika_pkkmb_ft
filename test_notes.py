# test_notes.py
import os

def test_speaker_notes():
    assert os.path.exists("speaker_notes.md"), "speaker_notes.md tidak ditemukan"
    with open("speaker_notes.md", "r", encoding="utf-8") as f:
        notes = f.read()
    assert "Slide 1" in notes, "Slide 1 tidak ada di speaker notes"
    assert "Slide 11" in notes, "Slide 11 tidak ada di speaker notes"
    assert "20 Menit" in notes or "20 menit" in notes, "Total durasi 20 menit tidak ada"
    assert "@imatika_ftkmup" in notes, "Akun Instagram tidak ada di notes"
    for i in range(1, 12):
        assert f"Slide {i}" in notes, f"Slide {i} tidak ada di speaker notes"
    print("Speaker notes test PASSED")

if __name__ == "__main__":
    test_speaker_notes()
