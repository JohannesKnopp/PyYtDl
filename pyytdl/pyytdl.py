import pafy
import configparser
import os
import re
import taglib

conf_params = configparser.RawConfigParser()
config_file_path = "config.ini"
conf_params.read(config_file_path)

download_list_location = os.path.join(conf_params.get("config", r"download_list_location"))
output_location = os.path.join(conf_params.get("config", r"output_location"))
mtd = conf_params.get("config", r"meta_tagging_delimiter").strip()

if not os.path.isdir(output_location):
    os.mkdir(output_location)

if not output_location.endswith("\\"):
    output_location += "\\"

file = open(download_list_location, "r")

regex_mask = re.compile(r"" + re.escape(mtd) + ".*" + re.escape(mtd) + ".*")

for line in file:
    is_metadata = False
    if regex_mask.search(line):
        is_metadata = True
    song = list(map(str.strip, line.split(r""+mtd)))

    try:
        video = pafy.new(song[0])
    except ValueError:
        if song[0].__len__() > 0:
            print("ERROR: " + song[0] + " is not a valid youtube-url or 11 character Id")
        continue

    audio = video.getbestaudio("m4a")

    if is_metadata:
        try:
            audio.download(output_location + song[1] + ".m4a")
            audio_file = taglib.File(output_location + song[1] + ".m4a")
            audio_file.tags["TITLE"], audio_file.tags["ARTIST"] = song[1], song[2]
            audio_file.save()
            audio_file.close()
            print("Successfully downloaded " + song[1] + ".m4a")
        except FileExistsError:
            print("ERROR: " + song[1] + ".m4a already exists")
            os.remove(os.path.join(output_location, song[1] + ".m4a.temp"))
    else:
        try:
            audio.download(output_location)
            print("Successfully downloaded " + video.title + ".m4a")
        except FileExistsError:
            print("ERROR: " + video.title + ".m4a already exists")
            os.remove(os.path.join(output_location, video.title + ".m4a.temp"))

print("Download finished!")