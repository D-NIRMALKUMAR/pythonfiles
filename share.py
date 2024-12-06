import tkinter as tk
from tkinter import ttk
import time
import sys
import yfinance as yf

'''def update_time():
    """Update the clock display."""
    current_time = time.strftime('%H:%M:%S')
    label.config(text=current_time)
    root.after(1000, update_time)'''
    
# Function to fetch and update live stock price
def update_time():
    #symbol = stock_entry.get().strip().upper()
    symbol = 'SOUTHBANK'
    if not symbol.endswith(".NS"):
        symbol += ".NS"  # Append NSE suffix for Indian stocks

    try:
        stock = yf.Ticker(symbol)
        price = stock.history(period="1d", interval="1m")['Close'].iloc[-1]
        label.config(text=f"{symbol}: ₹{price:.2f}")
    except Exception as e:
        label.config(text="Error fetching price")
        print(f"Error: {e}")
    
    # Schedule the function to run again after 1 minute
    root.after(500, update_time)


def on_closing():
    """Close the application."""
    root.destroy()
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Taskbar Clock")

# Remove window decorations for a minimal look
root.overrideredirect(True)
root.geometry("200x25")  # Set size to fit taskbar
root.attributes('-topmost', True)  # Keep the window on top

# Add a frame for styling
frame = ttk.Frame(root, padding="5")
frame.pack(fill=tk.BOTH, expand=True)

# Create a label to display the time
label = ttk.Label(frame, font=("Helvetica", 8), anchor="center")
label.pack(fill=tk.BOTH, expand=True)

# Add drag functionality
def start_drag(event):
    root.x = event.x
    root.y = event.y

def on_drag(event):
    x = root.winfo_pointerx() - root.x
    y = root.winfo_pointery() - root.y
    root.geometry(f'+{x}+{y}')

frame.bind('<Button-1>', start_drag)
frame.bind('<B1-Motion>', on_drag)

# Update the clock for the first time
update_time()

# Handle window close
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the application
root.mainloop()
