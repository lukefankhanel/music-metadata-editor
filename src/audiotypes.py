
from abc import ABC, abstractmethod
from mutagen.oggopus import OggOpus
from mutagen.mp4 import MP4
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3, TRCK, TPOS, TIT2, TPE1, TALB, TDRC, TCON, TCOM, WXXX, TXXX, COMM, TIT1


def createFileObject(fileLocation):
    if fileLocation.endswith(".opus"):
        return OGGFile(fileLocation)
    elif fileLocation.endswith(".m4a") or fileLocation.endswith(".mp4"):
        return MP4File(fileLocation)
    elif fileLocation.endswith(".flac"):
        return FLACFile(fileLocation)
    elif fileLocation.endswith(".mp3"):
        return MP3File(fileLocation)
    else:
        return None



class SongFile(ABC):
    def getMetadataField(self, field):
        try:
            return self.file[field][0]
        except:
            return ""
    
    def getMetadataFieldNumber(self, field):
        try:
            number = self.getMetadataField(field)
            return 0 if number == "" else int(number)
        except:
            return 0
    
    def setMetadataField(self, field, value):
        self.file[field] = value


    def getTrackNumberCurrent(self):
        return self.getMetadataFieldNumber("tracknumber")
    def setTrackNumberCurrent(self, value):
        self.setMetadataField("tracknumber", str(value))
    
    def getTrackNumberMaximum(self):
        return self.getMetadataFieldNumber("tracktotal")
    def setTrackNumberMaximum(self, value):
        self.setMetadataField("tracktotal", str(value))
    
    def getDiskNumberCurrent(self):
        return self.getMetadataFieldNumber("discnumber")
    def setDiskNumberCurrent(self, value):
        self.setMetadataField("discnumber", str(value))
    
    def getDiskNumberMaximum(self):
        return self.getMetadataFieldNumber("disctotal")
    def setDiskNumberMaximum(self, value):
        self.setMetadataField("disctotal", str(value))

    def getTitle(self):
        return self.getMetadataField("title")
    def setTitle(self, value):
        self.setMetadataField("title", value)

    def getArtist(self):
        return self.getMetadataField("artist")
    def setArtist(self, value):
        self.setMetadataField("artist", value)

    def getAlbum(self):
        return self.getMetadataField("album")
    def setAlbum(self, value):
        self.setMetadataField("album", value)

    def getDate(self):
        return self.getMetadataField("date")
    def setDate(self, value):
        self.setMetadataField("date", value)

    def getGenre(self):
        return self.getMetadataField("genre")
    def setGenre(self, value):
        self.setMetadataField("genre", value)

    def getComposer(self):
        return self.getMetadataField("composer")
    def setComposer(self, value):
        self.setMetadataField("composer", value)

    def getURL(self):
        return self.getMetadataField("url")
    def setURL(self, value):
        self.setMetadataField("url", value)

    def getReplayGain(self):
        replayGain = self.getMetadataField("replaygain_track_gain")
        return 0 if replayGain == "" else self.convertReplayGainToFloat(replayGain)
    def setReplayGain(self, value):
        self.setMetadataField("replaygain_track_gain", self.convertFloatToReplayGain(value))
    def convertReplayGainToFloat(self, value):
        try:
            return float(value.split()[0])
        except:
            return 0
    def convertFloatToReplayGain(self, value):
        # https://stackoverflow.com/questions/6149006/how-to-display-a-float-with-two-decimal-places
        return "%.2f" % value + " dB"

    def getComment(self):
        return self.getMetadataField("comment")
    def setComment(self, value):
        self.setMetadataField("comment", value)

    def getDescription(self):
        return self.getMetadataField("description")
    def setDescription(self, value):
        self.setMetadataField("description", value)

    def getAllFileMetadata(self):
        return self.file.pprint()

    def saveMetadata(self):
        self.file.save()
    

class FLACFile(SongFile):
    def __init__(self, fileLocation):
        self.file = FLAC(fileLocation)


class OGGFile(SongFile):
    def __init__(self, fileLocation):
        self.file = OggOpus(fileLocation)

    def getURL(self):
        return self.getMetadataField("purl")
    def setURL(self, value):
        self.setMetadataField("purl", value)


class MP3File(SongFile):
    def __init__(self, fileLocation):
        self.file = ID3(fileLocation)
    
    def setMetadataField(self, value):
        self.file.add(value)

    def splitTrackDiskInteger(self, value, space):
        try:
            return int(value.split("/")[space])
        except:
            return 0

    def getTrackNumberCurrent(self):
        return  self.splitTrackDiskInteger(self.getMetadataField("TRCK"), 0)
    def setTrackNumberCurrent(self, value):
        self.setMetadataField(TRCK(encoding=3, text=(str(value) + "/" + str(self.getTrackNumberMaximum()))))
    
    def getTrackNumberMaximum(self):
        return  self.splitTrackDiskInteger(self.getMetadataField("TRCK"), 1)
    def setTrackNumberMaximum(self, value):
        self.setMetadataField(TRCK(encoding=3, text=(str(self.getTrackNumberCurrent()) + "/" + str(value))))
    
    def getDiskNumberCurrent(self):
        return  self.splitTrackDiskInteger(self.getMetadataField("TPOS"), 0)
    def setDiskNumberCurrent(self, value):
        self.setMetadataField(TPOS(encoding=3, text=(str(value) + "/" + str(self.getDiskNumberMaximum()))))
    
    def getDiskNumberMaximum(self):
        return  self.splitTrackDiskInteger(self.getMetadataField("TPOS"), 1)
    def setDiskNumberMaximum(self, value):
        self.setMetadataField(TPOS(encoding=3, text=(str(self.getDiskNumberCurrent()) + "/" + str(value))))

    def getTitle(self):
        return self.getMetadataField("TIT2")
    def setTitle(self, value):
        self.setMetadataField(TIT2(encoding=3, text=value))

    def getArtist(self):
        return self.getMetadataField("TPE1")
    def setArtist(self, value):
        self.setMetadataField(TPE1(encoding=3, text=value))

    def getAlbum(self):
        return self.getMetadataField("TALB")
    def setAlbum(self, value):
        self.setMetadataField(TALB(encoding=3, text=value))

    def getDate(self):
        return str(self.getMetadataField("TDRC"))
    def setDate(self, value):
        self.setMetadataField(TDRC(encoding=3, text=value))

    def getGenre(self):
        return self.getMetadataField("TCON")
    def setGenre(self, value):
        self.setMetadataField(TCON(encoding=3, text=value))

    def getComposer(self):
        return self.getMetadataField("TCOM")
    def setComposer(self, value):
        self.setMetadataField(TCOM(encoding=3, text=value))

    def getURL(self):
        frames = self.file.getall("WXXX")
        for frame in frames:
            if frame.url:
                return frame.url
        return ""
    def setURL(self, value):
        self.setMetadataField(WXXX(encoding=3, desc="", url=value))

    def getReplayGain(self):
        # https://stackoverflow.com/questions/4040605/does-anyone-have-good-examples-of-using-mutagen-to-write-to-files
        # https://python.hotexamples.com/examples/mutagen.mp3/-/add_tags/python-add_tags-function-examples.html
        # https://mutagen.readthedocs.io/en/latest/user/id3.html
        # https://mutagen.readthedocs.io/en/latest/api/id3_frames.html
        frames = self.file.getall("TXXX")
        for frame in frames:
            if frame.desc == "replaygain_track_gain":
                return self.convertReplayGainToFloat(frame.text[0])
        return 0.00
    def setReplayGain(self, value):
        self.setMetadataField(TXXX(encoding=3, desc="replaygain_track_gain", text=self.convertFloatToReplayGain(value)))

    def getComment(self):
        frames = self.file.getall("COMM")
        print(frames)
        for frame in frames:
            if len(frame.text) > 0:
                return frame.text[0]
        return ""
    def setComment(self, value):
        self.setMetadataField(COMM(encoding=3, desc="", lang="eng", text=value))

    def getDescription(self):
        return self.getMetadataField("TIT1")
    def setDescription(self, value):
        self.setMetadataField(TIT1(encoding=3, text=value))


class MP4File(SongFile):
    def __init__(self, fileLocation):
        self.file = MP4(fileLocation)

    def getTitle(self):
        return self.getMetadataField("\xa9nam")
    def setTitle(self, value):
        self.setMetadataField("\xa9nam", value)

    def getArtist(self):
        return self.getMetadataField("\xa9ART")
    def setArtist(self, value):
        self.setMetadataField("\xa9ART", value)

    def getAlbum(self):
        return self.getMetadataField("\xa9alb")
    def setAlbum(self, value):
        self.setMetadataField("\xa9alb", value)

    def getDate(self):
        return self.getMetadataField("\xa9day")
    def setDate(self, value):
        self.setMetadataField("\xa9day", value)

    def getGenre(self):
        return self.getMetadataField("\xa9gen")
    def setGenre(self, value):
        self.setMetadataField("\xa9gen", value)

    def getComposer(self):
        return self.getMetadataField("\xa9wrt")
    def setComposer(self, value):
        self.setMetadataField("\xa9wrt", value)

    def getURL(self):
        return self.getMetadataField("purl")
    def setURL(self, value):
        self.setMetadataField("purl", value)

    def getDescription(self):
        return self.getMetadataField("desc")
    def setDescription(self, value):
        self.setMetadataField("desc", value)

    def getComment(self):
        return self.getMetadataField("\xa9cmt")
    def setComment(self, value):
        self.setMetadataField("\xa9cmt", value)

