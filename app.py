import tkinter as tk
import pyautogui as autog

# class for creating stickers
class Sticker:

	@staticmethod
	def get_prod_list():
		return ["Memtest", "Wiped Drive", "Install OS", "Update OS", "Install Drivers", "Test Peripherals", "Test USBs", "Test Webcam", "Test Audio", "Activate OS", "Clean/Stickers"]

	def __init__(self, master_frame):
		self.frame = tk.Frame(master=master_frame)
		
		self.name = tk.Entry(master=self.frame)
		
		self.notes = tk.Entry(master=self.frame)
		
		self.chk_array, self.chk_array_val = [], []
		for item in self.get_prod_list():
			self.chk_array_val.append(tk.IntVar())
			self.chk_array.append(tk.Checkbutton(master=self.frame, text=item, variable=self.chk_array_val[-1], onvalue=1, offvalue=0))
			
	def setup_grid(self, r, c):
		self.frame.grid(row=r, column=c)
		self.name.grid()
		self.notes.grid()
		for item in self.chk_array:
			item.grid()

# Get screen sizes for ratios
width, height = autog.size()
width = height * (16/9)

# Default Window Setup
window = tk.Tk()
window.title('Laptop Station Manager')
window.geometry(f'{int(width*0.75)}x{int(height*0.9)}+{int(width*0.125)}+{int(height*0.1)}')

# Main frame setup
frame_main = tk.Frame(master=window, borderwidth=1)
frame_main.pack()

# Create subframes for each spot in the grid
frame_stickers = []
for i in range(3):
	for j in range(6):
		frame_main.columnconfigure(j, minsize=200)
		frame_main.rowconfigure(i, minsize=200)
		frame_stickers.append(Sticker(frame_main))
		frame_stickers[-1].setup_grid(i, j)


window.mainloop()
