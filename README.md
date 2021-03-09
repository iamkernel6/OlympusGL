# APK yang di perlukan
- Termux

# Cara install

* Note : Sebelum membuka apk Termux Allow Storage Permision terlebih dahulu
- Caranya, Buka pengaturan -> Aplikasi -> Termux -> Izin -> Izinkan akses penyimpanan

* Setelah mengisinkan akses penyimpanan ikuti cara menginstall script di bawah ini :
- Buka Termux 
- Tuliskan command di bawah ini :
                                
                                pkg install root-repo
                                
                                pkg install unstable-repo
                                
                                pkg install x11-repo
                                
                                pkg update -y
                                
                                pkg upgrade -y
                                
                                pkg install python

                                pkg install python-pip
                                
                                pkg install git
                                
                                git clone http://.git
                                
                                cd OlympusGL

                                pip install -r requirements.txt

                                python olympusgl.py

- Selesai

* Untuk melihat command yang tersedia ketik 'help'
