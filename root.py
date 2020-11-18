import pyautogui as pa
import webbrowser as wb
import time

#before running this please complete the setup process of your whatsapp web
wb.open("web.whatsapp.com")

time.sleep(30)

#before 30 secs ends, open the chat window of the person you want to send the text
for i in range(5):
    pa.press("hi")
    pa.press("enter")
