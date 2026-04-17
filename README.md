# Intermediate Web Scraping: Book Store Data Extraction

Repositori ini berisi latihan pengerjaan modul **Intermediate Web Scraping** (Python). Fokus utama dari proyek ini adalah melakukan ekstraksi data secara otomatis dari website e-commerce fiktif yang memiliki sistem paginasi (banyak halaman).

## 🚀 Fitur Utama
- **Automated Pagination**: Mengambil data dari total 50 halaman secara otomatis.
- **Detailed Extraction**: Mengekstrak judul buku, harga, ketersediaan stok, dan rating.
- **Stealth Scraping**: Implementasi `User-Agent` untuk mensimulasikan permintaan dari browser asli agar terhindar dari pemblokiran.
- **Data Structuring**: Hasil ekstraksi diproses untuk kebutuhan alur ETL (Extract, Transform, Load).

## 🛠️ Tech Stack
- **Python** (Core Logic)
- **BeautifulSoup4 / Scrapy** (HTML Parsing)
- **Requests** (HTTP Library)

## 📁 Struktur Dokumen
- `basic_scraping.py`: Latihan dasar pengambilan elemen tunggal.
- `intermediate_scraping.py`: Script utama untuk scraping 50 halaman sekaligus.
- `requirements.txt`: Daftar library yang dibutuhkan.

## 📝 Cara Menjalankan
1. Clone repositori ini:
   ```bash
   git clone [https://github.com/dzikri007/exercise-web-scraping-intermediate.git](https://github.com/dzikri007/exercise-web-scraping-intermediate.git)
