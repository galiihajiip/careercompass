# Script Presentasi UAS
## CareerCompass AI + Career Action Plan CRUD

**Nama:** Galih Aji Pangestu  
**NPM:** 24081010123  
**Kelas:** OOP Class C  
**Estimasi durasi:** 10–15 menit  
**Format:** Presentasi + live demo aplikasi

---

## Cara Pakai Script Ini

1. Buat slide PowerPoint/Google Slides sesuai daftar slide di bawah.
2. Baca bagian **Yang ditampilkan** untuk isi slide.
3. Baca bagian **Yang dijelaskan** sebagai naskah presentasi.
4. Saat sampai slide demo, buka aplikasi Streamlit dan ikuti langkah live demo.
5. Sisipkan screenshot dari aplikasi ke slide agar presentasi tetap rapi walau demo gagal.

**Jalankan aplikasi sebelum presentasi:**

```bash
.venv\Scripts\python.exe -m streamlit run career_system.py
```

---

## RINGKASAN ALUR PRESENTASI

| No | Slide | Durasi | Fokus |
|---|---|---|---|
| 1 | Judul | 30 detik | Perkenalan |
| 2 | Latar Belakang | 1 menit | Masalah yang diselesaikan |
| 3 | Perbedaan UTS vs UAS | 1 menit | Studi kasus berbeda |
| 4 | Tujuan & Ketentuan UAS | 1 menit | Checklist pemenuhan |
| 5 | Arsitektur Aplikasi | 1 menit | Gambaran sistem |
| 6 | Class Diagram | 1,5 menit | Struktur class |
| 7 | Demo: Rekomendasi Karier | 2 menit | Modul UTS |
| 8 | Demo: CRUD Create & Read | 2 menit | Modul UAS |
| 9 | Demo: CRUD Update & Delete | 2 menit | Modul UAS |
| 10 | Polimorfisme | 1,5 menit | Konsep PBO |
| 11 | Hubungan Antar Class | 1,5 menit | Konsep PBO |
| 12 | Kesimpulan | 1 menit | Penutup |
| 13 | Q&A | — | Tanya jawab |

---

# SLIDE 1 — JUDUL

### Yang ditampilkan di slide

- Judul: **CareerCompass AI + Career Action Plan CRUD**
- Subjudul: Pengembangan Modul CRUD Berbasis Pemrograman Berorientasi Objek
- Nama: Galih Aji Pangestu
- NPM: 24081010123
- Kelas: OOP Class C
- Mata Kuliah: Pemrograman Berorientasi Objek

### Yang dijelaskan (naskah)

> "Selamat pagi/siang, Bapak/Ibu dosen dan teman-teman. Perkenalkan, nama saya **Galih Aji Pangestu**, NPM **24081010123**, dari kelas **OOP Class C**.
>
> Pada kesempatan ini saya akan mempresentasikan hasil project **Evaluasi Akhir Semester** saya berjudul **CareerCompass AI + Career Action Plan CRUD**.
>
> Aplikasi ini merupakan kelanjutan dari project UTS saya, dengan penambahan modul CRUD dan penerapan konsep PBO seperti polimorfisme serta hubungan antar class."

**Tips:** Senyum, lihat audiens, jangan langsung baca slide.

---

# SLIDE 2 — LATAR BELAKANG / MASALAH

### Yang ditampilkan di slide

- Banyak mahasiswa kesulitan menentukan arah karier
- Project UTS: memberi **rekomendasi karier**
- Masalah lanjutan: pengguna belum punya alat untuk **mencatat langkah tindak lanjut**
- Solusi UAS: modul **Career Action Plan CRUD**

**[GAMBAR: ilustrasi masalah — rekomendasi ada, tapi tidak ada rencana aksi]**

### Yang dijelaskan (naskah)

> "Pada project UTS, aplikasi saya membantu pengguna mendapatkan rekomendasi karier berdasarkan skill, minat, level kemampuan, dan preferensi kerja.
>
> Namun setelah mendapat rekomendasi, pengguna masih perlu tahu **langkah apa yang harus dilakukan selanjutnya**. Misalnya belajar skill teknis, mempersiapkan soft skill, atau membuat portfolio.
>
> Karena itu, pada UAS saya kembangkan modul baru bernama **Career Action Plan CRUD**, yang memungkinkan pengguna membuat, membaca, memperbarui, dan menghapus data rencana aksi karier."

**Poin penting yang harus tersampaikan:**
- Masalah bisnis jelas
- UAS melanjutkan UTS, bukan project baru yang tidak berhubungan

---

# SLIDE 3 — PERBEDAAN UTS DAN UAS

### Yang ditampilkan di slide

| Aspek | UTS | UAS |
|---|---|---|
| Fokus | Rekomendasi karier | Manajemen rencana aksi |
| Fitur utama | Scoring & rekomendasi | CRUD data action plan |
| Konsep PBO | Inheritance, constructor, overriding | Polimorfisme, relasi antar class |
| Class inti | User, SkillProfile, CareerEngine | CareerActionPlan, CareerPlanManager |

### Yang dijelaskan (naskah)

> "Project UAS ini **melanjutkan** project UTS, tetapi memiliki fokus yang berbeda.
>
> Jika UTS berfokus pada **rekomendasi karier**, maka UAS berfokus pada **pengelolaan rencana aksi karier**.
>
> Dengan begitu, aplikasi saya tetap satu kesatuan studi kasus, tetapi fitur dan penerapan PBO-nya berbeda sehingga memenuhi ketentuan bahwa aplikasi UAS tidak boleh sama dengan project UTS maupun teman sekelas."

---

# SLIDE 4 — TUJUAN DAN KETENTUAN UAS

### Yang ditampilkan di slide

Checklist ketentuan:

- ✅ Create data
- ✅ Read data
- ✅ Update data
- ✅ Delete data
- ✅ Polimorfisme
- ✅ Minimal 3 hubungan antar class
- ✅ Video demo aplikasi
- ✅ Studi kasus berbeda dari UTS

### Yang dijelaskan (naskah)

> "Pada pengembangan UAS ini, saya memastikan semua ketentuan terpenuhi.
>
> Pertama, aplikasi memiliki fitur **CRUD** lengkap.
> Kedua, saya menerapkan **polimorfisme** pada class rencana aksi karier.
> Ketiga, saya menerapkan **lebih dari tiga hubungan antar class**, yaitu inheritance, aggregation, composition, dependency, dan association.
>
> Selain itu, saya juga menyiapkan **video demo** dan **laporan dokumentasi** sebagai bagian dari pengumpulan UAS."

**Tips:** Tunjuk checklist satu per satu dengan jari atau laser pointer.

---

# SLIDE 5 — ARSITEKTUR APLIKASI

### Yang ditampilkan di slide

Diagram alur sederhana:

```
Sidebar Input Profil
        │
        ├─► Tab 1: UTS Recommendation System
        │         └─► CareerEngine
        │
        └─► Tab 2: EAS CRUD Action Plan
                  ├─► Create
                  ├─► Read
                  ├─► Update
                  ├─► Delete
                  └─► Konsep PBO
```

**Teknologi:** Python, Streamlit, Pandas, Plotly

### Yang dijelaskan (naskah)

> "Aplikasi ini dibangun menggunakan **Python** dan **Streamlit** sebagai antarmuka GUI.
>
> Secara arsitektur, aplikasi terdiri dari dua modul utama.
> Modul pertama adalah **UTS Recommendation System**, yang menghasilkan rekomendasi karier.
> Modul kedua adalah **EAS CRUD Action Plan**, yang digunakan untuk mengelola data rencana aksi karier.
>
> Pengguna mengisi profil di sidebar, lalu dapat berpindah antara tab rekomendasi dan tab CRUD."

---

# SLIDE 6 — CLASS DIAGRAM

### Yang ditampilkan di slide

**[GAMBAR: Class Diagram dari laporan]**

Class utama modul UAS:

- `CareerActionPlan`
- `TechnicalSkillPlan`
- `SoftSkillPlan`
- `PortfolioPlan`
- `CareerPlanFactory`
- `CareerPlanRepository`
- `AuditTrail`
- `CareerPlanManager`

### Yang dijelaskan (naskah)

> "Pada modul UAS, class utama adalah **CareerActionPlan** sebagai entity dasar data rencana aksi karier.
>
> Class ini diturunkan menjadi tiga jenis rencana, yaitu **TechnicalSkillPlan**, **SoftSkillPlan**, dan **PortfolioPlan**.
>
> Untuk operasi CRUD, saya menggunakan **CareerPlanRepository** sebagai tempat penyimpanan data, **CareerPlanManager** sebagai service utama, **CareerPlanFactory** untuk membuat object sesuai tipe, dan **AuditTrail** untuk mencatat aktivitas create, update, dan delete.
>
> Class dari modul UTS seperti **CareerEngine** tetap digunakan untuk menghasilkan target karier pada modul action plan."

**Tips:** Jangan baca semua atribut di diagram. Fokus ke peran masing-masing class.

---

# SLIDE 7 — LIVE DEMO: REKOMENDASI KARIER (UTS)

### Yang ditampilkan di slide

- Screenshot tab **UTS Recommendation System**
- Atau langsung buka aplikasi Streamlit

### Langkah demo

1. Buka `http://localhost:8501`
2. Isi sidebar:
   - Nama: Galih Aji Pangestu
   - Email: galih@example.com
   - Skills: Python, SQL, Docker, Git
   - Skill Level: Intermediate
   - Interest Field: Web Development
   - Work Preference: Remote
3. Klik **Analyze Career Match**
4. Tunjukkan hasil rekomendasi

### Yang dijelaskan (naskah)

> "Sekarang saya akan mendemokan aplikasi secara langsung.
>
> Di sidebar, pengguna mengisi profil dan skill yang dimiliki. Setelah itu, sistem akan menganalisis kecocokan terhadap beberapa career path.
>
> Hasilnya ditampilkan pada tab **UTS Recommendation System**, berupa profil pengguna, rekomendasi teratas, grafik skor, dan rekomendasi lainnya.
>
> Bagian ini merupakan kelanjutan dari project UTS, dan hasil rekomendasi ini nantinya digunakan sebagai **target karier** pada modul CRUD."

**Yang harus ditunjuk di layar:**
- Profile Summary
- Top Recommendation
- Score Breakdown

---

# SLIDE 8 — LIVE DEMO: CREATE & READ

### Yang ditampilkan di slide

- Screenshot tab **EAS CRUD Action Plan**
- Sub-tab: **Create** dan **Read**

### Langkah demo CREATE

1. Buka tab **EAS CRUD Action Plan**
2. Masuk sub-tab **Create**
3. Isi form:
   - Judul: Belajar Docker untuk Backend Developer
   - Tipe: Technical Skill
   - Target Karier: Backend Developer
   - Fokus Area: Docker dan deployment
   - Deadline: [pilih tanggal]
   - Progress: 10
   - Status: Planned
   - Catatan: Menyelesaikan roadmap Docker
4. Klik **Create Data**

### Yang dijelaskan saat CREATE (naskah)

> "Pada tab **EAS CRUD Action Plan**, pengguna dapat mengelola data rencana aksi karier.
>
> Fitur **Create** digunakan untuk menambahkan data baru. Data ini dibuat sebagai object melalui **CareerPlanFactory**, lalu disimpan ke **CareerPlanRepository**, dan aktivitasnya dicatat oleh **AuditTrail**.
>
> Perhatikan bahwa tipe rencana yang dipilih menentukan class object yang dibuat, misalnya **TechnicalSkillPlan**."

### Langkah demo READ

1. Buka sub-tab **Read**
2. Tunjukkan tabel data
3. Tunjukkan log aktivitas CRUD
4. Opsional: klik **Download Data CRUD (JSON)**

### Yang dijelaskan saat READ (naskah)

> "Fitur **Read** menampilkan seluruh data rencana aksi yang tersimpan.
>
> Data ditampilkan dalam bentuk tabel, dan setiap baris merupakan hasil pemanggilan method **display_summary()** dari object plan.
>
> Di bawah tabel, terdapat **log aktivitas CRUD** yang mencatat kapan data dibuat, diperbarui, atau dihapus.
>
> Pengguna juga dapat mengunduh data dalam format JSON."

**Poin penting:**
- Create = tambah data
- Read = tampilkan data + audit log

---

# SLIDE 9 — LIVE DEMO: UPDATE & DELETE

### Yang ditampilkan di slide

- Screenshot sub-tab **Update** dan **Delete**

### Langkah demo UPDATE

1. Buka sub-tab **Update**
2. Pilih data yang tadi dibuat
3. Ubah:
   - Progress: 40
   - Status: In Progress
   - Catatan: Sudah menyelesaikan dasar Docker
4. Klik **Update Data**
5. Kembali ke tab **Read** untuk tunjukkan perubahan

### Yang dijelaskan saat UPDATE (naskah)

> "Fitur **Update** digunakan untuk memperbarui data berdasarkan **plan_id**.
>
> Pengguna memilih data yang ingin diubah, lalu sistem memperbarui atribut object melalui method **update()**.
>
> Setelah di-update, data yang berubah langsung terlihat pada tab Read, dan aktivitas update juga tercatat di audit trail."

### Langkah demo DELETE

1. Buka sub-tab **Delete**
2. Pilih data
3. Centang konfirmasi
4. Klik **Delete Data**
5. Tunjukkan data sudah hilang di tab Read

### Yang dijelaskan saat DELETE (naskah)

> "Fitur **Delete** digunakan untuk menghapus data dari repository.
>
> Agar tidak terjadi kesalahan, aplikasi meminta **konfirmasi** sebelum data dihapus.
>
> Setelah proses delete, data tidak lagi muncul pada tab Read, dan aktivitas delete ikut tercatat pada audit trail."

**Poin penting:**
- CRUD lengkap sudah didemokan
- Setiap operasi tercatat di audit trail

---

# SLIDE 10 — POLIMORFISME

### Yang ditampilkan di slide

| Class | `get_plan_type()` | `priority_score()` |
|---|---|---|
| CareerActionPlan | General | 100 - progress |
| TechnicalSkillPlan | Technical Skill | 120 - progress |
| SoftSkillPlan | Soft Skill | 90 - progress |
| PortfolioPlan | Portfolio Project | 110 - progress |

**[GAMBAR: cuplikan kode TechnicalSkillPlan]**

### Yang dijelaskan (naskah)

> "Salah satu konsep PBO yang diterapkan pada UAS adalah **polimorfisme**.
>
> Polimorfisme terjadi ketika beberapa class memiliki method dengan nama yang sama, tetapi implementasinya berbeda.
>
> Pada aplikasi ini, class **CareerActionPlan** diturunkan menjadi **TechnicalSkillPlan**, **SoftSkillPlan**, dan **PortfolioPlan**.
>
> Ketiga class tersebut memiliki method **get_plan_type()** dan **priority_score()**, tetapi hasilnya berbeda.
>
> Saat aplikasi menampilkan data, method yang sama dipanggil pada object yang berbeda. Inilah bentuk polimorfisme."

**Contoh singkat jika ditanya:**

> "Jadi meskipun semua plan punya method `priority_score()`, nilai prioritasnya berbeda tergantung jenis rencana."

---

# SLIDE 11 — HUBUNGAN ANTAR CLASS

### Yang ditampilkan di slide

| Hubungan | Contoh pada Aplikasi |
|---|---|
| Inheritance | CareerActionPlan → TechnicalSkillPlan |
| Aggregation | CareerPlanRepository menyimpan banyak plan |
| Composition | CareerPlanManager memiliki AuditTrail |
| Dependency | CareerPlanManager memakai CareerPlanFactory |
| Association | Action plan terhubung ke target karier dari CareerEngine |

### Yang dijelaskan (naskah)

> "Selain polimorfisme, aplikasi ini juga menerapkan **lima hubungan antar class**.
>
> Pertama, **Inheritance**, yaitu class anak mewarisi class induk.
>
> Kedua, **Aggregation**, yaitu repository menyimpan kumpulan object plan.
>
> Ketiga, **Composition**, yaitu manager memiliki audit trail sebagai bagian internalnya.
>
> Keempat, **Dependency**, yaitu manager bergantung pada factory untuk membuat object plan.
>
> Kelima, **Association**, yaitu data action plan terhubung dengan target karier hasil rekomendasi dari CareerEngine.
>
> Dengan ini, aplikasi sudah memenuhi ketentuan minimal tiga hubungan antar class."

**Tips:** Sebutkan minimal 3 dulu, lalu tambahkan 2 lainnya jika waktu cukup.

---

# SLIDE 12 — KESIMPULAN

### Yang ditampilkan di slide

**Kesimpulan:**

1. UAS melanjutkan project UTS dengan modul baru
2. Fitur CRUD berjalan lengkap
3. Polimorfisme diterapkan pada action plan
4. Hubungan antar class diterapkan lebih dari 3
5. Aplikasi siap digunakan untuk demo dan dokumentasi

**Saran pengembangan:**
- Database permanen
- Login user
- Reminder deadline

### Yang dijelaskan (naskah)

> "Sebagai kesimpulan, project UAS saya berhasil melanjutkan project UTS dengan menambahkan modul **Career Action Plan CRUD**.
>
> Aplikasi ini sudah memiliki fitur **create, read, update, dan delete**, menerapkan **polimorfisme**, serta **hubungan antar class** sesuai ketentuan mata kuliah.
>
> Untuk pengembangan selanjutnya, modul ini bisa ditambahkan database permanen, fitur login, dan reminder deadline.
>
> Sekian presentasi dari saya. Terima kasih atas perhatian Bapak/Ibu dosen dan teman-teman. Saya siap menerima pertanyaan."

---

# SLIDE 13 — Q&A (PERSIAPAN JAWABAN)

Jika dosen atau teman bertanya, gunakan jawaban singkat berikut.

### "Di bagian mana CRUD-nya?"

> "CRUD ada di tab utama **EAS CRUD Action Plan**, dengan sub-tab Create, Read, Update, dan Delete."

### "Apa bedanya project UTS dan UAS?"

> "UTS fokus pada rekomendasi karier. UAS menambahkan modul pengelolaan rencana aksi karier berbasis CRUD."

### "Di mana polimorfismenya?"

> "Pada class CareerActionPlan dan turunannya: TechnicalSkillPlan, SoftSkillPlan, dan PortfolioPlan. Method yang sama, perilaku berbeda."

### "Hubungan antar class apa saja yang dipakai?"

> "Inheritance, aggregation, composition, dependency, dan association."

### "Data disimpan di mana?"

> "Saat ini disimpan di memori aplikasi melalui repository dan session state Streamlit, belum menggunakan database eksternal."

### "Kenapa pakai Streamlit?"

> "Karena memudahkan pembuatan GUI tanpa framework web yang terlalu kompleks, sehingga fokus bisa ke penerapan konsep PBO."

### "Class paling penting di modul UAS apa?"

> "CareerActionPlan sebagai entity data, CareerPlanRepository untuk CRUD storage, dan CareerPlanManager sebagai service utama."

---

## CHECKLIST SEBELUM PRESENTASI

- [ ] Aplikasi sudah dijalankan dan tidak error
- [ ] Browser sudah terbuka di `http://localhost:8501`
- [ ] Slide presentasi sudah siap
- [ ] Screenshot cadangan sudah ada di slide (jika demo gagal)
- [ ] Contoh data untuk Create sudah dipersiapkan
- [ ] Class diagram sudah ada di slide
- [ ] Link video demo siap jika ditanya
- [ ] Laporan `LAPORAN_UAS_CAREER_ACTION_PLAN.md` sudah dibawa

---

## CONTOH PEMBUKAAN SINGKAT (30 DETIK)

> "Assalamualaikum / Selamat pagi. Saya Galih Aji Pangestu, NPM 24081010123. Hari ini saya akan mempresentasikan aplikasi UAS saya, CareerCompass AI + Career Action Plan CRUD, yang melanjutkan project UTS dengan modul CRUD dan penerapan konsep PBO."

## CONTOH PENUTUP SINGKAT (30 DETIK)

> "Jadi aplikasi UAS saya sudah memenuhi ketentuan CRUD, polimorfisme, dan hubungan antar class. Terima kasih, saya siap menerima pertanyaan."

---

**File terkait:**
- Laporan: `LAPORAN_UAS_CAREER_ACTION_PLAN.md`
- Script video: `SCRIPT_VIDEO_DEMO_UAS.md`
- Aplikasi: `career_system.py`
