import streamlit as st

faqs = [
    'Bagaimana cara kerja vaksin COVID-19?',
    'Apakah vaksin COVID-19 aman?',
    'Bagaimana vaksin COVID-19 bisa dikembangkan dengan begitu cepat?',
    'Vaksin COVID-19 mana yang paling baik untuk saya?',
    'Apakah vaksin COVID-19 juga efektif melawan varian baru virus?',
    'Siapa yang perlu menerima vaksin terlebih dahulu?',
    'Dalam keadaan apa saya sebaiknya tidak menerima vaksin COVID-19?',
    'Apakah orang yang pernah terkena COVID-19 masih perlu divaksin?',
    'Apakah ibu menyusui perlu mendapatkan vaksin COVID-19?',
    'Apakah ibu hamil perlu mendapatkan vaksin COVID-19?',
    'Apakah vaksin COVID-19 bisa berdampak terhadap kesuburan?',
    'Apakah anak saya perlu menerima vaksin COVID-19?',
    'Kapan vaksin COVID-19 tersedia di negara saya?',
    'Apa itu COVAX?',
    'Saya menyimak informasi yang tidak akurat di dunia maya tentang vaksin COVID-19. Apa yang harus dilakukan?',
    'Apakah vaksin COVID-19 memiliki kandungan hewani?',
    'Bagaimana saya bisa melindungi keluarga hingga kami semua menerima vaksin COVID-19?'
]

answers = [
    ''' 
    Vaksin bekerja dengan cara meniru agen penyakit—baik berupa virus, bakteri, maupun mikroorganisme lain yang bisa menyebabkan penyakit. Dengan meniru, vaksin ‘mengajarkan’ sistem kekebalan tubuh kita untuk secara spesifik bereaksi dengan cepat dan efektif melawan agen penyakit.
    Biasanya, hal tersebut dapat terjadi karena vaksin membawa agen penyakit yang sudah dilemahkan. Sistem kekebalan tubuh pun ‘belajar’ dengan membangun memori tentang penyakit. Dengan begitu, tubuh kita bisa dengan cepat mengenali suatu penyakit dan melawannya sebelum kita menderita sakit berat. 
    Untuk informasi lebih jauh tentang cara kerja vaksin, silakan kunjungi situs WHO.
    ''',
    ''' 
    Ya, meskipun pengembangan vaksin COVID-19 diupayakan berjalan secepat mungkin, vaksin tetap harus melalui serangkaian uji klinis yang ketat untuk membuktikan kesesuaiannya dengan standar internasional dalam hal keamanan dan efektivitas vaksin. Hanya vaksin yang dinilai telah memenuhi standarlah yang akan mendapatkan persetujuan WHO dan otoritas nasional.
    UNICEF hanya akan mengadakan dan menyuplai vaksin COVID-19 yang memenuhi kriteria keamanan dan efikasi yang ditetapkan oleh WHO serta yang telah mendapatkan persetujuan resmi dari otoritas nasional.
    Cari tahu lebih lanjut di KIPI (Kejadian Ikutan Pasca Imunisasi).
    ''',
    ''' 
    Pengembangan vaksin COVID-19 yang cepat dimungkinkan oleh pendanaan penelitian dan pengembangan, serta oleh kerja sama global dalam skala yang belum pernah terjadi sebelumnya. Melalui segenap dukungan ini, para ilmuwan dapat mengembangkan vaksin COVID-19 yang aman dan efektif dengan amat cepat. Namun demikian, semua prosedur dan peraturan keamanan yang ketat tetap dipatuhi.
    Di samping beberapa jenis vaksin COVID-19 yang saat ini tengah digunakan di banyak negara di seluruh dunia, masyarakat patut merasa optimistis karena terdapat lebih dari 200 kandidat vaksin lain yang sedang berada dalam tahap pengembangan. Sebagian sudah berada pada Fase III uji klinis, yakni  fase terakhir sebelum suatu jenis vaksin mendapatkan persetujuan.
    ''',
    ''' 
    Semua vaksin yang disetujui oleh WHO telah terbukti aman dan efektif dalam melindungi penerimanya terhadap sakit berat yang ditimbulkan oleh COVID-19. Dengan demikian, vaksin terbaik adalah vaksin yang paling siap untuk diakses!
    ''',
    ''' 
    Menurut WHO, vaksin-vaksin yang sejauh ini telah disetujui penggunaannya diharapkan minimal dapat memberikan sebagian perlindungan terhadap varian baru virus.
    Para ahli di seluruh dunia terus mempelajari dampak varian baru terhadap perilaku virus, termasuk potensi dampaknya terhadap efektivitas vaksin COVID-19.
    Apabila vaksin-vaksin yang ada saat ini terbukti tidak terlalu efektif melawan satu atau lebih varian baru, komposisi kandungan vaksin dapat diubah untuk meningkatkan efek perlindungannya. Pada masa mendatang, mungkin dibutuhkan pengubahan terhadap vaksinasi, seperti pemberian dosis ulangan (booster) ataupun pembaruan lainnya.
    Akan tetapi, untuk sementara waktu, yang terpenting adalah masyarakat mendapatkan vaksinasi dan tidak berhenti berupaya mencegah penularan, seperti tetap menjaga jarak, mengenakan masker, berada di ruangan dengan sirkulasi udara yang baik, rajin mencuci tangan, dan segera menemui tenaga kesehatan jika mengalami gejala tertular COVID-19. Pencegahan penularan dapat membantu menekan peluang virus bermutasi.
    ''',
    ''' 
    Mengingat keterbatasan kapasitas produksi vaksin pada tahun 2021, sehingga kebutuhan global tidak dapat terpenuhi seluruhnya, maka tidak semua orang dapat menerima vaksin pada waktu yang sama. Setiap negara harus mengidentifikasi populasi prioritas, yang menurut rekomendasi WHO adalah tenaga kesehatan di garis depan (dalam rangka melindungi sistem kesehatan) dan kelompok lain yang berisiko tinggi mengalami kematian akibat COVID-19, seperti lansia dan penderita kondisi medis tertentu. Pekerja esensial lain, seperti guru dan pekerja sosial juga perlu diutamakan, diikuti dengan kelompok-kelompok lainnya sesuai dengan perkembangan ketersediaan dosis vaksin.
    ''',
    ''' 
    Hanya sedikit kondisi dimana seseorang sebaiknya tidak menerima vaksin, yaitu:
    1. Orang dengan riwayat reaksi alergi berat terhadap kandungan vaksin COVID-19
    2. Orang yang sedang sakit atau sedang mengalami gejala COVID-19 (vaksinasi dapat dilakukan setelah sembuh dan dengan persetujuan dokter).
    Anggota masyarakat yang ragu tentang kondisinya berkaitan dengan vaksinasi COVID-19 dapat berkonsultasi dengan dokter.
    ''',
    ''' 
    Ya, seseorang yang pernah tertular COVID-19 tetap perlu mendapatkan vaksin untuk mendapatkan perlindungan maksimal. Penyitas COVID-19 bisa jadi memiliki kekebalan alamiah terhadap virus ini, akan tetapi belum diketahui seberapa lama kekebalan itu bertahan atau seefektif apa perlindungannya.  Penyintas COVID-19 dapat divaksinasi 3 bulan setelah sembuh.
    ''',
    ''' 
    Para peneliti tengah mempelajari vaksin COVID-19 dan kaitannya dengan ibu menyusui, tetapi informasi yang tersedia saat ini masih terbatas. Sesuai saran WHO, vaksin dapat ditawarkan kepada ibu menyusui yang juga termasuk kelompok prioritas vaksinasi—contohnya, ibu menyusui yang juga seorang tenaga kesehatan. Pemberian ASI dapat dilanjutkan setelah vaksinasi; ASI tetap merupakan salah satu cara terbaik untuk melindungi anak dari berbagai macam penyakit dan membantu mereka agar tetap sehat.
    ''',
    ''' 
    Meskipun risiko seseorang menderita sakit parah akibat COVID-19 secara umum rendah, ibu hamil  lebih berisiko dibandingkan mereka yang tidak hamil.
    Ibu hamil yang berisiko tinggi terpapar COVID-19 (misalnya, tenaga kesehatan) atau yang memiliki kondisi tertentu yang memperbesar risikonya mengalami sakit parah, dapat menerima vaksinasi setelah berkonsultasi dengan dokter atau bidan yang menanganinya. Manfaat vaksin jauh lebih besar dibandingkan risiko sakit karena terinfeksi bila tidak divaksin.
    ''',
    ''' 
    Tidak. Klaim semacam ini bisa jadi didapatkan melalui media sosial, tetapi dapat disampaikan bahwa tidak ada bukti bahwa vaksin apa pun, termasuk vaksin COVID-19, bisa berdampak negatif terhadap kesuburan baik pada perempuan maupun laki-laki. Pasangan yang tengah merencanakan kehadiran anak tidak perlu menghindari kehamilan setelah menerima vaksin COVID-19.
    ''',
    ''' 
    Sistem kekebalan tubuh anak berbeda dari orang dewasa dan dapat sangat beragam bergantung pada usianya. Saat ini, vaksin COVID-19 yang disetujui WHO tidak disarankan untuk diberikan kepada anak yang berusia di bawah 16-18 tahun (angka usia yang spesifik bergantung pada jenis vaksin), meskipun anak itu termasuk kelompok berisiko tinggi. Anak-anak tidak disertakan dalam uji klinis awal vaksin COVID-19, sehingga saat ini informasi tentang keamanan dan efikasi vaksin terhadap anak di bawah usia 16 tahun sangat terbatas atau tidak ada. Dibutuhkan penelitian lebih lanjut, dan kami akan terus menyampaikan informasi terkini seiring dengan semakin banyak uji yang dilakukan dan perkembangan informasi yang tersedia.
    Namun demikian, hal yang terpenting bagi orang tua adalah memastikan anak tetap menerima vaksinasi rutinnya.
    ''',
    ''' 
    Distribusi vaksin sedang berjalan di seluruh dunia. Ketersediaan vaksin sendiri beragam di setiap negara. Silakan periksa informasi resmi secara berkala dari kementerian kesehatan untuk mendapatkan informasi terbaru di negara setempat.
    Atas nama COVAX Facility, UNICEF mengadakan vaksin COVID-19 dan menyuplai vaksin ke seluruh dunia untuk memastikan tidak ada negara yang tertinggal. Target kami adalah memastikan total 2 miliar dosis siap diberikan pada akhir 2021. Dosis vaksin dialokasikan kepada negara-negara yang berpartisipasi dalam COVAX Facility; alokasi dilakukan secara proporsional terhadap total populasi negara.
    ''',
    ''' 
    COVAX adalah bagian dari upaya global yang bertujuan mempercepat pengembangan dan produksi vaksin COVID-19 serta menjamin akses vaksin yang adil dan setara di seluruh dunia. Tidak ada satu pun negara yang aman dari COVID-19 sampai semua negara terlindungi.
    Terdapat 190 negara dan teritori yang ikut serta di dalam COVAX Facility, atau secara keseluruhan mewakili lebih dari 90 persen populasi dunia. Bekerja sama dengan CEPI, GAVI, WHO, dan mitra-mitra lain, UNICEF memimpin upaya untuk mengadakan dan menyuplai vaksin COVID-19 atas nama COVAX.
    ''',
    ''' 
    Sayangnya, banyak informasi keliru seputar virus dan vaksin COVID-19 yang beredar di dunia maya. Misinformasi di tengah situasi krisis kesehatan bisa menyebabkan paranoia, rasa takut, dan stigma, bahkan menyebabkan orang lain tidak terlindungi atau lebih rentan terhadap virus. Selalu rujuk fakta dan saran dari sumber-sumber tepercaya, seperti otoritas kesehatan, PBB, UNICEF, dan WHO.
    Anggota masyarakat yang melihat informasi salah atau bisa menimbulkan pemahaman keliru di dunia maya bisa membantu menghentikan peredarannya dengan membuat laporan ke platform media sosial.
    ''',
    ''' 
    Tidak. Semua vaksin COVID-19 yang disetujui WHO tidak mengandung produk hewan.
    ''',
    '''
    Vaksin yang aman dan efektif akan berdampak besar, namun ketersediaan vaksin di seluruh dunia masih terbatas sehingga pelaksanaan vaksinasi COVID-19 dilakukan secara bertahap. Untuk saat ini, meskipun telah menerima vaksin, kita tetap perlu menerapkan langkah pencegahan penularan demi melindungi diri sendiri dan orang lain, seperti mengenakan masker, menjaga jarak, dan rajin mencuci tangan
    '''
]

def load_faqs():
    header = st.container()
    main = st.container()
    
    with header:
        st.header('Pertanyaan yang Sering Ditanyakan')
        st.write('diperoleh dari https://www.unicef.org/indonesia/id/coronavirus')
    
    with main:
        questions = st.selectbox('Daftar pertanyaan : ', faqs, index=0)
        ans = ' '
        for i in range(len(faqs)):
            if questions == faqs[i]:
                ans = answers[i]
        st.write(ans)