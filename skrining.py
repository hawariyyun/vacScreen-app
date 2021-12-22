from predict import process_image
import streamlit as st
from PIL import Image


# list of screening questions
screenQuestions = [
    'Apakah Anda memiliki riwayat alergi berat seperti sesak napas, bengkak dan urtikaria seluruh badan atau reaksi berat lainnya karena vaksin?',
    'Apakah Anda memiliki riwayat alergi berat setelah divaksinasi COVID-19 sebelumnya?',
    'Apakah Anda sedang hamil?',
    'Apakah Anda mengidap penyakit autoimun seperti asma, lupus?',
    'Apakah Anda sedang mendapat pengobatan untuk gangguan pembekuan darah, kelainan darah, defisiensi imun dan penerima produk darah/transfusi?',
    'Apakah Anda sedang mendapat pengobatan immunosupressant seperti kortikosteroid dan kemoterapi?',
    'Apakah Anda memiliki penyakit jantung berat dalam keadaan sesak?',
    'Apakah Anda mengalami kesulitan untuk naik 10 anak tangga?',
    'Apakah Anda sering merasa kelelahan?',
    'Apakah Anda memiliki 5 atau lebih dari 11 penyakit berikut (Hipertensi, diabetes, kanker, penyakit paru kronis, serangan jantung, gagal jantung kongestif, nyeri dada asma, nyeri sendi, stroke, dan penyakit ginjal)?',
    'Apakah Anda mengalami kesulitan berjalan kira-kira 100 sampai 200 meter?',
    'Apakah Anda mengalami penurunan berat badan yang bermakna dalam setahun terakhir?'
]

# Hasil Skrining
result = [
    'LANJUT VAKSIN',
    'TUNDA',
    'TIDAK DIBERIKAN'
]

# Catatan Hasil Skrining
notes = [
    'Silakan datang ke Rumah Sakit terdekat untuk Vaksinasi dengan penanganan lebih lanjut',
    'Vaksinasi ke-2 tidak diberikan, bawalah hasil ini ke Lokasi Vaksinasi untuk mendapatkan surat keterangan',
    'Vaksinasi ditunda sampai melahirkan',
    'Jika tidak dalam kondisi akut silakan datang ke lokasi Vaksinasi untuk pemeriksaan lebih lanjut',
    'Vaksinasi ditunda dan Dirujuk',
    'Silakan datang ke lokasi Vaksinasi untuk pengecekan Tekanan Darah dan Suhu Tubuh',
    'Vaksinasi tidak dapat diberikan, berikan keterangan ini jika Ada keperluan yang membutuhkan surat Vaksinasi'
]

# Data calon peserta Vaksinasi
pasien = {
    'Nama' : '',
    'NIK' : '',
    'Jenis-Kelamin' : '',
    'Vaksin Ke' : '',
    'Rentang Umur': '',
    'Status Vaksinasi': '',
    'Catatan': ''
}

# load_skrining function
def load_skrining():
    header = st.container()
    main = st.container()
    panicDetection = st.container()


    # HEADER
    with header:
        st.title('Welcome to paDetect')
        st.text('''
        paDetect adalah aplikasi skrining vaksinasi COVID-19 yang akan 
        mempermudah anda untuk mempercepat antrian di tempat vaksinasi dilakukan, 
        anda hanya perlu cek tekanan darah dan suhu tubuh dan anda akan segera 
        ditangani untuk divaksinasi
        ''')

    # MAIN
    with main:
        st.header('Vaksinasi COVID-19')
        st.text(
        '''
        Isilah form berikut dengan jujur dan benar 
        berdasarkan riwayat medis yang anda miliki
        ''')
        st.info('Jika memiliki gejala penyakit berisiko, periksa kesehatan ke Klinik/Rumah Sakit terdekat terlebih dahulu')
        sel_col, disp_col = st.columns(2)

        # Input nama, NIK, Jenis Kelamin, dan rentang Umur.
        name = sel_col.text_input('Nama Lengkap :', 'Nama Lengkap')
        vacPhase = disp_col.selectbox('Vaksin Ke-', options=['1', '2'], index=0)
        gender = sel_col.selectbox('Jenis Kelamin :', options=['Pria', 'Wanita'], index=0)
        ageRange = disp_col.selectbox('Rentang umur anda sekarang: ', options=['di bawah 18 tahun', '18 tahun ke atas', 'di atas 60 tahun'], index=1)        
        NIK = sel_col.text_input('NIK :', '16 digit NIK Anda')
        pasien.update({
            'Nama' : name,
            'NIK' : NIK,
            'Jenis-Kelamin' : gender,
            'Vaksin Ke' : vacPhase,
            'Rentang Umur': ageRange
        })
        # Konfirmasi NIK dimasukkan dengan jumlah digit yang benar
        if NIK.isdigit()==True and len(NIK) == 16:            
            # vaksin pertama atau kedua
            if vacPhase == '1':
                alergicHist = sel_col.selectbox(screenQuestions[0], options=['Ya', 'Tidak'], index=1)
            else:
                alergicAfterfirstvac = sel_col.selectbox(screenQuestions[1], options=['Ya', 'Tidak'], index=1)
            
            # Pertanyaan tambahan bagi calon peserta vaksinasi wanita, hamil/menyusui?
            if gender == 'Wanita':
                pregOrnot = sel_col.selectbox(screenQuestions[2], options=['Ya', 'Tidak'], index=1)
            
            # Penyakit autoimun (seperti asma dll)
            autoImun = sel_col.selectbox(screenQuestions[3], options=['Ya', 'Tidak'], index=1)

            # Apakah calon peserta vaksinasi sedang dalam masa pengobatan pembekuan darah?
            onBloodmed = sel_col.selectbox(screenQuestions[4], options=['Ya', 'Tidak'], index=1)

            # Apakah calon peserta vaksinasi pengobatan immunosupressant
            onImumed = sel_col.selectbox(screenQuestions[5], options=['Ya', 'Tidak'], index=1)

            # Apakah calon peserta vaksinasi menderita penyakit jantung berat?
            heartDisease = sel_col.selectbox(screenQuestions[6], options=['Ya', 'Tidak'], index=1)
            
            # Pertanyaan tambahan untuk lansia
            if ageRange == 'di atas 60 tahun':
                # Kesulitan menaiki 10 anak tangga, sering lelah, penyakit apa saja, kesulitan berjalan, pengurangan berat badan
                stairsDif = sel_col.selectbox(screenQuestions[7], options=['Ya', 'Tidak'], index=1)
                tiredFreq = sel_col.selectbox(screenQuestions[8], options=['Ya', 'Tidak'], index=1)
                hmDiseases = sel_col.selectbox(screenQuestions[9], options=['Ya', 'Tidak'], index=1)
                walkDif = sel_col.selectbox(screenQuestions[10], options=['Ya', 'Tidak'], index=1)
                weightDec = sel_col.selectbox(screenQuestions[11], options=['Ya', 'Tidak'], index=1)
            
            validation = sel_col.checkbox('Saya sudah mengisi data dengan benar')
            if validation: 
                submit = sel_col.button('Lihat Hasil')
                if submit:
                    st.success('Data Berhasil Disimpan Sebagai berikut!')
                    # DATA SKRINING YANG DIISI CALON PESERTA VAKSIN
                    # VAKSIN PERTAMA
                    if vacPhase=='1':
                        # PRIA RENTANG UMUR 12 TAHUN KE ATAS
                        if gender=='Pria' and (ageRange=='di bawah 18 tahun' or ageRange=='18 tahun ke atas'):
                            st.markdown('---')
                            st.markdown(
                                f'''
                                - DATA SKRINING : {name}
                                - GOLONGAN UMUR : {ageRange}
                                - VAKSIN KE     : {vacPhase}
                                ''' 
                            )
                            st.markdown('---')
                            st.markdown(
                                f'''
                                1. {screenQuestions[0]} : **{alergicHist}**
                                2. {screenQuestions[3]} : **{autoImun}**
                                3. {screenQuestions[4]} : **{onBloodmed}**
                                4. {screenQuestions[5]} : **{onImumed}**
                                5. {screenQuestions[6]} : **{heartDisease}**
                                '''
                            )
                            st.markdown('---')
                            if alergicHist=='Ya':
                                pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[0]})
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                            else:
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                    else :
                                        pasien.update({'Status Vaksinasi':result[0], 'Catatan':notes[5]})

                            st.markdown(
                                f'''
                                * Status Vaksinasi Anda : {pasien['Status Vaksinasi']}
                                * Catatan : {pasien['Catatan']}
                                '''
                            )

                            st.markdown('---')
                        # WANITA 12 TAHUN KE ATAS
                        elif gender=='Wanita' and (ageRange=='di bawah 18 tahun' or ageRange=='18 tahun ke atas'):
                            st.markdown('---')
                            st.markdown(
                                f'''
                                - DATA SKRINING : {name}
                                - GOLONGAN UMUR : {ageRange}
                                - VAKSIN KE     : {vacPhase}
                                ''' 
                            )
                            st.markdown('---')
                            st.markdown(
                                f'''
                                1. {screenQuestions[0]} : **{alergicHist}**
                                2. {screenQuestions[2]} : **{pregOrnot}**
                                3. {screenQuestions[3]} : **{autoImun}**
                                4. {screenQuestions[4]} : **{onBloodmed}**
                                5. {screenQuestions[5]} : **{onImumed}**
                                6. {screenQuestions[6]} : **{heartDisease}**
                                '''
                            )
                            st.markdown('---')
                            if alergicHist=='Ya':
                                pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[0]})
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                    else:
                                        if pregOrnot=='Ya':
                                            pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[2]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                            else:
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if pregOrnot=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[2]})
                                        if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                            pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                    else:
                                        if pregOrnot=='Ya':
                                            pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[2]})
                                        else :
                                            pasien.update({'Status Vaksinasi':result[0], 'Catatan':notes[5]})

                            st.markdown(
                                f'''
                                * Status Vaksinasi Anda : {pasien['Status Vaksinasi']}
                                * Catatan : {pasien['Catatan']}
                                '''
                            )

                            st.markdown('---')
                        # LANSIA
                        else:
                            st.markdown('---')
                            st.markdown(
                                f'''
                                - DATA SKRINING : {name}
                                - GOLONGAN UMUR : {ageRange}
                                - VAKSIN KE     : {vacPhase}
                                ''' 
                            )
                            st.markdown('---')
                            st.markdown(
                                f'''
                                1. {screenQuestions[0]} : **{alergicHist}**
                                2. {screenQuestions[3]} : **{autoImun}**
                                3. {screenQuestions[4]} : **{onBloodmed}**
                                4. {screenQuestions[5]} : **{onImumed}**
                                5. {screenQuestions[6]} : **{heartDisease}**
                                6. {screenQuestions[7]} : **{stairsDif}**
                                7. {screenQuestions[8]} : **{tiredFreq}**
                                8. {screenQuestions[9]} : **{hmDiseases}**
                                9. {screenQuestions[10]} : **{walkDif}**
                                10. {screenQuestions[11]} : **{weightDec}**
                                '''
                            )
                            st.markdown('---')
                            if alergicHist=='Ya':
                                pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[0]})
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else:
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})                                    
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else:
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})                                                                                                     
                            else:
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else:
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})                                     
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else :
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                        else:
                                            pasien.update({'Status Vaksinasi':result[0], 'Catatan':notes[5]})

                            st.markdown(
                                f'''
                                * Status Vaksinasi Anda : {pasien['Status Vaksinasi']}
                                * Catatan : {pasien['Catatan']}
                                '''
                            )

                            st.markdown('---')
                    # VAKSIN KE-2
                    else:
                        # PRIA 12 TAHUN KE ATAS
                        if gender=='Pria' and (ageRange=='di bawah 18 tahun' or ageRange=='18 tahun ke atas'):
                            st.markdown('---')
                            st.markdown(
                                f'''
                                - DATA SKRINING : {name}
                                - GOLONGAN UMUR : {ageRange}
                                - VAKSIN KE     : {vacPhase}
                                ''' 
                            )
                            st.markdown('---')
                            st.markdown(
                                f'''
                                1. {screenQuestions[1]} : **{alergicAfterfirstvac}**
                                2. {screenQuestions[3]} : **{autoImun}**
                                3. {screenQuestions[4]} : **{onBloodmed}**
                                4. {screenQuestions[5]} : **{onImumed}**
                                5. {screenQuestions[6]} : **{heartDisease}**
                                '''
                            )
                            st.markdown('---')
                            if alergicAfterfirstvac=='Ya':
                                pasien.update({'Status Vaksinasi':result[2], 'Catatan':notes[1]})
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                            else:
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                    else :
                                        pasien.update({'Status Vaksinasi':result[0], 'Catatan':notes[5]})

                            st.markdown(
                                f'''
                                * Status Vaksinasi Anda : {pasien['Status Vaksinasi']}
                                * Catatan : {pasien['Catatan']}
                                '''
                            )

                            st.markdown('---')
                        # WANITA 12 TAHUN KE ATAS
                        elif gender=='Wanita' and (ageRange=='di bawah 18 tahun' or ageRange=='18 tahun ke atas'):
                            st.markdown('---')
                            st.markdown(
                                f'''
                                - DATA SKRINING : {name}
                                - GOLONGAN UMUR : {ageRange}
                                - VAKSIN KE     : {vacPhase}
                                ''' 
                            )
                            st.markdown('---')
                            st.markdown(
                                f'''
                                1. {screenQuestions[1]} : **{alergicAfterfirstvac}**
                                2. {screenQuestions[2]} : **{autoImun}**
                                3. {screenQuestions[3]} : **{onBloodmed}**
                                4. {screenQuestions[4]} : **{onImumed}**
                                5. {screenQuestions[5]} : **{heartDisease}**
                                6. {screenQuestions[6]} : **{pregOrnot}**
                                '''
                            )
                            st.markdown('---')
                            if alergicAfterfirstvac=='Ya':
                                pasien.update({'Status Vaksinasi':result[2], 'Catatan':notes[1]})
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                    else:
                                        if pregOrnot=='Ya':
                                            pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[2]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                            else:
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if pregOrnot=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[2]})
                                        if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                            pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                    else:
                                        if pregOrnot=='Ya':
                                            pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[2]})
                                        else :
                                            pasien.update({'Status Vaksinasi':result[0], 'Catatan':notes[5]})

                            st.markdown(
                                f'''
                                * Status Vaksinasi Anda : {pasien['Status Vaksinasi']}
                                * Catatan : {pasien['Catatan']}
                                '''
                            )

                            st.markdown('---')

                        # LANSIA
                        else:
                            st.markdown('---')
                            st.markdown(
                                f'''
                                - DATA SKRINING : {name}
                                - GOLONGAN UMUR : {ageRange}
                                - VAKSIN KE     : {vacPhase}
                                ''' 
                            )
                            st.markdown('---')
                            st.markdown(
                                f'''
                                1. {screenQuestions[1]} : **{alergicAfterfirstvac}**
                                2. {screenQuestions[3]} : **{autoImun}**
                                3. {screenQuestions[4]} : **{onBloodmed}**
                                4. {screenQuestions[5]} : **{onImumed}**
                                5. {screenQuestions[6]} : **{heartDisease}**
                                6. {screenQuestions[7]} : **{stairsDif}**
                                7. {screenQuestions[8]} : **{tiredFreq}**
                                8. {screenQuestions[9]} : **{hmDiseases}**
                                9. {screenQuestions[10]} : **{walkDif}**
                                10. {screenQuestions[11]} : **{weightDec}**
                                '''
                            )
                            st.markdown('---')
                            if alergicAfterfirstvac=='Ya':
                                pasien.update({'Status Vaksinasi':result[2], 'Catatan':notes[1]})
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else:
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})                                    
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else:
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})                                                                                                     
                            else:
                                if autoImun=='Ya':
                                    pasien.update({'Status Vaksinasi':result[1], 'Catatan':notes[3]})
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else:
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})                                     
                                else:
                                    if onBloodmed=='Ya' or onImumed=='Ya' or heartDisease=='Ya':
                                        pasien.update({'Status Vaksinasi':result[1], 'Catatan': notes[4]})
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                    else :
                                        if (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya') or(stairsDif=='Ya' and tiredFreq=='Ya' and hmDiseases=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and tiredFreq=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (stairsDif=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (stairsDif=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and walkDif=='Ya') or (tiredFreq=='Ya' and hmDiseases=='Ya' and weightDec=='Ya') or (tiredFreq=='Ya' and walkDif=='Ya' and weightDec=='Ya') or (hmDiseases=='Ya' and walkDif=='Ya' and weightDec=='Ya'):
                                            pasien.update({'Status Vaksinasi':result[2], 'Catatan': notes[6]})
                                        else:
                                            pasien.update({'Status Vaksinasi':result[0], 'Catatan':notes[5]})

                            st.markdown(
                                f'''
                                * Status Vaksinasi Anda : {pasien['Status Vaksinasi']}
                                * Catatan : {pasien['Catatan']}
                                '''
                            )

                            st.markdown('---')
            
        else:
            st.warning('Masukkan NIK dengan benar!')

        
    # DETEKSI PANIK
    if pasien['Status Vaksinasi'] == 'LANJUT VAKSIN' or (pasien['Status Vaksinasi']=='TUNDA' and (pasien['Catatan']==notes[0] or pasien['Catatan']==notes[3] )):
        with panicDetection:
            st.subheader('Unggah Foto Selfie Terkini Anda')
            foto = st.file_uploader("Pilih foto!", type=['jpg', 'png', 'jpeg'])
            if foto is not None:
                st.image(foto, use_column_width=False)
                save_image_path = './upload_images/'+foto.name
                with open(save_image_path, "wb") as f:
                    f.write(foto.getbuffer())
                
                if st.button("Simpan"):
                    hasil = process_image(save_image_path)
                    print(hasil)    
                    st.success("Ekspresi Anda menunjukkan bahwa anda sedang: "+hasil)