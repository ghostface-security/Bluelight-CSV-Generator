import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

def make_csv():
    try:
        # Get values from the GUI variables
        company_assets = company_value_var.get()
        current_stock_count = current_stock_var.get()
        old_price_per_unit = old_unit_var.get()
        new_price_per_unit = new_unit_var.get()

        # Open a file dialog to ask the user where to save the file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="bluelight_report.csv"
        )
        
        # If the user cancels the dialog, stop the function
        if not file_path:
            return

        # Perform the financial calculations
        stock_cost = current_stock_count * old_price_per_unit
        stock_return = current_stock_count * new_price_per_unit
        year_profit = stock_return - stock_cost
        old_value = company_assets - stock_cost
        new_value = company_assets + year_profit
        quarter_profit = year_profit * 0.25

        # Write the data to the chosen CSV file
        with open(file_path, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            headers = [
                "START-OF-YEAR-VALUE", "OLD-COMPANY-VALUE", "END-OF-YEAR-VALUE",
                "YEARLY-PROFIT", "QUARTERLY-PROFIT", "TOTAL-STOCK-SOLD"
            ]
            writer.writerow(headers)
            data_row = [
                company_assets, old_value, new_value,
                year_profit, quarter_profit, current_stock_count
            ]
            writer.writerow(data_row)

        messagebox.showinfo("Success", f"CSV file '{file_path}' created successfully!")

    except ValueError:
        messagebox.showerror("Error", "Please ensure all financial fields contain valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# --- GUI Setup ---
app = tk.Tk()
app.title("Bluelight Financial Report Generator")
app.geometry('400x350')
app.resizable(False, False)

# Set up the style for a light, professional look
style = ttk.Style(app)
style.theme_use('default')

# Define the new color palette
bg_color = '#f0f0f0'  # Light gray background
fg_color = '#333333'  # Dark gray for text
accent_color = '#007bff' # A clean, professional blue

app.configure(background=bg_color)
style.configure('TFrame', background=bg_color)
style.configure('TLabel', background=bg_color, foreground=fg_color, font=("Segoe UI", 10))
style.configure('Header.TLabel', font=("Segoe UI", 16, "bold"), foreground=accent_color)
style.configure('TEntry', fieldbackground='#ffffff', foreground=fg_color, insertcolor=fg_color)
style.configure('TButton', background=accent_color, foreground='white', font=("Segoe UI", 10, "bold"))
style.map('TButton', background=[('active', '#0056b3')], foreground=[('active', 'white')])

# Set up variables for the input fields
company_value_var = tk.DoubleVar()
current_stock_var = tk.DoubleVar()
old_unit_var = tk.DoubleVar()
new_unit_var = tk.DoubleVar()

main_frame = ttk.Frame(app, padding="20 20 20 20")
main_frame.pack(fill='both', expand=True)

ttk.Label(main_frame, text="Financial Report Generator", style='Header.TLabel').pack(pady=10)

input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=10)

field_labels = ["Assets:", "Stock:", "Price Per Unit:", "Expected Per Unit:"]
variables = [company_value_var, current_stock_var, old_unit_var, new_unit_var]

for i, label_text in enumerate(field_labels):
    label = ttk.Label(input_frame, text=label_text)
    label.grid(column=0, row=i, padx=10, pady=5, sticky='w')
    
    entry = ttk.Entry(input_frame, width=30, textvariable=variables[i])
    entry.grid(column=1, row=i, padx=10, pady=5)

ttk.Button(main_frame, text="Generate Report", command=make_csv).pack(pady=20)

app.mainloop()
