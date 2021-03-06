#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Defines autosub's metadata.
"""

_ = str
# For gettext po files

NAME = 'autosub'
VERSION = '0.5.6-alpha'
DESCRIPTION = _('Auto-generate subtitles for video/audio/subtitles file.')
LONG_DESCRIPTION = (
    _('Autosub is an automatic subtitles generating utility. '
      'It can detect speech regions automatically '
      'by using Auditok, split the audio files according to regions '
      'by using ffmpeg, '
      'transcribe speech based on several speech APIs and '
      'translate the subtitles\' text by using py-googletrans.'))
AUTHOR = 'Bing Ling'
AUTHOR_EMAIL = 'binglinggroup@outlook.com'
HOMEPAGE = 'https://github.com/BingLingGroup/autosub'
