from lyrics_extractor import SongLyrics
# použití knihovny lyrics extractor, která umí vytáhnout text z libovolné stránky 

extract_lyrics = SongLyrics(
    "AIzaSyCPi_kZSILOOrnuC-C-CTtjqbf-3rcNGI0", "2db71dfdf9b3d790b")
# API key a Engine ID stránky www.genius.com, díky kterým to může fungovat

temp = extract_lyrics.get_lyrics(str(input("songname: ")))
# input pro zadání songu

print("#### "+temp["title"]+" ####\n")
# vypíše celý název songu

print(temp["lyrics"])
# vypíše text songu