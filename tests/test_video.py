#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# enzyme - Video metadata parser
# Copyright (C) 2011 Antoine Bertin <diaoulael@gmail.com>
#
# This file is part of enzyme.
#
# enzyme is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# enzyme is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import datetime
import enzyme
import logging
import os
import unittest

# Set up logging
logging.basicConfig()
logging.getLogger('enzyme*').setLevel(logging.DEBUG)

# matroska_test_w1_1 path
matroska_test_path = os.path.abspath(os.path.join('files', 'matroska_test_w1_1'))
mp4_test_path = os.path.abspath('files')


class MKVTestCase(unittest.TestCase):
    tests = ['test_title', 'test_comment', 'test_type_mime_media', 'test_timestamp', 
             'test_datetime', 'test_length', 'test_tags', 'test_video', 'test_audio', 'test_subtitles']

    def setUp(self):
        self.p1 = enzyme.parse(os.path.join(matroska_test_path, u'test1.mkv'))
        self.p2 = enzyme.parse(os.path.join(matroska_test_path, u'test2.mkv'))
        self.p3 = enzyme.parse(os.path.join(matroska_test_path, u'test3.mkv'))
        self.p4 = enzyme.parse(os.path.join(matroska_test_path, u'test4.mkv'))
        self.p5 = enzyme.parse(os.path.join(matroska_test_path, u'test5.mkv'))
        self.p6 = enzyme.parse(os.path.join(matroska_test_path, u'test6.mkv'))
        self.p7 = enzyme.parse(os.path.join(matroska_test_path, u'test7.mkv'))
        self.p8 = enzyme.parse(os.path.join(matroska_test_path, u'test8.mkv'))

    def test_title(self):
        self.assertTrue(self.p1.title == 'Big Buck Bunny - test 1')
        self.assertTrue(self.p2.title == 'Elephant Dream - test 2')
        self.assertTrue(self.p3.title == 'Elephant Dream - test 3')
        #self.assertTrue(self.p4.title is None)
        self.assertTrue(self.p5.title == 'Big Buck Bunny - test 8')
        self.assertTrue(self.p6.title == 'Big Buck Bunny - test 6')
        self.assertTrue(self.p7.title == 'Big Buck Bunny - test 7')
        self.assertTrue(self.p8.title == 'Big Buck Bunny - test 8')

    def test_comment(self):
        self.assertTrue(self.p1.comment == 'Matroska Validation File1, basic MPEG4.2 and MP3 with only SimpleBlock')
        self.assertTrue(self.p2.comment == 'Matroska Validation File 2, 100,000 timecode scale, odd aspect ratio, and CRC-32. Codecs are AVC and AAC')
        self.assertTrue(self.p3.comment == 'Matroska Validation File 3, header stripping on the video track and no SimpleBlock')
        #self.assertTrue(self.p4.comment is None)
        self.assertTrue(self.p5.comment == 'Matroska Validation File 8, secondary audio commentary track, misc subtitle tracks')
        self.assertTrue(self.p6.comment == 'Matroska Validation File 6, random length to code the size of Clusters and Blocks, no Cues for seeking')
        self.assertTrue(self.p7.comment == 'Matroska Validation File 7, junk elements are present at the beggining or end of clusters, the parser should skip it. There is also a damaged element at 451418')
        self.assertTrue(self.p8.comment == 'Matroska Validation File 8, audio missing between timecodes 6.019s and 6.360s')

    def test_type_mime_media(self):
        self.assertTrue(self.p1.type == 'Matroska')
        self.assertTrue(self.p2.type == 'Matroska')
        self.assertTrue(self.p3.type == 'Matroska')
        #self.assertTrue(self.p4.type is None)
        self.assertTrue(self.p5.type == 'Matroska')
        self.assertTrue(self.p6.type == 'Matroska')
        self.assertTrue(self.p7.type == 'Matroska')
        self.assertTrue(self.p8.type == 'Matroska')
        self.assertTrue(self.p1.mime == 'video/x-matroska')
        self.assertTrue(self.p2.mime == 'video/x-matroska')
        self.assertTrue(self.p3.mime == 'video/x-matroska')
        #self.assertTrue(self.p4.mime is None)
        self.assertTrue(self.p5.mime == 'video/x-matroska')
        self.assertTrue(self.p6.mime == 'video/x-matroska')
        self.assertTrue(self.p7.mime == 'video/x-matroska')
        self.assertTrue(self.p8.mime == 'video/x-matroska')
        self.assertTrue(self.p1.media == 'MEDIA_AV')
        self.assertTrue(self.p2.media == 'MEDIA_AV')
        self.assertTrue(self.p3.media == 'MEDIA_AV')
        #self.assertTrue(self.p4.media is None)
        self.assertTrue(self.p5.media == 'MEDIA_AV')
        self.assertTrue(self.p6.media == 'MEDIA_AV')
        self.assertTrue(self.p7.media == 'MEDIA_AV')
        self.assertTrue(self.p8.media == 'MEDIA_AV')

    def test_timestamp(self):
        self.assertTrue(self.p1.timestamp == 1282375383)
        self.assertTrue(self.p2.timestamp == 1307018720)
        self.assertTrue(self.p3.timestamp == 1282427005)
        #self.assertTrue(self.p4.timestamp is None)
        self.assertTrue(self.p5.timestamp == 1282414003)
        self.assertTrue(self.p6.timestamp == 1282408315)
        self.assertTrue(self.p7.timestamp == 1282410023)
        self.assertTrue(self.p8.timestamp == 1282411334)

    def test_datetime(self):
        #TODO: Working?
        self.assertTrue(self.p1.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p2.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p3.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        #self.assertTrue(self.p4.datetime is None)
        self.assertTrue(self.p5.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p6.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p7.datetime == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p8.datetime == datetime.datetime(2010, 1, 1, 0, 0))

    def test_length(self):
        self.assertTrue(self.p1.length == 87.336)
        self.assertTrue(self.p2.length == 47.509)
        self.assertTrue(self.p3.length == 49.064)
        #self.assertTrue(self.p4.length is None)
        self.assertTrue(self.p5.length == 46.665)
        self.assertTrue(self.p6.length == 87.336)
        self.assertTrue(self.p7.length == 37.043)
        self.assertTrue(self.p8.length == 47.341)

    def test_tags(self):
        #TODO: Other properties
        self.assertTrue(self.p1.tags['comment'].value == 'Matroska Validation File1, basic MPEG4.2 and MP3 with only SimpleBlock')
        self.assertTrue(self.p1.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p1.tags['title'].value == 'Big Buck Bunny - test 1')
        self.assertTrue(self.p2.tags['comment'].value == 'Matroska Validation File 2, 100,000 timecode scale, odd aspect ratio, and CRC-32. Codecs are AVC and AAC')
        self.assertTrue(self.p2.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p2.tags['title'].value == 'Elephant Dream - test 2')
        self.assertTrue(self.p3.tags['comment'].value == 'Matroska Validation File 3, header stripping on the video track and no SimpleBlock')
        self.assertTrue(self.p3.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p3.tags['title'].value == 'Elephant Dream - test 3')
        #self.assertTrue(self.p4.tags['comment'].value == '')
        #self.assertTrue(self.p4.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        #self.assertTrue(self.p4.tags['title'].value == '')
        self.assertTrue(self.p5.tags['comment'].value == 'Matroska Validation File 8, secondary audio commentary track, misc subtitle tracks')
        self.assertTrue(self.p5.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p5.tags['title'].value == 'Big Buck Bunny - test 8')
        self.assertTrue(self.p6.tags['comment'].value == 'Matroska Validation File 6, random length to code the size of Clusters and Blocks, no Cues for seeking')
        self.assertTrue(self.p6.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p6.tags['title'].value == 'Big Buck Bunny - test 6')
        self.assertTrue(self.p7.tags['comment'].value == 'Matroska Validation File 7, junk elements are present at the beggining or end of clusters, the parser should skip it. There is also a damaged element at 451418')
        self.assertTrue(self.p7.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p7.tags['title'].value == 'Big Buck Bunny - test 7')
        self.assertTrue(self.p8.tags['comment'].value == 'Matroska Validation File 8, audio missing between timecodes 6.019s and 6.360s')
        self.assertTrue(self.p8.tags['date_released'].value == datetime.datetime(2010, 1, 1, 0, 0))
        self.assertTrue(self.p8.tags['title'].value == 'Big Buck Bunny - test 8')

    def test_video(self):
        self.assertTrue(self.p1.video[0].language == 'und')
        self.assertTrue(self.p1.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p1.video[0].codec == 'MP42')
        self.assertTrue(self.p1.video[0].width == 854)
        self.assertTrue(self.p1.video[0].height == 480)
        self.assertTrue(self.p1.video[0].fps == 24.000000384000003)
        self.assertTrue(self.p1.video[0].trackno == 1)
        self.assertTrue(self.p1.video[0].id == 0)
        
        self.assertTrue(self.p2.video[0].language == 'und')
        self.assertTrue(self.p2.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p2.video[0].codec == 'AVC1')
        self.assertTrue(self.p2.video[0].width == 1024)
        self.assertTrue(self.p2.video[0].height == 576)
        self.assertTrue(self.p2.video[0].fps == 24.000000960000037)
        self.assertTrue(self.p2.video[0].trackno == 1)
        self.assertTrue(self.p2.video[0].id == 0)
        
        self.assertTrue(self.p3.video[0].language == 'und')
        self.assertTrue(self.p3.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p3.video[0].codec == 'AVC1')
        self.assertTrue(self.p3.video[0].width == 1024)
        self.assertTrue(self.p3.video[0].height == 576)
        self.assertTrue(self.p3.video[0].fps == 24.000000960000037)
        self.assertTrue(self.p3.video[0].trackno == 1)
        self.assertTrue(self.p3.video[0].id == 0)
        
        self.assertTrue(self.p5.video[0].language == 'und')
        self.assertTrue(self.p5.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p5.video[0].codec == 'AVC1')
        self.assertTrue(self.p5.video[0].width == 1024)
        self.assertTrue(self.p5.video[0].height == 576)
        self.assertTrue(self.p5.video[0].fps == 24.000000960000037)
        self.assertTrue(self.p5.video[0].aspect == 1.7777777777777777)
        self.assertTrue(self.p5.video[0].trackno == 1)
        self.assertTrue(self.p5.video[0].id == 0)
        
        self.assertTrue(self.p6.video[0].language == 'und')
        self.assertTrue(self.p6.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p6.video[0].codec == 'MP42')
        self.assertTrue(self.p6.video[0].width == 854)
        self.assertTrue(self.p6.video[0].height == 480)
        self.assertTrue(self.p6.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p6.video[0].trackno == 1)
        self.assertTrue(self.p6.video[0].id == 0)
        self.assertTrue(self.p6.video[0].default == False)
        
        self.assertTrue(self.p7.video[0].language == 'und')
        self.assertTrue(self.p7.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p7.video[0].codec == 'AVC1')
        self.assertTrue(self.p7.video[0].width == 1024)
        self.assertTrue(self.p7.video[0].height == 576)
        self.assertTrue(self.p7.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p7.video[0].trackno == 1)
        self.assertTrue(self.p7.video[0].id == 0)
        self.assertTrue(self.p7.video[0].default == False)
        
        self.assertTrue(self.p8.video[0].language == 'und')
        self.assertTrue(self.p8.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p8.video[0].codec == 'AVC1')
        self.assertTrue(self.p8.video[0].width == 1024)
        self.assertTrue(self.p8.video[0].height == 576)
        self.assertTrue(self.p8.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p8.video[0].trackno == 1)
        self.assertTrue(self.p8.video[0].id == 0)
        self.assertTrue(self.p8.video[0].default == False)

    def test_audio(self):
        self.assertTrue(self.p1.audio[0].language == 'und')
        self.assertTrue(self.p1.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p1.audio[0].channels == 2)
        self.assertTrue(self.p1.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p1.audio[0].codec == 85)
        self.assertTrue(self.p1.audio[0].trackno == 2)
        self.assertTrue(self.p1.audio[0].id == 0)
        
        self.assertTrue(self.p2.audio[0].language == 'und')
        self.assertTrue(self.p2.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p2.audio[0].channels == 2)
        self.assertTrue(self.p2.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p2.audio[0].codec == 255)
        self.assertTrue(self.p2.audio[0].trackno == 2)
        self.assertTrue(self.p2.audio[0].id == 0)
        
        self.assertTrue(self.p3.audio[0].language == 'eng')
        self.assertTrue(self.p3.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p3.audio[0].channels == 2)
        self.assertTrue(self.p3.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p3.audio[0].codec == 85)
        self.assertTrue(self.p3.audio[0].trackno == 2)
        self.assertTrue(self.p3.audio[0].id == 0)
        
        self.assertTrue(self.p5.audio[0].language == 'und')
        self.assertTrue(self.p5.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p5.audio[0].channels == 2)
        self.assertTrue(self.p5.audio[0].samplerate == 48000.0)
        self.assertTrue(self.p5.audio[0].codec == 255)
        self.assertTrue(self.p5.audio[0].trackno == 2)
        self.assertTrue(self.p5.audio[0].id == 0)
        self.assertTrue(self.p5.audio[1].language == 'eng')
        self.assertTrue(self.p5.audio[1].title == 'Commentary')
        self.assertTrue(self.p5.audio[1].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p5.audio[1].samplerate == 22050.0)
        self.assertTrue(self.p5.audio[1].codec == 255)
        self.assertTrue(self.p5.audio[1].trackno == 10)
        self.assertTrue(self.p5.audio[1].id == 1)
        
        self.assertTrue(self.p6.video[0].language == 'und')
        self.assertTrue(self.p6.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p6.video[0].codec == 'MP42')
        self.assertTrue(self.p6.video[0].width == 854)
        self.assertTrue(self.p6.video[0].height == 480)
        self.assertTrue(self.p6.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p6.video[0].trackno == 1)
        self.assertTrue(self.p6.video[0].id == 0)
        self.assertTrue(self.p6.video[0].default == False)
        
        self.assertTrue(self.p7.video[0].language == 'und')
        self.assertTrue(self.p7.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p7.video[0].codec == 'AVC1')
        self.assertTrue(self.p7.video[0].width == 1024)
        self.assertTrue(self.p7.video[0].height == 576)
        self.assertTrue(self.p7.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p7.video[0].trackno == 1)
        self.assertTrue(self.p7.video[0].id == 0)
        self.assertTrue(self.p7.video[0].default == False)
        
        self.assertTrue(self.p8.video[0].language == 'und')
        self.assertTrue(self.p8.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p8.video[0].codec == 'AVC1')
        self.assertTrue(self.p8.video[0].width == 1024)
        self.assertTrue(self.p8.video[0].height == 576)
        self.assertTrue(self.p8.video[0].fps == 24.000002112000185)
        self.assertTrue(self.p8.video[0].trackno == 1)
        self.assertTrue(self.p8.video[0].id == 0)
        self.assertTrue(self.p8.video[0].default == False)

    def test_subtitles(self):
        self.assertTrue(len(self.p1.subtitles) == 0)
        self.assertTrue(len(self.p2.subtitles) == 0)
        self.assertTrue(len(self.p3.subtitles) == 0)
        self.assertTrue(self.p5.subtitles[0].language == 'eng')
        self.assertTrue(self.p5.subtitles[0].id == 0)
        self.assertTrue(self.p5.subtitles[0].trackno == 3)
        self.assertTrue(self.p5.subtitles[0].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[1].language == 'hun')
        self.assertTrue(self.p5.subtitles[1].id == 1)
        self.assertTrue(self.p5.subtitles[1].trackno == 4)
        self.assertTrue(self.p5.subtitles[1].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[2].language == 'ger')
        self.assertTrue(self.p5.subtitles[2].id == 2)
        self.assertTrue(self.p5.subtitles[2].trackno == 5)
        self.assertTrue(self.p5.subtitles[2].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[3].language == 'fre')
        self.assertTrue(self.p5.subtitles[3].id == 3)
        self.assertTrue(self.p5.subtitles[3].trackno == 6)
        self.assertTrue(self.p5.subtitles[3].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[4].language == 'spa')
        self.assertTrue(self.p5.subtitles[4].id == 4)
        self.assertTrue(self.p5.subtitles[4].trackno == 8)
        self.assertTrue(self.p5.subtitles[4].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[5].language == 'ita')
        self.assertTrue(self.p5.subtitles[5].id == 5)
        self.assertTrue(self.p5.subtitles[5].trackno == 9)
        self.assertTrue(self.p5.subtitles[5].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[6].language == 'jpn')
        self.assertTrue(self.p5.subtitles[6].id == 6)
        self.assertTrue(self.p5.subtitles[6].trackno == 11)
        self.assertTrue(self.p5.subtitles[6].codec == 'S_TEXT/UTF8')
        self.assertTrue(self.p5.subtitles[7].language == 'und')
        self.assertTrue(self.p5.subtitles[7].id == 7)
        self.assertTrue(self.p5.subtitles[7].trackno == 7)
        self.assertTrue(self.p5.subtitles[7].codec == 'S_TEXT/UTF8')
        self.assertTrue(len(self.p6.subtitles) == 0)
        self.assertTrue(len(self.p7.subtitles) == 0)
        self.assertTrue(len(self.p8.subtitles) == 0)


class MP4TestCase(unittest.TestCase):
    tests = ['test_type_mime_media', 'test_timestamp', 
             'test_length', 'test_video', 'test_audio']

    def setUp(self):
        self.p1 = enzyme.parse(os.path.join(mp4_test_path, u'sample_mpeg4.mp4'))
        self.p2 = enzyme.parse(os.path.join(mp4_test_path, u'Quality Sample.mp4'))
        self.p3 = enzyme.parse(os.path.join(mp4_test_path, u'sample.3gp'))
        self.p4 = enzyme.parse(os.path.join(mp4_test_path, u'sample_3GPP2.3g2'))

    def test_type_mime_media(self):
        self.assertTrue(self.p1.type == 'MPEG-4 Video')
        self.assertTrue(self.p1.mime == 'video/mp4')
        self.assertTrue(self.p1.media == 'MEDIA_AV')
        self.assertTrue(self.p2.type == 'MPEG-4 Video')
        self.assertTrue(self.p2.mime == 'video/mp4')
        self.assertTrue(self.p2.media == 'MEDIA_AV')
        self.assertTrue(self.p3.type == 'MPEG-4 Video')
        self.assertTrue(self.p3.mime == 'video/mp4')
        self.assertTrue(self.p3.media == 'MEDIA_AV')
        self.assertTrue(self.p4.type == 'MPEG-4 Video')
        self.assertTrue(self.p4.mime == 'video/mp4')
        self.assertTrue(self.p4.media == 'MEDIA_AV')

    def test_timestamp(self):
        self.assertTrue(self.p1.timestamp == 1130521606)
        self.assertTrue(self.p2.timestamp == 1278452391)
        self.assertTrue(self.p3.timestamp == 1130521000)
        self.assertTrue(self.p4.timestamp == 1130521775)

    def test_length(self):
        self.assertTrue(self.p1.length == 4)
        self.assertTrue(self.p2.length == 14)
        self.assertTrue(self.p3.length == 5)
        self.assertTrue(self.p4.length == 5)

    def test_video(self):
        self.assertTrue(self.p1.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p1.video[0].codec == 'mp4v')
        self.assertTrue(self.p1.video[0].width == 190)
        self.assertTrue(self.p1.video[0].height == 240)
        self.assertTrue(self.p1.video[0].id == 2)
        self.assertTrue(self.p2.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p2.video[0].codec == 'avc1')
        self.assertTrue(self.p2.video[0].length == 13)
        self.assertTrue(self.p2.video[0].width == 1280)
        self.assertTrue(self.p2.video[0].height == 720)
        self.assertTrue(self.p2.video[0].id == 1)
        self.assertTrue(self.p3.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p3.video[0].codec == 'mp4v')
        self.assertTrue(self.p3.video[0].length == 4)
        self.assertTrue(self.p3.video[0].width == 176)
        self.assertTrue(self.p3.video[0].height == 144)
        self.assertTrue(self.p3.video[0].id == 2)
        self.assertTrue(self.p4.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p4.video[0].codec == 'mp4v')
        self.assertTrue(self.p4.video[0].length == 4)
        self.assertTrue(self.p4.video[0].width == 176)
        self.assertTrue(self.p4.video[0].height == 144)
        self.assertTrue(self.p4.video[0].id == 2)

    def test_audio(self):
        self.assertTrue(self.p1.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p1.audio[0].length == 4)
        self.assertTrue(self.p1.audio[0].codec == "mp4a")
        self.assertTrue(self.p1.audio[0].id == 1)
        self.assertTrue(self.p2.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p2.audio[0].length == 14)
        self.assertTrue(self.p2.audio[0].codec == "mp4a")
        self.assertTrue(self.p2.audio[0].id == 2)
        self.assertTrue(self.p3.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p3.audio[0].length == 5)
        self.assertTrue(self.p3.audio[0].codec == "samr")
        self.assertTrue(self.p3.audio[0].id == 1)
        self.assertTrue(self.p4.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p4.audio[0].length == 5)
        self.assertTrue(self.p4.audio[0].codec == "samr")
        self.assertTrue(self.p4.audio[0].id == 1)


class ASFTestCase(unittest.TestCase):
    tests = ['test_type_mime_media', 'test_copyright', 'test_length', 'test_video', 'test_audio']

    def setUp(self):
        self.p1 = enzyme.parse(os.path.join(mp4_test_path, u'niceday.asf'))

    def test_type_mime_media(self):
        print self.p1
        self.assertTrue(self.p1.type == 'asf format')
        self.assertTrue(self.p1.mime == 'video/x-ms-asf')
        self.assertTrue(self.p1.media == 'MEDIA_AV')

    def test_copyright(self):
        self.assertTrue(self.p1.copyright == 'Fx Sound and Magic')

    def test_length(self):
        self.assertTrue(self.p1.length == 54.814)

    def test_video(self):
        self.assertTrue(self.p1.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p1.video[0].language == 'en-us')
        self.assertTrue(self.p1.video[0].bitrate == 250000)
        self.assertTrue(self.p1.video[0].codec == 'WMV3')
        self.assertTrue(self.p1.video[0].width == 320)
        self.assertTrue(self.p1.video[0].height == 240)
        self.assertTrue(self.p1.video[0].fps == 29.97000002997)
        self.assertTrue(self.p1.video[0].id == 2)

    def test_audio(self):
        self.assertTrue(self.p1.audio[0].language == 'en-us')
        self.assertTrue(self.p1.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p1.audio[0].channels == 2)
        self.assertTrue(self.p1.audio[0].samplerate == 44100)
        self.assertTrue(self.p1.audio[0].codec == 353)
        self.assertTrue(self.p1.audio[0].samplebits == 16)
        self.assertTrue(self.p1.audio[0].bitrate == 64040)
        self.assertTrue(self.p1.audio[0].id == 1)


class FLVTestCase(unittest.TestCase):
    tests = ['test_type_mime_media', 'test_length', 'test_video', 'test_audio']

    def setUp(self):
        self.p1 = enzyme.parse(os.path.join(mp4_test_path, u'20051210-w50s.flv'))

    def test_type_mime_media(self):
        print self.p1
        self.assertTrue(self.p1.type == 'Flash Video')
        self.assertTrue(self.p1.mime == 'video/flv')
        self.assertTrue(self.p1.media == 'MEDIA_AV')

    def test_length(self):
        self.assertTrue(self.p1.length == 16.92)

    def test_video(self):
        self.assertTrue(self.p1.video[0].media == 'MEDIA_VIDEO')
        self.assertTrue(self.p1.video[0].codec == 'VP60')

    def test_audio(self):
        self.assertTrue(self.p1.audio[0].media == 'MEDIA_AUDIO')
        self.assertTrue(self.p1.audio[0].channels == 2)
        self.assertTrue(self.p1.audio[0].samplerate == 22050)
        self.assertTrue(self.p1.audio[0].codec == 85)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(map(MKVTestCase, MKVTestCase.tests))
    suite.addTests(map(MP4TestCase, MP4TestCase.tests))
    suite.addTests(map(ASFTestCase, ASFTestCase.tests))
    suite.addTests(map(FLVTestCase, FLVTestCase.tests))
    unittest.TextTestRunner(verbosity=2).run(suite)
