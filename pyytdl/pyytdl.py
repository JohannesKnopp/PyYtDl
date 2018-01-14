import taglib
from pydub import AudioSegment


class PyYtDl:

    def download_song(self, stream, title, output_directory):
        audio = stream.getbestaudio("m4a")
        audio.download(output_directory + title + ".m4a")

    def convert_audio(self, input_file, input_format, output_directory, output_format, title):
        audio = AudioSegment.from_file(input_file, format=input_format)
        audio.export(output_directory + title + "." + output_format, format=output_format)

    def tag_audio_file(self, input_file, artist, title):
        tag_file = taglib.File(input_file)
        tag_file.tags["ARTIST"] = artist
        tag_file.tags["TITLE"] = title
        tag_file.save()
        tag_file.close()