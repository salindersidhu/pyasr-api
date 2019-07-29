import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

def merge_sentences(sentence_a, sentence_b):
	frag_a = sentence_a.split(' ')
	frag_b = sentence_b.split(' ')
	overlap = [x for x in frag_a if x in frag_b]
	frag_overlap_start = frag_a.index(overlap[0])
	frag_overlap_end = len(frag_b) - frag_b[::-1].index(overlap[-1])
	return ' '.join(frag_a[0:frag_overlap_start] + overlap + frag_b[frag_overlap_end:])

def convert_audio(file_in, file_out, **kwargs):
	src = os.path.join(os.getcwd(), file_in)
	dst = os.path.join(os.getcwd(), file_out)
	src_ext = os.path.splitext(src)[1][1:]
	audio = AudioSegment.from_file(src, src_ext)
	audio.export(dst, **kwargs)
