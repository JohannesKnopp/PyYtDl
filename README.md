# PyYtDl - by JK
## config.ini
#### download_list_location
Path to the input file (where the youtube-links are).
#### output_directory
Where the files will be saved.
You can specify a directory that doesn't exist yet, it will be created for you.
#### output_format
In which format you want your audio files. Currently supported are mp3, m4a, avi, flv, wav, ogg, webm.
Please note that meta tagging will only work with mp3, m4a and ogg.
#### meta_tagging_delimiter
Which character (or string) is used to set the audio-meta-tags and the file name. Default is ">", but you can use whatever you like, even multiple characters: ">~", "~~~~~" and so on.
#### Important:
Note that all four parameters must have correct values for the program to work. For the first two, correct directory paths. For the third one, one of the supported audio formats and for the last one a delimiter that has no chance to show up in the url or that you want to use as title / artist (e.g. don't use = as the delimiter). Also you have to specify one, even if you don't intend to use it, otherwise the program doesn't work.

---
## download_list.txt
---

- Doesn't have to be in the folder, but has to be mentioned in config.ini.
- Put each link in a separate line.
- Links to playlists will only download the song the link points to (i.e. link is 6th song of the playlist, only that song will be downloaded).
- To set the file name and the meta tags, use the delimiter specified in config.ini. After the first delimiter, write the artist of the song. After the second delimiter, write the song title / file name.
Example(in this case the delimiter is ">"):
```
https://www.youtube.com/watch?v=SomeYtIdXYZ >Artist >Title
```
This would produce a file called `Title.mp3` (if the audio format is set to mp3) and the meta tags be would as mentioned  above.
The tagging is completly optional, if you don't use it, the file name will be the name of the video on YouTube.
You don't have to use one method exclusively, it is no problem to download files with and without tagging in the the same execution of the program.

---
## Developer notes
---

The program is far from perfect, but I only made it for myself, it was never intended to be a real stand-alone application. I'm happy if you find any use for it anyways :)

_~ JK_