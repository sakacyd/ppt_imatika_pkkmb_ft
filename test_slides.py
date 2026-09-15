import os
import re

def test_slides():
    assert os.path.exists("index.html"), "index.html tidak ditemukan"
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    # Periksa 11 section utama slide
    sections_full = re.findall(r'<section[\s>].*?</section>', html, re.DOTALL)
    assert len(sections_full) == 11, f"Jumlah slide harus 11: ditemukan {len(sections_full)}"
    
    # Periksa keberadaan auto-animate data-id
    assert 'data-id="box-1"' in html, "data-id box-1 tidak ditemukan"
    assert 'data-id="imatika-logo"' in html, "data-id imatika-logo tidak ditemukan"
    
    # Periksa code highlight C++
    assert 'data-line-numbers' in html, "Atribut data-line-numbers tidak ditemukan pada kode"
    assert 'class IMATIKA_FTKMUP' in html, "Class C++ IMATIKA tidak ditemukan"
    
    # Periksa slide 4 IT & aspirasi
    slide4 = sections_full[3]
    assert re.search(r'\bIT\b', slide4), "Istilah IT harus ada pada slide aspirasi (slide 4)"
    assert not re.search(r'\bTI\b', slide4), "Istilah TI tidak boleh ada pada slide aspirasi (slide 4)"
    
    # Periksa slide 10 CTA Instagram
    assert '@imatika_ftkmup' in html, "Akun @imatika_ftkmup harus ada di slide CTA"
    
    # Periksa speaker notes
    notes = re.findall(r'<aside class="notes">', html)
    assert len(notes) == 11, f"Speaker notes harus berjumlah 11: ditemukan {len(notes)}"
    print("Slide structure test PASSED")

if __name__ == "__main__":
    test_slides()
