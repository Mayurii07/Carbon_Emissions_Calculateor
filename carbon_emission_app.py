import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sqlite3
import pandas as pd
from updated_queries import updated_queries
from carbon_emission_db import setup_database
from data_insertion import DataInsertionFrame
from reports import ReportsFrame

class CarbonEmissionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Carbon Emission Database - SQL Query Tool")
        self.root.geometry("1200x800")
        self.root.minsize(800, 600)
        
        # Set up the database if it doesn't exist
        try:
            self.check_database()
        except Exception as e:
            messagebox.showerror("Database Error", f"Failed to set up database: {str(e)}")
        
        # Create main notebook (tabs)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create query tab
        self.query_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.query_tab, text="Query Database")
        
        # Create data insertion tab
        self.insertion_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.insertion_tab, text="Insert Data")
        
        # Create reports tab
        self.reports_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.reports_tab, text="Carbon Reports")
        
        # Set up query tab
        self.setup_query_tab()
        
        # Set up data insertion tab
        self.setup_insertion_tab()
        
        # Set up reports tab
        self.setup_reports_tab()
        
        # Initialize the query history
        self.query_history = []
        self.history_index = -1
        
        # Add tab change event handler to refresh users when the Reports tab is selected
        self.notebook.bind("<<NotebookTabChanged>>", self.on_tab_change)
        
    def check_database(self):
        """Check if database exists, if not create it"""
        try:
            conn = sqlite3.connect('carbon_emission.db')
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='User_Profile'")
            if not cursor.fetchone():
                conn.close()
                setup_database()
            else:
                conn.close()
        except Exception as e:
            setup_database()
    
    def setup_query_tab(self):
        """Set up the query tab components"""
        # Create the main frames
        self.create_query_frames()
        
        # Create the query section
        self.create_query_section()
        
        # Create the results section
        self.create_results_section()
        
        # Create the predefined queries section
        self.create_predefined_queries_section()
    
    def setup_insertion_tab(self):
        """Set up the data insertion tab"""
        # Create the data insertion frame
        self.insertion_frame = DataInsertionFrame(self.insertion_tab)
        self.insertion_frame.pack(fill=tk.BOTH, expand=True)
    
    def setup_reports_tab(self):
        """Set up the reports tab"""
        # Create the reports frame
        self.reports_frame = ReportsFrame(self.reports_tab)
        self.reports_frame.pack(fill=tk.BOTH, expand=True)
            
    def create_query_frames(self):
        """Create the main application frames for the query tab"""
        # Top frame for query input
        self.query_frame = ttk.LabelFrame(self.query_tab, text="SQL Query")
        self.query_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=5)
        
        # Middle frame for query results
        self.results_frame = ttk.LabelFrame(self.query_tab, text="Query Results")
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Bottom frame for predefined queries
        self.predefined_frame = ttk.LabelFrame(self.query_tab, text="Predefined Queries")
        self.predefined_frame.pack(fill=tk.BOTH, expand=False, padx=10, pady=5)
        
    def create_query_section(self):
        """Create the query input section"""
        # Query text area
        self.query_text = scrolledtext.ScrolledText(self.query_frame, height=6)
        self.query_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Buttons frame
        button_frame = ttk.Frame(self.query_frame)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # Run query button
        run_button = ttk.Button(button_frame, text="Run Query", command=self.run_custom_query)
        run_button.pack(side=tk.LEFT, padx=5)
        
        # Clear button
        clear_button = ttk.Button(button_frame, text="Clear", command=self.clear_query)
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # History navigation buttons
        prev_button = ttk.Button(button_frame, text="Previous Query", command=self.load_previous_query)
        prev_button.pack(side=tk.LEFT, padx=5)
        
        next_button = ttk.Button(button_frame, text="Next Query", command=self.load_next_query)
        next_button.pack(side=tk.LEFT, padx=5)
        
    def create_results_section(self):
        """Create the results display section"""
        # Create a frame for the Treeview
        tree_frame = ttk.Frame(self.results_frame)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbars for the Treeview
        vsb = ttk.Scrollbar(tree_frame, orient="vertical")
        hsb = ttk.Scrollbar(tree_frame, orient="horizontal")
        
        # Results Treeview
        self.results_tree = ttk.Treeview(tree_frame, yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        # Configure scrollbars
        vsb.config(command=self.results_tree.yview)
        hsb.config(command=self.results_tree.xview)
        
        # Place the Treeview and scrollbars
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.results_tree.pack(fill=tk.BOTH, expand=True)
        
        # Status bar for showing query info
        self.status_bar = ttk.Label(self.results_frame, text="Ready", anchor=tk.W)
        self.status_bar.pack(fill=tk.X, padx=5, pady=2)
        
    def create_predefined_queries_section(self):
        """Create the predefined queries section with buttons"""
        # Create a canvas with scrollbar for the buttons
        canvas_frame = ttk.Frame(self.predefined_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Create a canvas
        canvas = tk.Canvas(canvas_frame)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Add buttons for predefined queries
        for i, (name, query) in enumerate(updated_queries.items()):
            button = ttk.Button(
                scrollable_frame, 
                text=name,
                width=25,
                command=lambda q=query, n=name: self.run_predefined_query(q, n)
            )
            button.grid(row=i//4, column=i%4, padx=5, pady=5, sticky="ew")
        
    def run_custom_query(self):
        """Run the custom query from the text input"""
        query = self.query_text.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Empty Query", "Please enter an SQL query to run.")
            return
        
        # Add to history if not already the last query
        if not self.query_history or query != self.query_history[-1]:
            self.query_history.append(query)
            self.history_index = len(self.query_history) - 1
        
        # Run the query
        self.execute_query(query, "Custom Query")
        
    def run_predefined_query(self, query, name):
        """Run a predefined query"""
        # Set the query text in the input area
        self.query_text.delete("1.0", tk.END)
        self.query_text.insert("1.0", query)
        
        # Add to history if not already the last query
        if not self.query_history or query != self.query_history[-1]:
            self.query_history.append(query)
            self.history_index = len(self.query_history) - 1
        
        # Run the query
        self.execute_query(query, name)
        
    def execute_query(self, query, name):
        """Execute the given SQL query and display results"""
        try:
            # Connect to the database
            conn = sqlite3.connect('carbon_emission.db')
            
            # Check if it's a SELECT query
            is_select = query.strip().upper().startswith("SELECT")
            
            if is_select:
                # For SELECT queries, fetch and display results
                df = pd.read_sql_query(query, conn)
                self.display_results(df)
                row_count = len(df)
                col_count = len(df.columns)
                self.status_bar.config(text=f"{name}: {row_count} rows, {col_count} columns")
            else:
                # For other queries (INSERT, UPDATE, DELETE, etc.)
                cursor = conn.cursor()
                cursor.execute(query)
                conn.commit()
                affected_rows = cursor.rowcount
                self.status_bar.config(text=f"{name}: {affected_rows} rows affected")
                self.clear_results()
                messagebox.showinfo("Success", f"Query executed successfully. {affected_rows} rows affected.")
            
            conn.close()
            
        except Exception as e:
            self.status_bar.config(text=f"Error: {str(e)}")
            messagebox.showerror("Query Error", str(e))
            
    def display_results(self, df):
        """Display the results DataFrame in the Treeview"""
        # Clear previous results
        self.clear_results()
        
        # Configure columns
        self.results_tree["columns"] = list(df.columns)
        
        # Format column headings
        self.results_tree.column("#0", width=0, stretch=False)
        for col in df.columns:
            self.results_tree.column(col, anchor=tk.W, width=100)
            self.results_tree.heading(col, text=col, anchor=tk.W)
        
        # Add data rows
        for i, row in df.iterrows():
            values = [row[col] for col in df.columns]
            self.results_tree.insert("", tk.END, text=str(i), values=values)
            
    def clear_results(self):
        """Clear the results Treeview"""
        # Delete all items
        for item in self.results_tree.get_children():
            self.results_tree.delete(item)
            
        # Reset columns
        self.results_tree["columns"] = []
        
    def clear_query(self):
        """Clear the query text area"""
        self.query_text.delete("1.0", tk.END)
        
    def load_previous_query(self):
        """Load the previous query from history"""
        if not self.query_history:
            return
            
        if self.history_index > 0:
            self.history_index -= 1
            query = self.query_history[self.history_index]
            self.query_text.delete("1.0", tk.END)
            self.query_text.insert("1.0", query)
            
    def load_next_query(self):
        """Load the next query from history"""
        if not self.query_history:
            return
            
        if self.history_index < len(self.query_history) - 1:
            self.history_index += 1
            query = self.query_history[self.history_index]
            self.query_text.delete("1.0", tk.END)
            self.query_text.insert("1.0", query)

    def on_tab_change(self, event):
        """Handle tab change events"""
        # Get the currently selected tab
        current_tab = self.notebook.select()
        current_tab_index = self.notebook.index(current_tab)
        
        # If the Reports tab is selected, refresh the user list
        if current_tab_index == 2:  # Index 2 is the Reports tab
            if hasattr(self, 'reports_frame') and hasattr(self.reports_frame, 'refresh_users'):
                self.reports_frame.refresh_users()

if __name__ == "__main__":
    # Create main window
    root = tk.Tk()
    app = CarbonEmissionApp(root)
    root.mainloop() 