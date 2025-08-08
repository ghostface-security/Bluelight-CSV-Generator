import tkinter as tk
from tkinter import ttk, messagebox
import csv

def make_csv():
    try:
        company_assets = company_value_var.get()
        current_stock_count = current_stock_var.get()
        old_price_per_unit = old_unit_var.get()
        new_price_per_unit = new_unit_var.get()
        csv_file_name = file_name_var.get()

        stock_cost = current_stock_count * old_price_per_unit
        stock_return = current_stock_count * new_price_per_unit
        year_profit = stock_return - stock_cost
        old_value = company_assets - stock_cost
        new_value = company_assets + year_profit
        quarter_profit = year_profit * 0.25

        if not csv_file_name:
            messagebox.showerror("Error", "Please enter a CSV file name.")
            return

        with open(csv_file_name, "w", newline='') as csvfile:
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

        messagebox.showinfo("Success", f"CSV file '{csv_file_name}' created successfully!")

    except ValueError:
        messagebox.showerror("Error", "Please ensure all financial fields contain valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

app = tk.Tk()
app.title("Bluelight Financial Report Generator")
app.geometry('400x350')
app.resizable(False, False)

style = ttk.Style(app)
style.theme_use('clam')

bg_color = '#1e3d59'
fg_color = 'white'
accent_color = 'royal blue'

app.configure(background=bg_color)
style.configure('TFrame', background=bg_color)
style.configure('TLabel', background=bg_color, foreground=fg_color, font=("Helvetica", 10))
style.configure('Header.TLabel', font=("Helvetica", 16, "bold"))
style.configure('TEntry', fieldbackground='#404040', foreground=fg_color, insertcolor=fg_color)
style.configure('TButton', background=accent_color, foreground='white', font=("Helvetica", 10, "bold"))
style.map('TButton', background=[('active', '#5c85d6')], foreground=[('active', 'white')])

company_value_var = tk.DoubleVar()
current_stock_var = tk.DoubleVar()
old_unit_var = tk.DoubleVar()
new_unit_var = tk.DoubleVar()
file_name_var = tk.StringVar(value="bluelight_report.csv")

main_frame = ttk.Frame(app, padding="20 20 20 20")
main_frame.pack(fill='both', expand=True)

ttk.Label(main_frame, text="Financial Report Generator", style='Header.TLabel').pack(pady=10)

input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=10)

field_labels = ["Assets:", "Stock:", "Price Per Unit:", "Expected Per Unit:", "CSV File Name:"]
variables = [company_value_var, current_stock_var, old_unit_var, new_unit_var, file_name_var]

for i, label_text in enumerate(field_labels):
    label = ttk.Label(input_frame, text=label_text)
    label.grid(column=0, row=i, padx=10, pady=5, sticky='w')
    
    entry = ttk.Entry(input_frame, width=30, textvariable=variables[i])
    entry.grid(column=1, row=i, padx=10, pady=5)

ttk.Button(main_frame, text="Generate Report", command=make_csv).pack(pady=20)

app.mainloop()
