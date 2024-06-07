# training_dev
Program  monitoring mompetensi karyawan untuk peningkatan kualitas training dan development

https://drive.google.com/file/d/17SG96u4J8iTCkjaqzMs-0Gya7yh3dB8U/view?usp=drive_link

Proyek kami berfokus pada peningkatan efisiensi dalam proses pengambilan keputusan dan pengolahan data, yang merupakan sub tema 1 dari hackathon. Kami berencana untuk menciptakan dampak positif pada ekonomi digital dengan mengembangkan solusi yang memungkinkan pemantauan kemampuan dan karakteristik karyawan melalui platform digital. Ini diharapkan dapat meningkatkan efisiensi dalam ekonomi digital. Selain itu, dalam konteks keuangan Indonesia, proyek kami bertujuan untuk menyelesaikan masalah seperti alokasi yang tepat untuk pelatihan dan pengembangan karyawan, serta pengukuran kemampuan karyawan. Dengan demikian, proyek kami berupaya untuk memberikan solusi inovatif untuk meningkatkan efisiensi dan efektivitas dalam pengelolaan sumber daya manusia, yang pada akhirnya dapat berkontribusi pada pertumbuhan dan perkembangan ekonomi digital dan lanskap keuangan di Indonesia.

## Dependency-Dependency & Instalasi
----------------------------
Untuk menginstall aplikasi ini, ikuti langkah-langkah berikut:

1. Clone repository:
   ```
   git clone [https://github.com/AndhikaFW/training_dev.git]
   ```
2. Masuk ke folder:
   ```
   cd training_dev
   ```

4. Buat _python virtual environment_:
   ```
   python3 -m venv .venv
   ```
5. Jalankan _python virtual environment_:
   ```
   source .venv/bin/activate  
   ```

3. Install dependency-dependency yang dibutuhkan:
   ```
   pip install -r requirements.txt
   ```

4. Dapatkan API key dari OpenAI dan tambahkan API key serta tanda anda ke file `.env` di direktori projek.
   ```commandline
   OPENAI_API_KEY=api_key_rahasia_anda
   ```

## Penggunaan
-----
Untuk menggunakan aplikasi ini, ikuti langkah-langkah berikut:

1. Pastikan dependency-dependency sudah diinstall dan pastikan sudah menambahkan OpenAI API key serta tanda anda ke file `.env`.

2. Jalankan _python virtual environment_:
   ```
   source .venv/bin/activate  
   ```

3. Jalankan file `main.py` dengan CLI. `Jalankan perintah berikut`:
   ```
   #Untuk Lokal
   uvicorn main:docs_chat

   #Untuk Server #.#.#.# diisi dengan ip tujuan dan #### diisi dengan port yang kosong
   uvicorn main:docs_chat --host #.#.#.# --port ####
   ```

4. Aplikasi akan muncul di browser default anda, menampilkan GUI.
   ```
   #Jika tidak maka sesuai dengan yang tertulis di cli misal:
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   #Untuk interface client ada pada /user misal:
   Uvicorn running on http://127.0.0.1:8000/user
   ```

6. Masukkan dokumen ke aplikasi dengan instruksi yang diberikan.

7. Masukkan pertanyaan secara natural mengenai PDFs dengan chat interface.



## Lisensi
-------
 Aplikasi MultiDocs Chat dirilis dibawah [Lisensi MIT](https://opensource.org/licenses/MIT).
