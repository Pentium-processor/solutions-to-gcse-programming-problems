import subprocess
from bs4 import BeautifulSoup
import curses
import requests
import blessed
from time import sleep
term=blessed.Terminal()
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
         "Connection":"Keep-Alive"}
r=requests.get("https://www.bbc.co.uk/news/technology",headers=headers)
sleep(5)
with open("headlines.html","w",encoding="UTF-8")as a:
    a.write(str(r.text))

open_html_file=open("headlines.html","r")
headline_parser=BeautifulSoup(open_html_file,"html.parser")
links=[]
url_prefix="https://www.bbc.co.uk/"
headlines=[]
for headline in headline_parser.find_all("span"):
    text=headline.get("aria-hidden")
    if text=="false":
       headlines.append(headline.string.strip())
    else:
       continue
for headline in headline_parser.find_all("a"):
    headline_page=headline.get("href")
    if "/news/articles" in str(headline_page) and str(headline_page).endswith("#comments")==False:
     links.append(url_prefix+str(headline_page))
    else:
      pass

headlines=headlines[:5]
links=links[:5]
n=0
for url  in links:
  n+=1
  url_req=requests.get(url)
  with open(f"{n}_news.html","w") as a:
    a.write(str(url_req.text))
  open_html_file=open(f"{n}_news.html","r")
  news_page_reader=BeautifulSoup(open_html_file,"html.parser")
  with open(f"{n}_news.txt","w") as a:
    for char in news_page_reader.find_all("p"):
        a.write(str(char.string))
'''
def create_curses_application(stdscr):
    curses.start_color()
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_GREEN)
    curses.init_pair(2,curses.COLOR_BLACK,curses.COLOR_WHITE)
    curses.curs_set(0)
    curses.cbreak(True)
    stdscr.keypad(True)
    pos=1
    stdscr.addstr(0,0,"Today\'s Tech News Headlines:",curses.A_BLINK)
    while True:
     for index,headline in enumerate(headlines,start=1):
         if index==pos:
            stdscr.addstr(pos,0,headline,curses.color_pair(1))
         else:
            stdscr.addstr(index,0,headline,curses.color_pair(2))
     detect_key=stdscr.getch()
     if detect_key==ord("q"):
        exit("")
     elif detect_key==curses.KEY_DOWN and pos<6:
         pos+=1
     elif detect_key==curses.KEY_UP and pos>1:
         pos-=1
     elif detect_key==curses.KEY_DOWN and pos==6:
         pos-=5
     elif detect_key==curses.KEY_UP and pos==1:
         pos+=5
'''
def news_headlines_dashboard():
    pos=0
    while True:
     with term.fullscreen(),term.cbreak(),term.hidden_cursor():
       print(term.cyan_underline_bold_dim+"Today\'s Tech News Headlines\n-------------------------------".center(20))
       for index,headline in enumerate(headlines):
        if index==pos:
           term.move_x(term.width//2)
           print(term.reverse_green+term.link(links[pos],headline))
        else:
           term.move_y(index)
           print(term.reverse_white+headline)

       key=term.inkey()
       if key=="q":
        break
       elif key.name=="KEY_DOWN" and pos<5:
           pos+=1
       elif key.name=="KEY_UP" and pos>0:
           pos-=1
       elif key.name=="KEY_UP" and pos==0:
           pos+=5
       elif key.name=="KEY_DOWN" and pos==5:
           pos-=5

if __name__=="__main__":
   news_headlines_dashboard()
