import webcolors
import itertools
import operator
import collections
import math

#def get_colour_from_xkcd_dataset:
#    dataset = 

#Pirated from: https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css21_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[int(math.sqrt((rd + gd + bd)))] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

#https://stackoverflow.com/questions/2249036/grouping-python-tuple-list
#group the same colors
def accumulate(pairs):
    sums = {}
    for pair in pairs:
        sums.setdefault(pair[0], 0)
        sums[pair[0]] += pair[1]
    return sums.items()

def translate_css_21_color(color_name):

    result = ''
    if color_name == 'black':
        result = 'Schwarz'
    if color_name == 'silver':
        result = 'Silber'
    if color_name == 'gray':
        result = 'Grau'
    if color_name == 'navy':
        result = 'Dunkelblau'
    if color_name == 'aqua':
        result = 'Hellblau'
    if color_name == 'blue':
        result = 'Blau'
    if color_name == 'teal':
        result = 'Türkis'
    if color_name == 'purple':
        result = 'Lila'
    if color_name == 'fuchsia':
        result = 'Pink'
    if color_name == 'white':
        result = 'Weiß'
    if color_name == 'lime':
        result = 'Hellgrün'
    if color_name == 'green':
        result = 'Grün'
    if color_name == 'maroon':
        result = 'Braun'
    if color_name == 'red':
        result = 'Rot'
    if color_name == 'orange':
        result = 'Orange'
    if color_name == 'yellow':
        result = 'Gelb'
    if color_name == 'olive':
        result = 'Dunkelgrün'

    return result
