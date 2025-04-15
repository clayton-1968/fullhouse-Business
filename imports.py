import subprocess
from funcoes import *

from db.db_conector import MySqlDatabase


from datetime import *
from datetime import datetime
from PIL import ImageTk, Image
import io

from tktooltip import ToolTip
from tkinter import StringVar, OptionMenu, font, messagebox, ttk, PhotoImage
from tkinter import *
from tkinter import Toplevel



from ttkwidgets.autocomplete import *

from markupsafe import escape

from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session, jsonify
from flask_login import login_user, logout_user, login_required

from customtkinter import *

import tkinter as tk  # Importação do tkinter para o anchor
# import ttkthemes
# from ttkthemes import ThemedStyle

import base64
import customtkinter
import webbrowser
import os
from collections import defaultdict
import re
import hashlib
import smtplib
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
