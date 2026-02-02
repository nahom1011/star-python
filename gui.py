import customtkinter as ctk
import tkinter as tk
from adv_pass_strength_checker import check_password_strength, generate_strong_password, load_common_passwords
import threading

class PasswordCheckerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Load common passwords in background
        threading.Thread(target=load_common_passwords, daemon=True).start()

        self.title("🛡️ Advanced Password Security Analyzer")
        self.geometry("700x600")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configure Grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Title
        self.title_label = ctk.CTkLabel(self.main_frame, text="Password Security Analyzer", font=ctk.CTkFont(size=24, weight="bold"))
        self.title_label.pack(pady=(20, 10))

        self.subtitle_label = ctk.CTkLabel(self.main_frame, text="Multi-layered entropy and breach analysis", font=ctk.CTkFont(size=14))
        self.subtitle_label.pack(pady=(0, 20))

        # Password Input
        self.input_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.input_frame.pack(fill="x", padx=40, pady=10)

        self.password_entry = ctk.CTkEntry(self.input_frame, placeholder_text="Enter password to analyze...", height=45, show="*")
        self.password_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.password_entry.bind("<KeyRelease>", self.update_analysis)

        self.view_btn = ctk.CTkButton(self.input_frame, text="👁️", width=40, height=45, command=self.toggle_password)
        self.view_btn.pack(side="right")

        # Strength Indicator
        self.strength_bar = ctk.CTkProgressBar(self.main_frame, height=12)
        self.strength_bar.pack(fill="x", padx=40, pady=(20, 5))
        self.strength_bar.set(0)

        self.strength_label = ctk.CTkLabel(self.main_frame, text="Strength: Unknown", font=ctk.CTkFont(weight="bold"))
        self.strength_label.pack()

        # Results Dashboard
        self.results_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.results_frame.pack(fill="both", expand=True, padx=40, pady=20)

        self.create_result_row("Theoretical Entropy:", "0.00 bits", 0)
        self.create_result_row("Shannon Entropy:", "0.00", 1)
        self.create_result_row("Breach Status:", "Checking...", 2)
        self.create_result_row("Length:", "0", 3)

        # Password Generator
        self.gen_frame = ctk.CTkFrame(self.main_frame, height=100)
        self.gen_frame.pack(fill="x", padx=40, pady=(0, 20))
        
        self.gen_btn = ctk.CTkButton(self.gen_frame, text="⚡ Generate Secure Password", command=self.on_generate)
        self.gen_btn.pack(pady=10)

        self.gen_output = ctk.CTkEntry(self.gen_frame, height=35, font=ctk.CTkFont(family="Courier"))
        self.gen_output.pack(fill="x", padx=20, pady=(0, 10))

        self.is_password_visible = False

    def create_result_row(self, label_text, value_text, row):
        label = ctk.CTkLabel(self.results_frame, text=label_text, font=ctk.CTkFont(size=13))
        label.grid(row=row, column=0, padx=20, pady=10, sticky="w")
        
        value = ctk.CTkLabel(self.results_frame, text=value_text, font=ctk.CTkFont(size=13, weight="bold"))
        value.grid(row=row, column=1, padx=20, pady=10, sticky="e")
        
        # Store for update
        if "entropy" in label_text.lower() and "theoretical" in label_text.lower():
            self.theoretical_val = value
        elif "shannon" in label_text.lower():
            self.shannon_val = value
        elif "breach" in label_text.lower():
            self.breach_val = value
        elif "length" in label_text.lower():
            self.length_val = value

    def toggle_password(self):
        if self.is_password_visible:
            self.password_entry.configure(show="*")
            self.view_btn.configure(text="👁️")
        else:
            self.password_entry.configure(show="")
            self.view_btn.configure(text="🙈")
        self.is_password_visible = not self.is_password_visible

    def update_analysis(self, event=None):
        pwd = self.password_entry.get()
        if not pwd:
            self.reset_results()
            return

        results = check_password_strength(pwd)
        
        # Update labels
        self.theoretical_val.configure(text=f"{results['theoretical_entropy']:.2f} bits")
        self.shannon_val.configure(text=f"{results['shannon_entropy']:.2f}")
        self.length_val.configure(text=str(results['length']))
        
        if results['is_compromised']:
            self.breach_val.configure(text="FOUND IN BREACH!", text_color="#FF4B4B")
            self.strength_label.configure(text="Strength: COMPROMISED", text_color="#FF4B4B")
            self.strength_bar.configure(progress_color="#FF4B4B")
            self.strength_bar.set(0.1)
        else:
            self.breach_val.configure(text="NOT FOUND", text_color="#2ECC71")
            
            strength = results['strength']
            if "Weak" in strength:
                color = "#FF4B4B"
                progress = 0.3
            elif "Medium" in strength:
                color = "#F1C40F"
                progress = 0.6
            else:
                color = "#2ECC71"
                progress = 1.0
            
            self.strength_label.configure(text=f"Strength: {strength.upper()}", text_color=color)
            self.strength_bar.configure(progress_color=color)
            self.strength_bar.set(progress)

    def reset_results(self):
        self.theoretical_val.configure(text="0.00 bits")
        self.shannon_val.configure(text="0.00")
        self.breach_val.configure(text="Checking...", text_color="white")
        self.length_val.configure(text="0")
        self.strength_label.configure(text="Strength: Unknown", text_color="white")
        self.strength_bar.set(0)

    def on_generate(self):
        new_pwd = generate_strong_password()
        self.gen_output.delete(0, tk.END)
        self.gen_output.insert(0, new_pwd)
        # Optionally put it in the checker automatically
        # self.password_entry.delete(0, tk.END)
        # self.password_entry.insert(0, new_pwd)
        # self.update_analysis()

if __name__ == "__main__":
    app = PasswordCheckerApp()
    app.mainloop()
