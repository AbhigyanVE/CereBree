import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
import tkinter as tk
from tkinter import ttk

def display_data(records, show_gui=False):
    """Formats and displays dictionary records in a table."""
    if not records:
        print("No records found.")
        return

    # Extract column names from the first dictionary
    headers = list(records[0].keys())
    # Extract row values
    rows = [list(row.values()) for row in records]

    if not show_gui:
        # Beautiful Terminal Output
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        # Beautiful Pop-up GUI Output
        root = tk.Tk()
        root.title("ITSM Database Viewer")
        root.geometry("1200x400") # Width x Height

        # Create a scrollable table (Treeview)
        tree = ttk.Treeview(root, columns=headers, show="headings")
        
        # Setup columns and headers
        for col in headers:
            tree.heading(col, text=col)
            # Set a default width, adjust as needed
            tree.column(col, width=150, anchor=tk.W)

        # Insert the data rows
        for row in rows:
            # Convert values to strings to prevent tkinter errors with datetime objects
            str_row = [str(item) for item in row]
            tree.insert("", tk.END, values=str_row)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        
        # Pack elements onto the window
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(expand=True, fill=tk.BOTH)

        # Run the UI loop
        root.mainloop()

def test_database_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='cerebree_itsmdb',
            user='root',
            password='admin123'
        )

        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            table_to_query = "incident" 
            
            try:
                print(f"Fetching top 5 records from '{table_to_query}'...\n")
                cursor.execute(f"SELECT * FROM {table_to_query} LIMIT 5;")
                records = cursor.fetchall()
                
                # --- CHANGE THIS FLAG TO TEST TERMINAL VS GUI ---
                # Set to False for Terminal table, True for Pop-up window
                display_data(records, show_gui=True)
                
            except Error as e:
                print(f"Error querying table: {e}")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == '__main__':
    test_database_connection()