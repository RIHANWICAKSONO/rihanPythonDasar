import PySimpleGUI as sg 

layout = [[sg.button('Klik saya')]]

window = sg.window('Contoh Program PySimpleGUI', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'klik saya':
        print('Tombol diklik')
        
window.close()