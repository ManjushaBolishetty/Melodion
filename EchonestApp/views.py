# -*- coding: utf-8 -*-
from pyechonest import config
config.ECHO_NEST_API_KEY = 'QRSITE4FCSBOPXOLA'

from django.http import HttpResponse
from django.shortcuts import render
from pyechonest import song
from django.template import RequestContext, loader
from pyechonest.util import EchoNestAPIError
import pprint



def index(request):
    return render(request, 'index.html')

def get_song_key(key_index, mode):
    notelist=['C','C#','D','Eb','E','F','F#','G','G#','A','A#','B']
    modelist=['Minor','Major']
    return notelist[key_index] + '-' + modelist[mode]

def get_notes(song_key):
	scale_to_note_map = {'C-Minor':'C, D, Eb, F, G, Ab, Bb',
			     'C-Major':'C, D, E, F, G, A, B',
                 'C#-Minor':'C♯, D♯, E, F♯, G♯, A, B',
                 'C#-Major':'C♯, D♯, E♯, F♯, G♯, A♯, B♯',
                 'D-Minor':'D, E, F, G, A, B♭, C',
                 'D-Major':'D, E, F♯, G, A, B, C♯',
                 'F-Minor':'F, G, A♭, B♭, C, D♭, E♭',
                 'F-Major':'F, G, A, B♭, C, D, E',
                 'EB-Minor':'E♭, F, G♭, A♭, B♭, C♭, D♭',
                 'EB-Major':'E♭, F, G, A♭, B♭, C, D',
                 'E-Minor':'E, F♯,G, A, B, C, D',
                 'E-Major':'E, F♯, G♯, A, B, C♯, D♯',
                 'F-Minor':'F, G, A♭, B♭, C, D♭, E♭',
                 'F-Major':'F, G, A, B♭, C, D, E',
                 'F#-Minor':'F♯, G♯, A, B, C♯, D, E',
                 'F#-Major':'F♯, G♯, A♯, B, C♯, D♯, E♯',
                 'G-Minor':'G, A, B♭, C, D, E♭, F',
                 'G-Major':'G, A, B, C, D, E, F♯',
                 'G#-Minor':'G♯, A♯, B, C♯, D♯, E, F♯',
                 'G#-Major':'G♯, A♯, B♯, C♯, D♯, E♯, F##',
                 'A-Minor':'A, B, C, D, E, F, G',
                 'A-Major':'A, B, C♯, D, E, F♯, G♯',
                 'A#-Minor':'A♯, B♯, C♯, D♯, E♯, F♯, G♯',
                 'A#-Major':'',
                 'B-Minor':'B, C♯, D, E, F♯, G, A',
                 'B-Major':'B, C♯, D♯, E, F♯, G♯, A♯',
                 }

	return scale_to_note_map[song_key]

def get_chords(key_index, mode):
	c_list = [['C minor chord - C, Eb, G',
		   'D diminished chord - D, F, Ab',
		   'Eb major chord - Eb, G, Bb',
		   'F minor chord - F, Ab, C',
		   'G minor chord - G, Bb, D',
		   'Ab major chord - Ab, C, Eb',
		   'Bb major chord - Bb, D, F'],
		  ['C major chord - C, E, G',
		   'D minor chord - D, F, A',
		   'E minor chord - E, G, B',
		   'F major chord - F, A, C',
		   'G major chord - G, B, D',
		   'A minor chord - A, C, E',
		   'B diminished chord -B, D, F'],
		  ['C minor chord - C, Eb, G',
		   'D diminished chord - D, F, Ab',
		   'Eb major chord - Eb, G, Bb',
		   'F minor chord - F, Ab, C',
		   'G minor chord - G, Bb, D',
		   'Ab major chord - Ab, C, Eb',
		   'Bb major chord - Bb, D, F'],
		  ['C major chord - C, E, G',
		   'D minor chord - D, F, A',
		   'E minor chord - E, G, B',
		   'F major chord - F, A, C',
		   'G major chord - G, B, D',
		   'A minor chord - A, C, E',
		   'B diminished chord - B, D, F'],
		  ['D minor chord - D, F, A',
		  'E diminished chord - E, G, Bb',
		  'F major chord - F, A, C',
		  'G minor chord - G, Bb,D',
		  'A minor chord - A, C, E',
		  'Bb major chord - Bb, D, F',
		  'C major chord - C, E, G'],
		  ['D major chord - D, F#, A',
		   'E minor chord - E, G, B',
		   'F# minor chord - F#, A, C#',
		   'G major chord - G, B, D',
		   'A major chord - A, C#, E',
		   'B minor chord - B, D, F',
		   'C# diminished chord - C#, E, G'],
		  ['F minor chord - F, Ab, C',
          'G diminished chord - G, Bb, Db',
          'Ab major chord - Ab, C, Eb',
          'Bb minor chord - Bb, Db, F',
          'C minor chord - C, Eb, G',
          'Db major chord - Db, F, Ab',
          'Eb major chord - Eb, G, Bb'],
          ['F major chord - F, A, C',
          'G minor chord - G, Bb, D',
          'A minor chord - A, C, E',
          'Bb major chord - Bb, D, F',
          'C major chord - C, E, G',
          'D minor chord - D, F, A',
          'E diminished - E, G,Bb'],
          ['Eb minor chord - Eb, Gb, Bb',
          'F diminished chord - F, Ab, C',
          'Gb major chord - Gb, Bb, D',
          'Ab minor chord - Ab, Cb, Eb',
          'Bb minor chord - Bb, Db, F',
          'Cb major chord - Cb, Eb, Gb',
          'Db major chord - Db, F, Ab'],
          ['Eb major chord - Eb, G, Bb'
          'F minor chord - F, Ab, C'
          'G minor chord - G, Bb, D'
          'Ab major chord - Ab, C, Eb'
          'Bb major chord - Bb, D, F'
          'C minor chord - C, Eb, G'
          'D diminished chord - D, F, Ab'],
          ['E minor chord - E, G, B',
          'F# diminished chord - F#, A, C',
          'G major chord - G, B, D',
          'A minor chord - A, C, E',
          'B minor chord - B, D, F#',
          'C major chord - C, E, G',
          'D major chord - D, F#, A'],
          ['E major chord - E, G#, B',
          'F# minor chord - F#, A, C#',
          'G# minor chord - G#, B, D#',
          'A major chord - A, C#, E',
          'B major chord - B, D#, F#',
          'C# minor chord - C#, E, G#',
          'D# diminished chord - D#, F#, A'],
          ['F minor chord - F, Ab, C',
          'G diminished chord - G, Bb, Db',
          'Ab major chord - Ab, C, Eb',
          'Bb minor chord - Bb, Db, F',
          'C minor chord - C, Eb, G',
          'Db major chord - Db, F, Ab',
          'Eb major chord - Eb, G, Bb'],
          ['F major chord - F, A, C',
          'G minor chord - G, Bb, D',
          'A minor chord - A, C, E',
          'Bb major chord - Bb, D, F',
          'C major chord - C, E, G',
          'D minor chord - D, F, A',
          'E diminished chord - E, G, Bb'],
          ['F# minor chord - F#, A, C#',
          'G# diminished chord - G#, B, D' ,
          'A major chord - A, C#, E',
          'B minor chord - B, D, F#',
          'C# minor chord - C#, E, G#',
          'D major chord - D, F#, A',
          'E major chord - E, G#, B'],
          ['F# major chord - F#, A#, C#',
          'G# minor chord - G#, B, D#',
          'A# minor chord - A#, C#, E#',
          'B major chord - B, D#, F#',
          'C# major chord - C#, E#, G#',
          'D# minor chord - D#, F#, A#',
          'E# diminished chord - E#, G#, B'],
          ['G minor chord - G, Bb, and D',
          'A diminished chord - A, C, and Eb',
          'Bb major chord - Bb, D, and F',
          'C minor chord - C, Eb, and G',
          'D minor chord - D, F, and A',
          'Eb major chord - Eb, G, and Bb',
          'F major chord - F, A, and C'],
          ['G major chord - G, B, D',
          'A minor chord - A, C, E',
          'B minor chord - B, D, F#',
          'C major chord - C, E, G',
          'D major chord - D, F#, A',
          'E minor chord - E, G, B',
          'F# diminished chord - F#, A, C'],
          ['G# minor chord - G#, B, D#',
          'A# diminished chord - A#, C#, E',
          'B major chord - B, D#, F#',
          'C# minor chord - C#, E, G#',
          'D# minor chord - D#, F#, A#',
          'E major chord - E, G#, B',
          'F# major chord - F#, A#, C#'],
          ['G# major chord - G#, B#, D#',
          'A# minor chord - A#, C#, E#',
          'B# minor chord - B#, D#, F##',
          'C# major chord - C#, E#, G#',
          'D# major chord - D#, F##, A#',
          'E# minor chord - E#, G#, B#',
          'F## diminished chord - F##, A#, C#'],
          ['A minor chord - A, C, and E',
          'B diminished chord - B, D, and F',
          'C major chord - C, E, and G',
          'D minor chord - D, F, and A',
          'E minor chord - E, G, and B',
          'F major chord - F, A, and C',
          'G major chord - G, B, and D'],
          ['A major chord - A, C#, and E',
          'B minor chord - B, D, and F#',
          'C# minor chord - C#, E, and G#',
          'D major chord - D, F#, and A',
          'E major chord - E, G#, and B',
          'F# minor chord - F#, A, and C#',
          'G# diminished chord - G#, B, and D'],
          ['A# Minor'],
          ['A# Major'],
          ['B minor chord - B, D, F#',
          'C# diminished chord - C#, E, G',
          'D major chord - D, F#, A',
          'E minor chord - E, G, B',
          'F# minor chord - F#, A, C#',
          'G major chord - G, B, D',
          'A major chord - A, C#, E'],
          ['B major chord - B, D#, F#',
          'C# minor chord - C#, E, G#',
          'D# minor chord - D#, F#, A#',
          'E major chord - E, G#, B',
          'F# major chord - F#, A#, C#',
          'G# minor chord - G#, B, D#',
          'A# diminished chord - A#, C#, E']]
	#scale_to_chord_map = ['C-Minor':'C minor chord - C, Eb, G \nD diminished chord - D, F, Ab \nEb major chord - Eb, G, Bb \nF minor 				chord - F, Ab, C \nG minor chord - G, Bb, D \nAb major chord - Ab, C, Eb \nBb major chord - Bb, D, F']
	return c_list[2 * key_index + mode]

def search(request):
    song_title = request.POST['SongTitle']
    try:
        search_results = song.search(title=song_title)
    except EchoNestAPIError:
        template = loader.get_template('error.html')
        context = RequestContext(request, {'Error_Message' : 'Please enter a song title.'})
        return HttpResponse(template.render(context))
    try:
        search_result_0 = search_results[0]
        # return HttpResponse("You're looking for song %s. Song Tempo is %d" % (song_title, search_result_0.audio_summary['tempo'],))
        template = loader.get_template('melody.html')
	song_key = get_song_key(search_result_0.audio_summary['key'], search_result_0.audio_summary['mode'])
        context = RequestContext(request, { 'Song_Name': search_result_0.title,
                                        'Artist': search_result_0.artist_name,
                                        'Tempo': search_result_0.audio_summary['tempo'],
                                        'Key': song_key,
                                        'Energy': search_result_0.audio_summary['energy'],
                                        'Time_signature': search_result_0.audio_summary['time_signature'],
                                        #'Liveness': search_result_0.audio_summary['liveness'],
                                        #'Acousticness': search_result_0.audio_summary['acousticness'],
                                        #'Analysis_url': search_result_0.audio_summary['analysis_url'],
                                        #'Audio_md5': search_result_0.audio_summary['audio_md5'],
                                        #'Danceability': search_result_0.audio_summary['danceability'],
                                        #'Duration': search_result_0.audio_summary['duration'],
                                        #'Instrumentalness': search_result_0.audio_summary['instrumentalness'],
                                        #'Loudness': search_result_0.audio_summary['loudness'],
                                        #'Mode': search_result_0.audio_summary['mode'],
                                        #'Speechiness': search_result_0.audio_summary['speechiness'],
                                        #'valence': search_result_0.audio_summary['valence'],
					'Scale_Notes': get_notes('C-Minor'),
					'Scale_Chords': get_chords(search_result_0.audio_summary['key'],
					 			   search_result_0.audio_summary['mode']),
					})

        return HttpResponse(template.render(context))
    except IndexError :
        template = loader.get_template('error.html')
        context = RequestContext(request, {'Error_Message' : 'The Song ' + "\"" + song_title + "\"" + ' could not be found. Please enter a new song.'})
        return HttpResponse(template.render(context))
