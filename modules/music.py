from pygame import mixer
import modules.find_path as m_path

mixer.init()

list_songs_name = ["songs/despasito.mp3", "songs/myself.mp3", "songs/nostylist.mp3","songs/omsk.mp3", "songs/paranoid.mp3", "songs/pokolenie.mp3", "songs/slimshady.mp3"]   

mixer.music.load(m_path.find_path_to_file(list_songs_name[0]))