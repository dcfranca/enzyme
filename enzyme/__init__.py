# -*- coding: utf-8 -*-
# enzyme - Video metadata parser
#
# Copyright (C) 2011 Antoine Bertin <diaoulael@gmail.com>
# Copyright (C) 2003-2006 Thomas Schueppel <stain@acm.org>
# Copyright (C) 2003-2006 Dirk Meyer <dischi@freevo.org>
#
# Please see the file AUTHORS for a complete list of authors.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MER-
# CHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

import mimetypes
import os
import sys
from exceptions import *

PARSERS = [('video.asf', ['video/asf'], ['asf', 'wmv', 'wma']),
           ('video.flv', ['video/flv'], ['flv']),
           ('mkv', ['video/x-matroska', 'application/mkv'], ['mkv', 'mka', 'webm']),
           ('mp4', ['video/quicktime', 'video/mp4'], ['mov', 'qt', 'mp4', 'mp4a', '3gp', '3gp2', 'mk2']),
           ('mpeg', ['video/mpeg'], ['mpeg', 'mpg', 'mp4', 'ts']),
           ('video.ogm', ['application/ogg'], ['ogm', 'ogg']),
           ('video.real', ['video/real'], ['rm', 'ra', 'ram']),
           ('video.riff', ['video/avi'], ['wav', 'avi'])]


def parse(path):
    if not os.path.isfile(path):
        raise ValueError('Invalid path')
    extension = os.path.splitext(path)[1][1:]
    mimetype = mimetypes.guess_type(path)[0]
    parser_ext = None
    parser_mime = None
    for (parser_name, parser_mimetypes, parser_extensions) in PARSERS:
        if mimetype in parser_mimetypes:
            parser_mime = parser_name
        if extension in parser_extensions:
            parser_ext = parser_name
    parser =  parser_mime or parser_ext
    if not parser:
        raise NoParserError()
    mod = __import__(parser, globals=globals(), locals=locals(), fromlist=[], level=-1)
    with open(path, 'rb') as f:
        p = mod.Parser(f)
    return p
