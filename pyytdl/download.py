import os
import re
import configparser
import pafy
from pydub.exceptions import CouldntEncodeError
from pyytdl import PyYtDl

pyytdl = PyYtDl()

conf_params = configparser.RawConfigParser()
config_file_path = "config.ini"
conf_params.read(config_file_path)

download_list_location = os.path.join(conf_params.get("config", r"download_list_location"))
output_directory = os.path.join(conf_params.get("config", r"output_directory"))
output_format = conf_params.get("config", "output_format").strip()
mtd = conf_params.get("config", r"meta_tagging_delimiter").strip()

if not os.path.isdir(output_directory):
    os.makedirs(output_directory)

if not output_directory.endswith("\\"):
    output_directory += "\\"

file = open(download_list_location, "r")
regex_mask = re.compile(r"" + re.escape(mtd) + ".*" + re.escape(mtd) + ".*")


for line in file:
    is_metadata = False
    if(regex_mask.search(line)):
        is_metadata = True

    song = list(map(str.strip, line.split(r"" + mtd)))

    try:
        stream = pafy.new(song[0])
    except ValueError:
        if song[0].__len__() > 0:
            print("ERROR: " + song[0] + " is not a valid youtube-url or 11 character Id")
        continue

    if not is_metadata:
        song.extend([None, stream.title])

    output_file_path = os.path.join(output_directory + song[2] + "." + output_format)

    if os.path.isfile(output_file_path):
        print("ERROR: " + output_file_path + " already exists!")
        continue

    try:
        pyytdl.download_song(stream, song[2], output_directory)
    except FileExistsError:
        print("ERROR: file already exists")
        os.remove(os.path.join(output_directory + song[2] + ".m4a"))
        continue

    if output_format != "m4a":
        try:
            pyytdl.convert_audio(output_directory + song[2] + ".m4a", "m4a", output_directory,
                                 output_format, song[2])
            os.remove(os.path.join(output_directory + song[2] + ".m4a"))
        except CouldntEncodeError:
            print("ERROR: file format not supported")
            os.remove(output_file_path)
            continue

    if is_metadata:
        if output_format == "wav":
            print("INFO: Meta tagging not supported in .wav format")
        try:
            pyytdl.tag_audio_file(output_file_path, song[1], song[2])
        except OSError:
            print("INFO: Meta tagging not supported in ." + output_format + " format")


    print("Successfully downloaded " + song[2] + "." + output_format)

print("Download finished!")