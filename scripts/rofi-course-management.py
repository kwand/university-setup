#!/usr/bin/python3

from rofi import Rofi
from courses import Courses, Course
from config import TERMINAL_EMULATOR, BROWSER
import subprocess

def open_in_vim(terminal: str, shell: str, file : str) -> None:
    subprocess.Popen([
        terminal,
        '-e', shell, '-i', '-c',
        "vim " + file
    ])

def open_in_browser(browser: str, link: str) -> None:
    subprocess.Popen([browser, link])

def get_options(current : Course) -> dict:
    options = {
        'Open course TeX preamble' : 'preamble',
        'Open TeX snippets': 'snippets', 
        'Go to the course website': 'website',
        'Edit YAML info file': 'yaml',
        'Initialize course directories and files' : 'init'
    }

    if 'markus' in current.info:
        options['Open MarkUs'] = 'markus'
    if 'crowdmark' in current.info:
        options['Open Crowdmark'] = 'crowdmark'

    return options

def course_action(result : str, current : Course) -> None:
    if result == 'preamble': # Open course preamble
        open_in_vim(TERMINAL_EMULATOR, 'fish', f"{str(current.path)}/preamble.tex")

    elif result == 'snippets': # Open snippets
        open_in_vim(TERMINAL_EMULATOR, 'fish', f"{str(current.path)}/UltiSnips/tex.snippets")

    elif result == 'website': # Open course website
        open_in_browser(BROWSER, current.info['url'])

    elif result == 'yaml': # Edit YAML info file
        open_in_vim(TERMINAL_EMULATOR, 'fish', f"{str(current.path)}/info.yaml")

    elif result == 'init': # Initialize course directories
        (current.path / 'figures').mkdir()
        (current.path / 'preamble.tex').touch()
        (current.path / 'UltiSnips').mkdir()
        (current.path / 'tex.snippets').touch()

    elif result == 'markus': # Open MarkUs
        open_in_browser(BROWSER, current.info['markus'])

    elif result == 'crowdmark':
        open_in_browser(BROWSER, current.info['crowdmark'])


# Load current course data
courses = Courses()
current_course = courses.current

options = get_options(current_course)
    
rofi_instance = Rofi(lines=len(options))

index, key = rofi_instance.select(
    current_course.info['short'], list(options)
)

if index >= 0:
    result = options.get(list(options)[index])
    course_action(result, current_course)