import PySimpleGUI as sg


# Define a custom theme resembling darkpurple1 with unchanged disabled button color
custom_theme = {
    'BACKGROUND': '#2E2E2E',
    'TEXT': '#FFFFFF',
    'INPUT': '#D9D9D9',
    'TEXT_INPUT': '#000000',
    'SCROLL': '#000000',
    'BUTTON': ('#FFFFFF', '#2E2E2E'),
    'PROGRESS': ('#01826B', '#D0D0D0'),
    'BORDER': 1,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
    'DISABLED_BUTTON': ('#FFFFFF', '#2E2E2E')  # Keeping disabled button colors unchanged
}

# Set the custom theme
sg.theme_add_new('CustomTheme', custom_theme)
sg.theme('CustomTheme')

# Create a layout with buttons (one of them disabled)
layout = [
    [sg.Button('Normal Button'), sg.Button('Disabled Button', disabled=(True, sg.BUTTON_DISABLED_MEANS_IGNORE))]
]

# Create the window
window = sg.Window('Customized DarkPurple1-like Theme', layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
