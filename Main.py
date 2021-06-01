# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:28:13 2021
Computational Thinking Final Project
Collin Crowder and Olivia Hellwig
"""

from tkinter import *
from PIL import ImageTk, Image
import json
import Utilities as ut

class AllTkinterWidgets:
    def __init__(self, master):
        root.configure(background = 'black')
        root.geometry('1500x1200')
        frame = Frame(master, width=1500, height=1200)
        frame.pack(expand = 0, side = LEFT, anchor = NW)
        
#====================menu creation===============================#        
        self.sidebar = Frame(frame, width = 250)
        self.sidebar.pack(expand = 0, fill = Y, side = LEFT)
        
        self.start = Frame(self.sidebar)
        self.start.pack(expand = 0, fill = X, side = TOP)
        self.bt0 = Button(self.start, text = "Run", bd=5, 
                          bg='#000099', fg='white', command = self.Start)
        self.info = Label(self.start, text = "Please wait 30-45 seconds after clicking \'Start\' for it to load"
                          + "\n Click coin buttons after the names appear")
        self.bt0.pack(expand=0, side = TOP)
        self.info.pack(expand = 0, side = TOP)
        
        self.menu = Frame(self.sidebar)
        self.menu.pack(fill=X, side=LEFT)
        self.coin1 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin1)
        self.coin2 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin2)
        self.coin3 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin3)
        self.coin4 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin4)
        self.coin5 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin5)
        self.coin6 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin6)
        self.coin7 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin7)
        self.coin8 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin8)        
        self.coin9 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin9)
        self.coin10 = Button(self.menu, text = '[...]', width = 50, command=self.OnCoin10)
        self.coin1.pack(side=TOP, fill=X, padx=15)
        self.coin2.pack(side=TOP, fill=X, padx=15)  
        self.coin3.pack(side=TOP, fill=X, padx=15)  
        self.coin4.pack(side=TOP, fill=X, padx=15)  
        self.coin5.pack(side=TOP, fill=X, padx=15)  
        self.coin6.pack(side=TOP, fill=X, padx=15)  
        self.coin7.pack(side=TOP, fill=X, padx=15)  
        self.coin8.pack(side=TOP, fill=X, padx=15)  
        self.coin9.pack(side=TOP, fill=X, padx=15)  
        self.coin10.pack(side=TOP, fill=X, padx=15)          
        
#==================display window=================================#
        self.image = None
        self.t = StringVar()
        self.chart_display = Label(bg='black')
        self.display = Frame(bg='black')
        self.display.pack(fill=X, side=LEFT)       
        self.text_display = Label(self.display, text=self.t.get(), bg='black',
                                  fg='white', font=18, justify=LEFT)
        self.text_display.pack(expand=1, side=TOP, fill=X)
        
    
    def Start(self):
        ut.getCoins()
        ut.getReddit()
        ut.getCoinData(ut.find_mentions())
        ut.Plotter()
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol_list = list(coins.keys())
        for i in range(0,10):
            symbol = symbol_list[i]
            name = coin_info[symbol]['Coin']
            coin_names.append(name)
        self.coin1['text'] = coin_names[0]
        self.coin2['text'] = coin_names[1]
        self.coin3['text'] = coin_names[2]
        self.coin4['text'] = coin_names[3]
        self.coin5['text'] = coin_names[4]
        self.coin6['text'] = coin_names[5]
        self.coin7['text'] = coin_names[6]
        self.coin8['text'] = coin_names[7]
        self.coin9['text'] = coin_names[8]
        self.coin10['text'] = coin_names[9]
        f.close()
   
    def OnCoin1(self):
        try:
            self.image = Image.open('Chart1.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[0]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()
   
    def OnCoin2(self):
        try:
            self.image = Image.open('Chart2.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[1]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin3(self):
        try:
            self.image = Image.open('Chart3.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[2]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()
        
    def OnCoin4(self):
        try:
            self.image = Image.open('Chart4.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[3]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin5(self):
        try:
            self.image = Image.open('Chart5.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[4]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin6(self):
        try:
            self.image = Image.open('Chart6.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[5]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin7(self):
        try:
            self.image = Image.open('Chart7.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[6]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin8(self):
        try:
            self.image = Image.open('Chart8.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[7]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin9(self):
        try:
            self.image = Image.open('Chart9.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[8]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

    def OnCoin10(self):
        try:
            self.image = Image.open('Chart10.PNG')
            resized = self.image.resize((1000, 500),Image.ANTIALIAS)
            test = ImageTk.PhotoImage(resized)
            self.chart_display.configure(image=test)
            self.chart_display.image = test
            self.chart_display.pack(before=self.display) 
        except Exception as e:
            print(e)
        f = open('CoinListing.txt')
        raw = f.read()
        coin_info = json.loads(raw)
        coins = ut.find_mentions()
        symbol = list(coins.keys())[9]
        name = coin_info[symbol]['Coin']
        price = round(float(coin_info[symbol]['Quote']['USD']['price']),2)
        change_24h = round(float(coin_info[symbol]['Quote']['USD']['percent_change_24h']),2)
        vol = round(float(coin_info[symbol]['Quote']['USD']['volume_24h']),0)
        mcap = round(float(coin_info[symbol]['Quote']['USD']['market_cap']),0)
        supply = int(coin_info[symbol]['Supply'])
        info_lines = [f'{name} (${symbol}) - {coins[symbol]} Mentions\n\n',   
                      f'Price:  ${price:,.2f}\n', 
                      f'% Change (24h):  {change_24h:.2f}%\n', 
                      f'24h Volume:  {vol:,.0f}\n', f'Market Capitalization:  ${mcap:,.0f}\n',
                      f'Circulating Supply:  {supply:,.0f} {symbol}\n']
        self.text_display['text'] = "\n".join(info_lines)
        f.close()

            
coin_names = []
symbol_list = []
root = Tk()
all = AllTkinterWidgets(root)
root.title('Computational Thinking - Final Project')
root.pack_propagate(0)
root.mainloop()