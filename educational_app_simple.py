import tkinter as tk
from tkinter import ttk, messagebox
from problem_data import PROBLEMS_DATA

class EducationalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Adventure Learning - Fun Math & Reading!")
        self.root.geometry("1000x700")
        self.root.configure(bg="#E8F4FD")
        
        # Initialize variables
        self.current_level = tk.StringVar(value="Easy")
        self.current_theme = tk.StringVar(value="Sports")
        self.current_skill = tk.StringVar(value="Math")
        self.score = 0
        self.badges = []
        self.current_problem = 0
        self.problems = PROBLEMS_DATA
        
        # Create main menu
        self.create_main_menu()
        
    def create_main_menu(self):
        """Create the main menu interface"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main title
        title_label = tk.Label(self.root, text="🎓 Adventure Learning", 
                              font=("Comic Sans MS", 32, "bold"), 
                              fg="#2E86AB", bg="#E8F4FD")
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(self.root, text="Fun Math & Reading Adventures!", 
                                 font=("Comic Sans MS", 18), 
                                 fg="#A23B72", bg="#E8F4FD")
        subtitle_label.pack()
        
        # Score display
        score_label = tk.Label(self.root, text=f"🏆 Total Score: {self.score}", 
                              font=("Comic Sans MS", 16, "bold"), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack(pady=10)
        
        # Badges display
        if self.badges:
            badges_label = tk.Label(self.root, text=f"🏅 Badges: {', '.join(self.badges)}", 
                                   font=("Comic Sans MS", 14), 
                                   fg="#C73E1D", bg="#E8F4FD")
            badges_label.pack()
        
        # Level selection
        level_frame = tk.LabelFrame(self.root, text="📊 Choose Your Level", 
                                   font=("Comic Sans MS", 16, "bold"), 
                                   fg="#2E86AB", bg="#E8F4FD", bd=3)
        level_frame.pack(pady=10, padx=20, fill="x")
        
        levels = ["Easy", "Medium", "Advanced"]
        for level in levels:
            rb = tk.Radiobutton(level_frame, text=level, variable=self.current_level, 
                               value=level, font=("Comic Sans MS", 14), 
                               fg="#2E86AB", bg="#E8F4FD", selectcolor="#F8F9FA")
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Theme selection
        theme_frame = tk.LabelFrame(self.root, text="🎨 Choose Your Theme", 
                                   font=("Comic Sans MS", 16, "bold"), 
                                   fg="#A23B72", bg="#E8F4FD", bd=3)
        theme_frame.pack(pady=10, padx=20, fill="x")
        
        themes = ["Sports", "Music", "Painting", "Swimming", "Adventure"]
        for theme in themes:
            rb = tk.Radiobutton(theme_frame, text=theme, variable=self.current_theme, 
                               value=theme, font=("Comic Sans MS", 14), 
                               fg="#A23B72", bg="#E8F4FD", selectcolor="#F8F9FA")
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Skill selection
        skill_frame = tk.LabelFrame(self.root, text="🧠 Choose Your Skill", 
                                   font=("Comic Sans MS", 16, "bold"), 
                                   fg="#F18F01", bg="#E8F4FD", bd=3)
        skill_frame.pack(pady=10, padx=20, fill="x")
        
        skills = ["Math", "Reading"]
        for skill in skills:
            rb = tk.Radiobutton(skill_frame, text=skill, variable=self.current_skill, 
                               value=skill, font=("Comic Sans MS", 14), 
                               fg="#F18F01", bg="#E8F4FD", selectcolor="#F8F9FA")
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Buttons
        start_button = tk.Button(self.root, text="🚀 Start Adventure!", 
                                command=self.start_adventure,
                                font=("Comic Sans MS", 18, "bold"), 
                                fg="white", bg="#2E86AB", 
                                relief="raised", bd=3, padx=30, pady=10)
        start_button.pack(pady=20)
        
        badges_button = tk.Button(self.root, text="🏅 View Badges", 
                                 command=self.show_badges,
                                 font=("Comic Sans MS", 16), 
                                 fg="white", bg="#A23B72", 
                                 relief="raised", bd=3, padx=20, pady=8)
        badges_button.pack(pady=10)
        
        help_button = tk.Button(self.root, text="❓ Help", 
                               command=self.show_help,
                               font=("Comic Sans MS", 16), 
                               fg="white", bg="#F18F01", 
                               relief="raised", bd=3, padx=20, pady=8)
        help_button.pack(pady=10)
    
    def start_adventure(self):
        """Start the learning adventure with selected options"""
        level = self.current_level.get()
        theme = self.current_theme.get()
        skill = self.current_skill.get()
        
        # Check if problems exist for the selection
        if (level in self.problems and 
            theme in self.problems[level] and 
            skill in self.problems[level][theme]):
            
            self.current_problem = 0
            self.show_problem()
        else:
            messagebox.showinfo("Coming Soon!", 
                              f"Problems for {level} level, {theme} theme, and {skill} skill are coming soon!\n\nTry a different combination!")
    
    def show_problem(self):
        """Display the current problem"""
        level = self.current_level.get()
        theme = self.current_theme.get()
        skill = self.current_skill.get()
        
        problems = self.problems[level][theme][skill]
        
        if self.current_problem >= len(problems):
            self.show_results()
            return
        
        problem = problems[self.current_problem]
        
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Problem header
        progress_text = f"Problem {self.current_problem + 1} of {len(problems)}"
        progress_label = tk.Label(self.root, text=progress_text,
                                 font=("Comic Sans MS", 16, "bold"), 
                                 fg="#2E86AB", bg="#E8F4FD")
        progress_label.pack(pady=20)
        
        score_label = tk.Label(self.root, text=f"Score: {self.score}", 
                              font=("Comic Sans MS", 14), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack()
        
        # Story
        story_label = tk.Label(self.root, text=problem["story"], 
                              font=("Comic Sans MS", 16), 
                              fg="#2E86AB", bg="#E8F4FD", 
                              wraplength=800, justify="left", padx=20, pady=20)
        story_label.pack()
        
        # Question
        question_label = tk.Label(self.root, text=problem["question"], 
                                 font=("Comic Sans MS", 18, "bold"), 
                                 fg="#A23B72", bg="#E8F4FD", 
                                 wraplength=800, justify="center")
        question_label.pack(pady=20)
        
        # Options
        self.selected_answer = tk.StringVar()
        
        for option in problem["options"]:
            rb = tk.Radiobutton(self.root, text=option, 
                               variable=self.selected_answer, value=option,
                               font=("Comic Sans MS", 16), 
                               fg="#2E86AB", bg="#E8F4FD", 
                               selectcolor="#F8F9FA", padx=20, pady=10)
            rb.pack(anchor="w")
        
        # Buttons
        submit_button = tk.Button(self.root, text="✅ Submit Answer", 
                                 command=self.check_answer,
                                 font=("Comic Sans MS", 16, "bold"), 
                                 fg="white", bg="#2E86AB", 
                                 relief="raised", bd=3, padx=30, pady=10)
        submit_button.pack(pady=20)
        
        back_button = tk.Button(self.root, text="🏠 Back to Menu", 
                               command=self.create_main_menu,
                               font=("Comic Sans MS", 16), 
                               fg="white", bg="#A23B72", 
                               relief="raised", bd=3, padx=20, pady=8)
        back_button.pack(pady=10)
    
    def check_answer(self):
        """Check if the selected answer is correct"""
        if not self.selected_answer.get():
            messagebox.showwarning("No Answer Selected", "Please select an answer before submitting!")
            return
        
        level = self.current_level.get()
        theme = self.current_theme.get()
        skill = self.current_skill.get()
        problems = self.problems[level][theme][skill]
        problem = problems[self.current_problem]
        
        if self.selected_answer.get() == problem["correct"]:
            self.score += 10
            messagebox.showinfo("🎉 Correct!", 
                              f"Great job! You got it right!\n\n{problem['explanation']}\n\n+10 points!")
            
            # Award badges
            if self.score >= 50 and "Math MVP" not in self.badges and skill == "Math":
                self.badges.append("Math MVP")
                messagebox.showinfo("🏆 New Badge!", "Congratulations! You earned the 'Math MVP' badge!")
            elif self.score >= 50 and "Story Star" not in self.badges and skill == "Reading":
                self.badges.append("Story Star")
                messagebox.showinfo("🏆 New Badge!", "Congratulations! You earned the 'Story Star' badge!")
        else:
            messagebox.showinfo("❌ Try Again!", 
                              f"That's not quite right. The correct answer is: {problem['correct']}\n\n{problem['explanation']}\n\nKeep trying!")
        
        self.current_problem += 1
        self.show_problem()
    
    def show_results(self):
        """Show the results after completing all problems"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Results
        congrats_label = tk.Label(self.root, text="🎉 Congratulations!", 
                                 font=("Comic Sans MS", 32, "bold"), 
                                 fg="#2E86AB", bg="#E8F4FD")
        congrats_label.pack(pady=50)
        
        score_label = tk.Label(self.root, text=f"Final Score: {self.score} points", 
                              font=("Comic Sans MS", 24, "bold"), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack(pady=20)
        
        if self.badges:
            badges_label = tk.Label(self.root, text=f"Badges Earned: {', '.join(self.badges)}", 
                                   font=("Comic Sans MS", 20), 
                                   fg="#A23B72", bg="#E8F4FD")
            badges_label.pack(pady=20)
        
        # Buttons
        play_again_button = tk.Button(self.root, text="🔄 Play Again", 
                                     command=self.create_main_menu,
                                     font=("Comic Sans MS", 18, "bold"), 
                                     fg="white", bg="#2E86AB", 
                                     relief="raised", bd=3, padx=30, pady=10)
        play_again_button.pack(pady=30)
    
    def show_badges(self):
        """Show all earned badges"""
        badge_window = tk.Toplevel(self.root)
        badge_window.title("🏅 Your Badges")
        badge_window.geometry("400x300")
        badge_window.configure(bg="#E8F4FD")
        
        title_label = tk.Label(badge_window, text="🏅 Your Achievement Badges", 
                              font=("Comic Sans MS", 20, "bold"), 
                              fg="#2E86AB", bg="#E8F4FD")
        title_label.pack(pady=20)
        
        if self.badges:
            for badge in self.badges:
                badge_label = tk.Label(badge_window, text=f"🏆 {badge}", 
                                      font=("Comic Sans MS", 16), 
                                      fg="#F18F01", bg="#E8F4FD")
                badge_label.pack(pady=10)
        else:
            no_badges_label = tk.Label(badge_window, text="No badges earned yet.\nKeep learning to earn badges!", 
                                      font=("Comic Sans MS", 14), 
                                      fg="#A23B72", bg="#E8F4FD")
            no_badges_label.pack(pady=50)
        
        close_button = tk.Button(badge_window, text="Close", 
                                command=badge_window.destroy,
                                font=("Comic Sans MS", 14), 
                                fg="white", bg="#2E86AB", 
                                relief="raised", bd=3, padx=20, pady=5)
        close_button.pack(pady=20)
    
    def show_help(self):
        """Show help information"""
        help_text = """
🎓 Adventure Learning - Help Guide

How to Play:
1. Choose your difficulty level (Easy, Medium, Advanced)
2. Select your favorite theme (Sports, Music, Painting, Swimming, Adventure)
3. Pick whether you want to practice Math or Reading
4. Read the fun story and answer the questions
5. Earn points and unlock badges!

Features:
• 🧠 Story-based learning problems
• 🏆 Earn points and badges
• 🎨 Colorful, child-friendly interface
• 📚 Math and Reading comprehension

Badges You Can Earn:
• Math MVP - For math excellence
• Story Star - For reading comprehension

Have fun learning! 🌟
        """
        
        messagebox.showinfo("Help", help_text)

def main():
    root = tk.Tk()
    app = EducationalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
