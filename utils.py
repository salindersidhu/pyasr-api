import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def merge_sentences(sentence_a, sentence_b):
	words_a = sentence_a.split(' ')
	words_b = sentence_b.split(' ')
	overlap = [x for x in words_a if x in words_b]
	start_point = words_a.index(overlap[0])
	end_point = len(words_b) - words_b[::-1].index(overlap[-1])
	return ' '.join(words_a[0:start_point] + overlap + words_b[end_point:])

def convert_audio_file(fname_in, fname_out, **kwargs):
	src = os.path.join(os.getcwd(), fname_in)
	dest = os.path.join(os.getcwd(), fname_out)
	src_ext = os.path.splitext(src)[1][1:]
	audio = AudioSegment.from_file(src, src_ext)
	audio.export(dest, **kwargs)
