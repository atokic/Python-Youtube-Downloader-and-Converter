print("YouTube Downloader and Converter")

import pytube
import youtube_downloader
import file_converter

print('''
Što želite napraviti?

(1) Preuzimanje YouTube videozapisa ručno
(2) Preuzimanje YouTube playliste
(3) Preuzimanje YouTube videozapisa i pretvaranje u .mp3 format

Preuzimanje YouTube videozapisa zaštićenih autorskim pravima je protuzakonito!
Ne snosim odgovornost za vaša preuzimanja! Preuzimate na vlastitu odgovornost!

Copyright (c) 2023
''')

choice = input("Izbor: ")

if choice == "1" or choice == "2":
    quality = input("Odaberite kvalitetu (low, medium, high, very high):")
    if choice == "2":
        link = input("Unesite link na popis za reprodukciju: ")
        print("Preuzimanje popisa za reprodukciju...")
        youtube_downloader.download_playlist(link, quality)
        print("Preuzimanje završeno!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Preuzimanje u tijeku...")
        filename = youtube_downloader.download_video(link, 'low')
        print("Pretvaranje videozapisa u tijeku...")
        file_converter.convert_to_mp3(filename)
else:
    print("Pogrešan unos! Prekid...")