#!/usr/bin/python3

from rofi import Rofi
from courses import Courses
from config import TERMINAL_EMULATOR, BROWSER
import subprocess

def open_in_vim(terminal: str, shell: str, file : str):
    subprocess.Popen([
        terminal,
        '-e', shell, '-i', '-c',
        "vim " + file
    ])

    return 

def open_in_browser(browser: str, link: str):
    subprocess.Popen([browser, link])


# Load current course data
courses = Courses()
current = courses.current

options = [
    'Open course TeX preamble',
    'Open TeX snippets', 
    'Go to the course website',
    'Edit YAML info file',
    'Initialize course directories and files'
]

if 'markus' in current.info:
    options.append('Open MarkUs')

rofi_instance = Rofi(lines=len(options))

index, key = rofi_instance.select(
    current.info['short'], options
)

if index == 0: # Open course preamble
    open_in_vim(TERMINAL_EMULATOR, 'fish', f"{str(current.path)}/preamble.tex")

elif index == 1: # Open snippets
    open_in_vim(TERMINAL_EMULATOR, 'fish', f"{str(current.path)}/UltiSnips/tex.snippets")

elif index == 2: # Open course website
    open_in_browser(BROWSER, current.info['url'])

elif index == 3: # Edit YAML info file
    open_in_vim(TERMINAL_EMULATOR, 'fish', f"{str(current.path)}/info.yaml")

elif index == 4: # Initialize course directories
    (current.path / 'figures').mkdir()
    (current.path / 'preamble.tex').touch()
    (current.path / 'UltiSnips').mkdir()
    (current.path / 'tex.snippets').touch()

elif index == 5: # Open MarkUs
    open_in_browser(BROWSER, current.info['markus'])