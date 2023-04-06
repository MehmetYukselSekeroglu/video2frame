# video2frame
Videoları kare kare ayırmak için basit python3 programı. Web üzerinen bulamadım basit ama lazım oluyor.

<hr>
Videoları incelerken daha fazla kolaylık sağlaması için karelere ayırır vlc de vs işlem çok karmaşık 
olduğu için pek sevemedim açıkçası.

<hr>
<h2>Kullanım: </h2>
Gereksinimler:
python3.X ve OpenCv

```sh
# Kullanım:
python3 video2frame.py --video /home/user/video.mp4 
```

```sh
# Her başlatma sorunası tmp/cv2output altını temizler ama ellede temizlenebilir
python3 video2frame.py --clsoutdir 
```

işlem sonuçlarını çalıştırıldığı klasör içerisinde tmp/cv2output altına atar 
Fazla kare çıkmasın diye sıra numarası tek olan kareleri kaydeder sadece.

<h2>Örnek:</h2>
</br>
<img src="img/example.png" /> 

