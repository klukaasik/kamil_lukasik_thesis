# Platforma wspierająca korektę transkrypcji mowy do tekstu

Aby móc skonfigurować lokalnie tę platformę, należy przejść przez następujące kroki:
<br />
1. Stwórz środowisko wirtualne <br />
Nie jest konieczne, ale jest przydatne. W PyCharm wirtualne środowisko można dodać w momencie dodawania interpretera do projektu. Aplikacja została napisana w języku Python w wersji 3.9. Wirtualne środowisko można stworzyć jak na screenie poniżej.

![image](https://user-images.githubusercontent.com/56301469/201491354-394e1d77-21b5-4c43-a41d-1350c00c6b6c.png)
<br />
2. Pobierz potrzebne biblioteki <br />
W terminalu, w miejscu projektu pobierz bibliotekę PyQt5 służąca do tworzenia i wyświetlania interfejsów graficznych za pomocą komendy:
```
pip install pyqt5
``` 
Przykład poniżej:

![image](https://user-images.githubusercontent.com/56301469/201491494-cf7646c2-8965-4302-8f35-8c050b6f3bc0.png)

W podobny sposób zainstaluj biblioteki:
```
pip install pyqt5-tools
pip install git+https://github.com/openai/whisper.git 
pip install rich
pip install pysrt
```
<br />
3. Gotowe! <br />
Teraz wystarczy włączyć aplikację. Należy włączyć główny skrypt aplikacji "app.py".

![image](https://user-images.githubusercontent.com/56301469/201491630-0d95c170-2eae-4081-972c-f1774e3b0f28.png)
<br />

Tak powinna wyglądać aplikacja po włączeniu:

![image](https://user-images.githubusercontent.com/56301469/201491684-e4e74f86-2fe8-44e8-a503-270840d1298e.png)


# Ważne:

Pliki audio wraz z transkrypcjami powinny znajdować się w pliku "transcriptions".

