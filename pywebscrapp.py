import requests
from bs4 import BeautifulSoup
import winsound
import PySimpleGUI as sg   


# initialise variables
winsound.Beep(800, 200)
good = 525
bad = 500

winsound.Beep(800, 200)
htp = "https://"
paij = "google.com"
timeout = 30
layout = [[sg.Text('Please enter URL and HTP for web scrapping')],
          [sg.Text('URL', size=(10, 1)), sg.InputText(key='-NAME-')],
          [sg.Text('please input https:// or http:// as a protocol')],
          [sg.Text('bad answers will lead to an error')],
          [sg.Text('HTP', size=(10, 1)), sg.InputText(key='-ADDRESS-')],
          [sg.Button('Submit'), sg.Button('Cancel')]]
winsound.Beep(good, 500)


print("pywebscrapp")
print("----------------------------------------------------------------------------------------------------")
paij = input("type the URL for web scrapping: ")
print("type https:// or http:// for htp protocol")
print("incorect value will result in an error")
htp = input("")
if htp ==  "https://":
      htp = "https://"
elif htp == "http://":
        htp = "http://"
else:
        winsound.Beep(bad, 1000)
        print("Bad value")
        input("")
        quit()







try:
	page = requests.get(htp + paij, timeout=timeout)
except (requests.ConnectionError, requests.Timeout) as exception:
	print("No internet connection, not connected, page doesnt exist, wrong protocol.")
	winsound.Beep(bad, 1000)
	input(" ")
	exit()
winsound.Beep(good, 500)
soup = BeautifulSoup(page.content, 'html.parser')


page_title = soup.title.text


page_body = soup.body


page_head = soup.head

print("scrapped URL: " + paij)
print("https protocol: " + htp)
print("title : " + page_title)
print("----------------------------------------------------------------------------------------------------")
print("head:")
print(page_head)
print("----------------------------------------------------------------------------------------------------")
print("body:")
print(page_body)
input("press any key an then enter or just press enter to continue")
