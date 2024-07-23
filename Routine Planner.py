import tkinter as tk
from tkinter import messagebox
import datetime

class DailyRoutinePlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daily Routine Planner for Single Parents")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")  # Light grey background

        # Define colors
        self.primary_color = "#4CAF50"  # Green for primary actions
        self.secondary_color = "#2196F3"  # Blue for secondary actions
        self.accent_color = "#FFC107"  # Amber for highlights
        self.error_color = "#F44336"  # Red for error messages

        self.current_frame = None
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(pady=20, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Login", font=("Arial", 24), bg="#f0f0f0", fg=self.primary_color).pack(pady=10)

        tk.Label(frame, text="Email:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.email_entry = tk.Entry(frame, width=30)
        self.email_entry.pack(padx=10, pady=5)

        tk.Label(frame, text="Password:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.password_entry = tk.Entry(frame, show='*', width=30)
        self.password_entry.pack(padx=10, pady=5)

        tk.Button(frame, text="Login", command=self.show_main_dashboard, bg=self.primary_color, fg="white").pack(pady=10)
        tk.Button(frame, text="Register", command=self.show_registration_screen, bg=self.secondary_color, fg="white").pack(pady=10)

    def show_registration_screen(self):
        self.clear_screen()
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(pady=20, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Register", font=("Arial", 24), bg="#f0f0f0", fg=self.primary_color).pack(pady=10)

        tk.Label(frame, text="Name:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.name_entry = tk.Entry(frame, width=30)
        self.name_entry.pack(padx=10, pady=5)

        tk.Label(frame, text="Email:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.email_entry = tk.Entry(frame, width=30)
        self.email_entry.pack(padx=10, pady=5)

        tk.Label(frame, text="Password:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.password_entry = tk.Entry(frame, show='*', width=30)
        self.password_entry.pack(padx=10, pady=5)

        tk.Button(frame, text="Register", command=self.show_main_dashboard, bg=self.primary_color, fg="white").pack(pady=10)

    def show_main_dashboard(self):
        self.clear_screen()
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(pady=20, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Today's Schedule", font=("Arial", 24), bg="#f0f0f0", fg=self.primary_color).pack(pady=10)

        self.task_listbox = tk.Listbox(frame, width=50, height=10, bg="white", fg="black", selectbackground=self.primary_color, selectforeground="white")
        self.task_listbox.pack(pady=10)

        tk.Button(frame, text="Add Task", command=self.show_add_task_screen, bg=self.primary_color, fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Edit Task", command=self.show_edit_task_screen, bg=self.secondary_color, fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Delete Task", command=self.delete_task, bg=self.error_color, fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Logout", command=self.show_login_screen, bg=self.error_color, fg="white").pack(side=tk.RIGHT, padx=10)

    def show_add_task_screen(self):
        self.clear_screen()
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(pady=20, fill=tk.BOTH, expand=True)

        tk.Label(frame, text="Add Task", font=("Arial", 24), bg="#f0f0f0", fg=self.primary_color).pack(pady=10)

        tk.Label(frame, text="Task Name:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.task_name_entry = tk.Entry(frame, width=30)
        self.task_name_entry.pack(padx=10, pady=5)

        tk.Label(frame, text="Description:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.task_description_entry = tk.Entry(frame, width=30)
        self.task_description_entry.pack(padx=10, pady=5)

        tk.Label(frame, text="Date and Time:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.task_date_entry = tk.Entry(frame, width=30)
        self.task_date_entry.pack(padx=10, pady=5)

        tk.Label(frame, text="Priority:", bg="#f0f0f0").pack(anchor='w', padx=10, pady=5)
        self.priority_var = tk.StringVar(value="Medium")
        tk.OptionMenu(frame, self.priority_var, "High", "Medium", "Low").pack(padx=10, pady=5)

        tk.Button(frame, text="Save", command=self.save_task, bg=self.primary_color, fg="white").pack(pady=10)

    def show_edit_task_screen(self):
        # This function can be implemented similarly to the add task screen
        pass

    def delete_task(self):
        # This function can be implemented to delete the selected task
        pass

    def save_task(self):
        # Implement save task logic here
        pass

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = DailyRoutinePlannerApp()
    app.mainloop()
