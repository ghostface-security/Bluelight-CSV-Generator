import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
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
app.title("Bluelight")
app.geometry('300x200')
app.resizable(False, False)

company_value_var = tk.DoubleVar()
current_stock_var = tk.DoubleVar()
old_unit_var = tk.DoubleVar()
new_unit_var = tk.DoubleVar()
file_name_var = tk.StringVar(value="bluelight_report.csv")

ttk.Label(app, text="Assets:").grid(column=0, row=0, padx=10, pady=5, sticky='w')
ttk.Label(app, text="Stock:").grid(column=0, row=1, padx=10, pady=5, sticky='w')
ttk.Label(app, text="Price Per Unit:").grid(column=0, row=2, padx=10, pady=5, sticky='w')
ttk.Label(app, text="Expected Per Unit:").grid(column=0, row=3, padx=10, pady=5, sticky='w')
ttk.Label(app, text="CSV File Name:").grid(column=0, row=4, padx=10, pady=5, sticky='w')

ttk.Entry(app, width=25, textvariable=company_value_var).grid(column=1, row=0, padx=10, pady=5)
ttk.Entry(app, width=25, textvariable=current_stock_var).grid(column=1, row=1, padx=10, pady=5)
ttk.Entry(app, width=25, textvariable=old_unit_var).grid(column=1, row=2, padx=10, pady=5)
ttk.Entry(app, width=25, textvariable=new_unit_var).grid(column=1, row=3, padx=10, pady=5)
ttk.Entry(app, width=25, textvariable=file_name_var).grid(column=1, row=4, padx=10, pady=5)

ttk.Button(app, text="Submit", width=25, command=make_csv).grid(column=0, columnspan=2, row=5, padx=10, pady=10)

app.mainloop()
