# Script Video Demo UAS
## CareerCompass AI + Career Action Plan CRUD

Gunakan file ini sebagai panduan saat merekam video demo aplikasi.

---

## 1. Pembukaan

Perkenalkan:

- Nama: Galih Aji Pangestu
- NPM: 24081010123
- Kelas: OOP Class C
- Judul aplikasi: CareerCompass AI + Career Action Plan CRUD

Contoh narasi:

"Pada video ini saya akan mendemokan aplikasi UAS saya, yaitu CareerCompass AI + Career Action Plan CRUD. Aplikasi ini melanjutkan project UTS yang sebelumnya berfokus pada rekomendasi karier. Pada pengembangan UAS, saya menambahkan fitur CRUD untuk mengelola rencana aksi karier."

---

## 2. Jalankan Aplikasi

Tampilkan terminal, lalu jalankan:

```bash
streamlit run career_system.py
```

Setelah aplikasi terbuka, jelaskan bahwa aplikasi dibuat menggunakan Python, Streamlit, Pandas, dan Plotly.

---

## 3. Demo Fitur Rekomendasi Karier

Isi sidebar:

- Full Name: Galih Aji Pangestu
- Email: galih@example.com
- Skills: pilih minimal 3 skill, misalnya Python, SQL, Docker, Git
- Skill Level: Intermediate
- Interest Field: Web Development atau Data Science & Analytics
- Work Preference: Remote / Hybrid / Office

Klik **Analyze Career Match**.

Jelaskan output:

- Profile Summary
- Top Recommendation
- Score Breakdown
- Other Recommendations
- Download Report

---

## 4. Demo Create Data

Buka tab **EAS CRUD Action Plan**, lalu tab **Create**.

Isi contoh:

- Judul Rencana: Belajar Docker untuk Backend Developer
- Tipe Rencana: Technical Skill
- Target Karier: pilih dari hasil rekomendasi
- Fokus Area: Docker dan deployment
- Deadline: pilih tanggal
- Progress: 10
- Status: Planned
- Catatan: Menyelesaikan roadmap Docker dan membuat mini project

Klik **Create Data**.

Narasi:

"Fitur create digunakan untuk menambahkan data rencana aksi karier baru. Data ini dibuat sebagai object turunan dari CareerActionPlan."

---

## 5. Demo Read Data

Buka tab **Read**.

Tunjukkan tabel data yang muncul.

Narasi:

"Fitur read menampilkan seluruh data rencana aksi yang tersimpan di repository. Data juga dapat diunduh dalam format JSON."

---

## 6. Demo Update Data

Buka tab **Update**.

Pilih data yang sudah dibuat, lalu ubah:

- Progress: 40
- Status: In Progress
- Catatan: Sudah menyelesaikan dasar Docker dan mulai praktik deployment

Klik **Update Data**.

Narasi:

"Fitur update digunakan untuk memperbarui data berdasarkan plan_id. Atribut object diperbarui melalui method update."

---

## 7. Demo Delete Data

Buka tab **Delete**.

Pilih data, centang konfirmasi, lalu klik **Delete Data**.

Narasi:

"Fitur delete digunakan untuk menghapus data dari repository. Untuk mencegah kesalahan, aplikasi meminta konfirmasi sebelum menghapus data."

---

## 8. Jelaskan Konsep Polimorfisme

Buka tab **Konsep PBO**.

Narasi:

"Polimorfisme diterapkan pada class CareerActionPlan dan turunannya, yaitu TechnicalSkillPlan, SoftSkillPlan, dan PortfolioPlan. Ketiga class ini memiliki method yang sama, yaitu get_plan_type dan priority_score, tetapi hasilnya berbeda sesuai jenis object. Aplikasi dapat memanggil method yang sama pada object berbeda."

---

## 9. Jelaskan Hubungan Antar Class

Jelaskan minimal 3 hubungan, tetapi aplikasi ini menerapkan 5:

- Inheritance: `CareerActionPlan` diwarisi oleh `TechnicalSkillPlan`, `SoftSkillPlan`, dan `PortfolioPlan`.
- Aggregation: `CareerPlanRepository` menyimpan kumpulan object action plan.
- Composition: `CareerPlanManager` memiliki `AuditTrail`.
- Dependency: `CareerPlanManager` menggunakan `CareerPlanFactory`.
- Association: action plan terhubung dengan target karier hasil rekomendasi.

---

## 10. Penutup

Contoh narasi:

"Kesimpulannya, aplikasi ini sudah memenuhi ketentuan UAS karena memiliki fitur create, read, update, dan delete data, menerapkan polimorfisme, serta menerapkan lebih dari tiga hubungan antar class. Aplikasi ini juga berbeda dari project UTS karena menambahkan modul manajemen rencana aksi karier."
