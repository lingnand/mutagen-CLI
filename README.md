# mutagen-CLI

[mutagen-CLI](http://mutagen.lynnard.tk) is a [mutagen][mutagen] frontend that handles universal ID3 music tagging.

## Install

Development version from Github:

    pip install https://github.com/maphew/mutagen-CLI/archive/master.zip 


## Usage

    $ mutagenc

    usage: Change or manipulate the ID3 tags of the audio files
           [-h] [--artist ARTIST] [--album ALBUM] [--title TITLE] [--wors WORS]
           [--year YEAR] [--cover COVER] [--format FORMAT] [--separator SEPARATOR]
           [--escape ESCAPE]
           audiofile [audiofile ...]

    positional arguments:
      audiofile             an audio file containing the ID3 tags

    optional arguments:
      -h, --help            show this help message and exit
      --artist ARTIST, -a ARTIST
                            set the artist name
      --album ALBUM, -A ALBUM
                            set the album name
      --title TITLE, -t TITLE
                            set the title name
      --wors WORS, -r WORS  set the internet radio url
      --year YEAR, -Y YEAR  set the release year
      --cover COVER, -c COVER
                            set the cover image
      --format FORMAT, -f FORMAT
                            return the ID3 information as a formatted string; the
                            format string should containing one or more of the
                            following specifiers: , {artist} , {title} , {album} ,
                            {year} , {kbps} , {wors} , {len} (the length of the
                            audio file, in seconds) , {path} (the absolute path of
                            the file)
      --separator SEPARATOR, -s SEPARATOR
                            define the separator used to append at the end of the
                            output for each file (excluding the last file)
      --escape ESCAPE, -e ESCAPE
                            define the characters that should be escaped in all
                            the outputed fields
        usage: Change or manipulate the ID3 tags of the audio files
               [-h] [--artist ARTIST] [--album ALBUM] [--title TITLE] [--wors WORS]
               [--year YEAR] [--cover COVER] [--format FORMAT] [--separator SEPARATOR]
               [--escape ESCAPE]
               audiofile [audiofile ...]

[mutagen]: https://www.github.com/nex3/mutagen
