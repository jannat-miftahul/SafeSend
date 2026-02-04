import tkinter as Tkinter
from tkinter import *
from tkinter import ttk
import webbrowser
import safesend_core
import tkinter.filedialog as tkFileDialog
import os
from ttkthemes import ThemedTk

HOME_DIR = os.path.expanduser("~")

# Modern Color Palette
BG_COLOR = "#f8fafc"
CARD_BG = "#ffffff"
PRIMARY_COLOR = "#0ea5e9"
TEXT_COLOR = "#0f172a"
TEXT_MUTED = "#64748b"

def openfileEnc():
	filename = tkFileDialog.askopenfilename(initialdir = HOME_DIR,title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileToEncrptyEntryUpdate(filename)

def opendirectoryEnc():
	directory = tkFileDialog.askdirectory(initialdir = HOME_DIR,title = "Select directory")
	destinationFolderEncEntryUpdate(directory)

def openfileDec():
	filename = tkFileDialog.askopenfilename(initialdir = HOME_DIR,title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	fileToDecryptEntryUpdate(filename)	
def opendirectoryDec():
	directory = tkFileDialog.askdirectory(initialdir = HOME_DIR,title = "Select directory")
	destinationFolderDecEntryUpdate(directory)

def sendfilepage():
	webbrowser.open_new(r"http://127.0.0.1:5000/upload-file")

def recievefilepage():
	webbrowser.open_new(r"http://127.0.0.1:5000/file-directory")

def opengithub(event):
	webbrowser.open_new(r"https://github.com/jannat-miftahul/SafeSend")

def openlinkedin(event):
	webbrowser.open_new(r"https://in.linkedin.com/in/miftahuljannatofficial")


def fileToEncrptyEntryUpdate(filename):
	inputEncFileEntry.delete(0,END)
	inputEncFileEntry.insert(0,filename)
def destinationFolderEncEntryUpdate(directory):
	inputEncDirEntry.delete(0,END)
	inputEncDirEntry.insert(0,directory)
def fileToDecryptEntryUpdate(filename):
	outputDecFileEntry.delete(0,END)
	outputDecFileEntry.insert(0,filename)
def destinationFolderDecEntryUpdate(directory):
	outputDecDirEntry.delete(0,END)
	outputDecDirEntry.insert(0,directory)

def encryptor():
	EncryptBTN.config(state="disabled")
	public_key = publicKeyOfRecieverEntry.get()
	private_key = privateKeyOfSenderEntry.get()
	directory = inputEncDirEntry.get()
	filename = inputEncFileEntry.get()
	try:
		safesend_core.encrypt(filename,directory,public_key,private_key)
		status_label_enc.config(text="Encryption Successful!", foreground="green")
	except Exception as e:
		status_label_enc.config(text=f"Error: {str(e)}", foreground="red")
	finally:
		EncryptBTN.config(state="normal")

def decryptor():
	DecryptBTN.config(state="disabled")
	public_key = publicKeyOfSenderEntry.get()
	private_key = privateKeyOfRecieverEntry.get()
	directory = outputDecDirEntry.get()
	filename = outputDecFileEntry.get()
	try:
		safesend_core.decrypt(filename,directory,public_key,private_key)
		status_label_dec.config(text="Decryption Successful!", foreground="green")
	except Exception as e:
		status_label_dec.config(text=f"Error: {str(e)}", foreground="red")
	finally:
		DecryptBTN.config(state="normal")

def main():
	global filename
	global directory
	global inputEncFileEntry, inputEncDirEntry, publicKeyOfRecieverEntry, privateKeyOfSenderEntry, EncryptBTN, status_label_enc
	global outputDecFileEntry, outputDecDirEntry, publicKeyOfSenderEntry, privateKeyOfRecieverEntry, DecryptBTN, status_label_dec

	filename = ""
	directory = ""

	# Use ThemedTk for modern look
	form = ThemedTk(theme="arc")
	form.title('SafeSend - Secure File Transfer')
	form.geometry("900x700")
	form.configure(bg=BG_COLOR)

	# Main Style Configuration
	style = ttk.Style()
	style.configure("TLabel", background=BG_COLOR, foreground=TEXT_COLOR, font=('Segoe UI', 10))
	style.configure("TButton", font=('Segoe UI', 10, 'bold'))
	style.configure("Header.TLabel", font=('Segoe UI', 18, 'bold'), foreground=PRIMARY_COLOR)
	style.configure("SubHeader.TLabel", font=('Segoe UI', 12, 'bold'), foreground=TEXT_MUTED)
	style.configure("Card.TFrame", background=CARD_BG, relief="flat")

	# Main Container
	main_frame = ttk.Frame(form, padding="20")
	main_frame.pack(fill=BOTH, expand=True)

	# Header
	header_frame = ttk.Frame(main_frame)
	header_frame.pack(fill=X, pady=(0, 20))
	ttk.Label(header_frame, text="SafeSend", style="Header.TLabel").pack(side=LEFT)
	
	# Menu Buttons
	menu_frame = ttk.Frame(header_frame)
	menu_frame.pack(side=RIGHT)
	ttk.Button(menu_frame, text="Upload to Cloud", command=sendfilepage).pack(side=LEFT, padx=5)
	ttk.Button(menu_frame, text="Cloud Directory", command=recievefilepage).pack(side=LEFT, padx=5)

	# Notebook for Tabs
	notebook = ttk.Notebook(main_frame)
	notebook.pack(fill=BOTH, expand=True)

	# Encryption Tab
	enc_frame = ttk.Frame(notebook, padding="20")
	notebook.add(enc_frame, text="  Encryption  ")

	ttk.Label(enc_frame, text="Encrypt a File", style="SubHeader.TLabel").grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 20))

	# File Selection
	ttk.Label(enc_frame, text="Select File:").grid(row=1, column=0, sticky="w", pady=5)
	inputEncFileEntry = ttk.Entry(enc_frame, width=50)
	inputEncFileEntry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
	ttk.Button(enc_frame, text="Browse", command=openfileEnc).grid(row=1, column=2, pady=5)

	# Directory Selection
	ttk.Label(enc_frame, text="Save To:").grid(row=2, column=0, sticky="w", pady=5)
	inputEncDirEntry = ttk.Entry(enc_frame, width=50)
	inputEncDirEntry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
	ttk.Button(enc_frame, text="Browse", command=opendirectoryEnc).grid(row=2, column=2, pady=5)

	# Keys
	ttk.Label(enc_frame, text="Receiver Public Key:").grid(row=3, column=0, sticky="w", pady=5)
	publicKeyOfRecieverEntry = ttk.Entry(enc_frame, width=50)
	publicKeyOfRecieverEntry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

	ttk.Label(enc_frame, text="Your Private Key:").grid(row=4, column=0, sticky="w", pady=5)
	privateKeyOfSenderEntry = ttk.Entry(enc_frame, width=50, show="*")
	privateKeyOfSenderEntry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

	# Action
	EncryptBTN = ttk.Button(enc_frame, text="Encrypt File", command=encryptor)
	EncryptBTN.grid(row=5, column=1, pady=20, sticky="ew")
	
	status_label_enc = ttk.Label(enc_frame, text="", font=('Segoe UI', 9))
	status_label_enc.grid(row=6, column=1)

	# Decryption Tab
	dec_frame = ttk.Frame(notebook, padding="20")
	notebook.add(dec_frame, text="  Decryption  ")

	ttk.Label(dec_frame, text="Decrypt a File", style="SubHeader.TLabel").grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 20))

	# File Selection
	ttk.Label(dec_frame, text="Select File:").grid(row=1, column=0, sticky="w", pady=5)
	outputDecFileEntry = ttk.Entry(dec_frame, width=50)
	outputDecFileEntry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
	ttk.Button(dec_frame, text="Browse", command=openfileDec).grid(row=1, column=2, pady=5)

	# Directory Selection
	ttk.Label(dec_frame, text="Save To:").grid(row=2, column=0, sticky="w", pady=5)
	outputDecDirEntry = ttk.Entry(dec_frame, width=50)
	outputDecDirEntry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
	ttk.Button(dec_frame, text="Browse", command=opendirectoryDec).grid(row=2, column=2, pady=5)

	# Keys
	ttk.Label(dec_frame, text="Sender Public Key:").grid(row=3, column=0, sticky="w", pady=5)
	publicKeyOfSenderEntry = ttk.Entry(dec_frame, width=50)
	publicKeyOfSenderEntry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

	ttk.Label(dec_frame, text="Your Private Key:").grid(row=4, column=0, sticky="w", pady=5)
	privateKeyOfRecieverEntry = ttk.Entry(dec_frame, width=50, show="*")
	privateKeyOfRecieverEntry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

	# Action
	DecryptBTN = ttk.Button(dec_frame, text="Decrypt File", command=decryptor)
	DecryptBTN.grid(row=5, column=1, pady=20, sticky="ew")

	status_label_dec = ttk.Label(dec_frame, text="", font=('Segoe UI', 9))
	status_label_dec.grid(row=6, column=1)

	# About Tab
	about_frame = ttk.Frame(notebook, padding="20")
	notebook.add(about_frame, text="  About  ")

	ttk.Label(about_frame, text="About SafeSend", style="SubHeader.TLabel").pack(pady=(0, 10))
	ttk.Label(about_frame, text="SafeSend enables secure file transfer using Diffie-Hellman Key Exchange.", wraplength=400).pack()
	
	link_frame = ttk.Frame(about_frame)
	link_frame.pack(pady=20)
	
	github_link = ttk.Label(link_frame, text="View on GitHub", foreground="blue", cursor="hand2")
	github_link.pack()
	github_link.bind("<Button-1>", opengithub)

	footer_frame = ttk.Frame(about_frame)
	footer_frame.pack(side=BOTTOM, pady=20)
	ttk.Label(footer_frame, text="Developed by:", font=('Segoe UI', 9, 'bold')).pack()
	
	contributor = ttk.Label(footer_frame, text="Miftahul Jannat", foreground="blue", cursor="hand2", font=('Segoe UI', 10))
	contributor.pack(pady=5)
	contributor.bind("<Button-1>", openlinkedin)

	form.mainloop()

if __name__ == "__main__":
	main()