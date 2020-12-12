import wolframalpha
import PySimpleGUI as sg
import time
import wikipedia
import pyttsx3

app_id = 'ADD API KEY HERE'  # get your own at https://products.wolframalpha.com/api/
client = wolframalpha.Client(app_id)



engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

sg.theme('LightGreen')
layout = [  [sg.Text('Enter your Question: '), sg.InputText()],
            [sg.Button('Ask question'), sg.Button('Cancel')],
            [sg.Button('Submit', visible=False, bind_return_key=True)],
            [sg.ProgressBar(1, orientation='h', size=(20, 20), key='progress')]]

# Create the Window
window = sg.Window('Intelli Chatbot', layout)
progress_bar = window.FindElement('progress')
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    elif event == 'Submit' or event=='Ask question':
        wolframalpha_res = client.query(values[0])
        wiki_res = wikipedia.summary(values[0], sentences=2)
        progress_bar.UpdateBar(0, 5)
        # adding time.sleep(length in Seconds) has been used to Simulate adding your script in between Bar Updates
        time.sleep(.5)

        progress_bar.UpdateBar(1, 5)
        time.sleep(.5)

        progress_bar.UpdateBar(2, 5)
        time.sleep(.5)

        progress_bar.UpdateBar(3, 5)
        time.sleep(.5)

        progress_bar.UpdateBar(4, 5)
        time.sleep(.5)

        progress_bar.UpdateBar(5, 5)
        time.sleep(.5)

        sg.PopupNonBlocking(next(wolframalpha_res.results).text,"Wikipedia Results:",wiki_res)
        engine.say(next(wolframalpha_res.results).text)
        engine.say(wiki_res)
        engine.runAndWait()
        progress_bar.UpdateBar(0, 5)



    # print(next(res.results).text)

window.close()



