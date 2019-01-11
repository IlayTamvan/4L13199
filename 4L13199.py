import os, sys
###############
# Dede : Hair #
# Fors : Repo #
###############
try:
 print('')
 print('[0m=====================================================[0;91m')
 os.system('figlet AUTOMATIC')
 print('[0m=====================================================')
 print('[+_+] Penyususun Tamvan [[0;93mIlay[0m]')
 
 print('[+_+] Repo Github Milik [[0;93m4L13199[0m]')
 print(''''[0m====================================================
 [0;92m[[0m1[0;92m] [0mInstall[0;93m FabricLTE
 [0;92m[[0m2[0;92m] [0mInstall[0;93m LITEBOT
 [0;92m[[0m3[0;92m] [0mInstall[0;93m LITEDDOS
 [0;92m[[0m4[0;92m] [0mInstall[0;93m LITEFONT
 [0;92m[[0m5[0;92m] [0mInstall[0;93m LITESCRIPT
 [0;92m[[0m6[0;92m] [0mInstall[0;93m LITESPAM
 [0;92m[[0m7[0;92m] [0mInstall[0;93m LITETOOLS
 [0;92m[[0m8[0;92m] [0mInstall[0;93m meTAInstall
 [0;92m[[0m9[0;92m] [0mInstall[0;93m SETOOLKIT''')
 f=["https://github.com/4L13199/FabricLTE.git", "https://github.com/4L13199/LITEBOT.git", "https://github.com/4L13199/LITEDDOS.git", "https://github.com/4L13199/LITEFONT.git", "https://github.com/4L13199/LITESCRIPT.git", "https://github.com/4L13199/LITESPAM.git", "https://github.com/4L13199/LITETOOLS.git", "https://github.com/4L13199/meTAInstall.git", "https://github.com/4L13199/SETOOLKIT.git"]
 print('[0m=====================================================')
 Plh = input('[0;93m[><][0m Install Nomer : ')
 print('=====================================================')
 Y=f[Plh-1]
 if f !=[]:
   try:
     os.system('git clone '+Y)
     print('=====================================================')
     print('[><] Selesai Install (Cek Folder)')
     os.system('ls')
     print('=====================================================')
   except(ImportError):
     sys.exit()
 else:
   print('[!!] Url Kosong (Cek Ulang)')
   print('=====================================================')
except(ImportError):
  sys.exit()