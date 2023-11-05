import customtkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import reservation_system.reservation_database as reservation_database

application = customtkinter.CTk()
application.title('Tickets Booking System')
application.geometry('600*600')
application.config(bg='#18161D')
application.resizable(False,False)

font1 = ('Arial', 25,'bold')
font2 = ('Arial', 13,'bold')
font3 = ('Arial', 18,'bold')
