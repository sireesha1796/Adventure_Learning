import tkinter as tk
from tkinter import ttk, messagebox
from problem_data import PROBLEMS_DATA

class EducationalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Adventure Learning - Fun Math & Reading!")
        self.root.geometry("1200x800")
        self.root.configure(bg="#E8F4FD")
        
        # Initialize variables
        self.current_level = tk.StringVar(value="Easy")
        self.current_theme = tk.StringVar(value="Sports")
        self.current_skill = tk.StringVar(value="Math")
        self.score = 0
        self.badges = []
        self.current_problem = 0
        self.problems = PROBLEMS_DATA
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create main menu
        self.create_main_menu()
        
    def create_menu_bar(self):
        """Create the menu bar with level and theme options"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Level menu
        level_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="📊 Choose Level", menu=level_menu)
        
        levels = ["Easy", "Medium", "Advanced"]
        for level in levels:
            level_menu.add_radiobutton(
                label=level,
                variable=self.current_level,
                value=level,
                command=self.update_selection_display
            )
        
        # Theme menu
        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="🎨 Choose Theme", menu=theme_menu)
        
        themes = ["Sports", "Music", "Painting", "Swimming", "Adventure"]
        for theme in themes:
            theme_menu.add_radiobutton(
                label=theme,
                variable=self.current_theme,
                value=theme,
                command=self.update_selection_display
            )
        
        # Skill menu
        skill_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="🧠 Choose Skill", menu=skill_menu)
        
        skills = ["Math", "Reading"]
        for skill in skills:
            skill_menu.add_radiobutton(
                label=skill,
                variable=self.current_skill,
                value=skill,
                command=self.update_selection_display
            )
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="❓ Help", menu=help_menu)
        help_menu.add_command(label="How to Play", command=self.show_help)
        help_menu.add_command(label="View Badges", command=self.show_badges)
        
    def update_selection_display(self):
        """Update the selection display when menu items are changed"""
        if hasattr(self, 'selection_label'):
            level = self.current_level.get()
            theme = self.current_theme.get()
            skill = self.current_skill.get()
            self.selection_label.config(
                text=f"📊 Level: {level} | 🎨 Theme: {theme} | 🧠 Skill: {skill}"
            )
        
    def create_main_menu(self):
        """Create the main menu interface"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()
        
        # Create main frame
        main_frame = tk.Frame(self.root, bg="#E8F4FD")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Main title
        title_label = tk.Label(main_frame, text="🎓 Adventure Learning", 
                              font=("Comic Sans MS", 36, "bold"), 
                              fg="#2E86AB", bg="#E8F4FD")
        title_label.pack(pady=20)
        
        subtitle_label = tk.Label(main_frame, text="Fun Math & Reading Adventures!", 
                                 font=("Comic Sans MS", 20), 
                                 fg="#A23B72", bg="#E8F4FD")
        subtitle_label.pack()
        
        # Score display
        score_label = tk.Label(main_frame, text=f"🏆 Total Score: {self.score}", 
                              font=("Comic Sans MS", 18, "bold"), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack(pady=15)
        
        # Badges display
        if self.badges:
            badges_label = tk.Label(main_frame, text=f"🏅 Badges: {', '.join(self.badges)}", 
                                   font=("Comic Sans MS", 16), 
                                   fg="#C73E1D", bg="#E8F4FD")
            badges_label.pack()
        
        # Current selection display
        level = self.current_level.get()
        theme = self.current_theme.get()
        skill = self.current_skill.get()
        
        self.selection_label = tk.Label(main_frame, 
                                       text=f"📊 Level: {level} | 🎨 Theme: {theme} | 🧠 Skill: {skill}",
                                       font=("Comic Sans MS", 16, "bold"), 
                                       fg="#2E86AB", bg="#E8F4FD",
                                       relief="solid", bd=2, padx=20, pady=10)
        self.selection_label.pack(pady=20)
        
        # Instructions
        instructions_label = tk.Label(main_frame, 
                                     text="Use the menu bar above to choose your Level, Theme, and Skill!\nThen click 'Start Adventure' to begin!",
                                     font=("Comic Sans MS", 14), 
                                     fg="#A23B72", bg="#E8F4FD",
                                     wraplength=600, justify="center")
        instructions_label.pack(pady=15)
        
        # Buttons
        start_button = tk.Button(main_frame, text="🚀 Start Adventure!", 
                                command=self.start_adventure,
                                font=("Comic Sans MS", 20, "bold"), 
                                fg="white", bg="#2E86AB", 
                                relief="raised", bd=3, padx=40, pady=15)
        start_button.pack(pady=25)
        
        badges_button = tk.Button(main_frame, text="🏅 View Badges", 
                                 command=self.show_badges,
                                 font=("Comic Sans MS", 18), 
                                 fg="white", bg="#A23B72", 
                                 relief="raised", bd=3, padx=30, pady=12)
        badges_button.pack(pady=15)
        
        help_button = tk.Button(main_frame, text="❓ Help", 
                               command=self.show_help,
                               font=("Comic Sans MS", 18), 
                               fg="white", bg="#F18F01", 
                               relief="raised", bd=3, padx=30, pady=12)
        help_button.pack(pady=15)
    
    def start_adventure(self):
        """Start the learning adventure with selected options"""
        level = self.current_level.get()
        theme = self.current_theme.get()
        skill = self.current_skill.get()
        
        print(f"Starting adventure: {level} level, {theme} theme, {skill} skill")
        
        # Check if problems exist for the selection
        if (level in self.problems and 
            theme in self.problems[level] and 
            skill in self.problems[level][theme]):
            
            self.current_problem = 0
            print(f"Found {len(self.problems[level][theme][skill])} problems")
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
        
        print(f"Showing problem {self.current_problem + 1} of {len(problems)}")
        
        if self.current_problem >= len(problems):
            print("All problems completed, showing results")
            self.show_results()
            return
        
        problem = problems[self.current_problem]
        
        # Clear existing widgets (except menu)
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()
        
        # Create scrollable frame
        canvas = tk.Canvas(self.root, bg="#E8F4FD", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#E8F4FD")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Problem header
        progress_text = f"Problem {self.current_problem + 1} of {len(problems)}"
        progress_label = tk.Label(scrollable_frame, text=progress_text,
                                 font=("Comic Sans MS", 18, "bold"), 
                                 fg="#2E86AB", bg="#E8F4FD")
        progress_label.pack(pady=20)
        
        score_label = tk.Label(scrollable_frame, text=f"Score: {self.score}", 
                              font=("Comic Sans MS", 16), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack()
        
        # Current selection
        selection_label = tk.Label(scrollable_frame, 
                                  text=f"📊 {level} | 🎨 {theme} | 🧠 {skill}",
                                  font=("Comic Sans MS", 14), 
                                  fg="#A23B72", bg="#E8F4FD")
        selection_label.pack(pady=10)
        
        # Story
        story_label = tk.Label(scrollable_frame, text=problem["story"], 
                              font=("Comic Sans MS", 18), 
                              fg="#2E86AB", bg="#E8F4FD", 
                              wraplength=900, justify="left", padx=30, pady=25)
        story_label.pack()
        
        # Question
        question_label = tk.Label(scrollable_frame, text=problem["question"], 
                                 font=("Comic Sans MS", 20, "bold"), 
                                 fg="#A23B72", bg="#E8F4FD", 
                                 wraplength=900, justify="center")
        question_label.pack(pady=25)
        
        # Options
        self.selected_answer = tk.StringVar()
        
        for option in problem["options"]:
            rb = tk.Radiobutton(scrollable_frame, text=option, 
                               variable=self.selected_answer, value=option,
                               font=("Comic Sans MS", 18), 
                               fg="#2E86AB", bg="#E8F4FD", 
                               selectcolor="#F8F9FA", padx=30, pady=12)
            rb.pack(anchor="w")
        
        # Feedback label (will be updated)
        self.feedback_label = tk.Label(scrollable_frame, text="", 
                                      font=("Comic Sans MS", 16, "bold"), 
                                      fg="#2E86AB", bg="#E8F4FD")
        self.feedback_label.pack(pady=15)
        
        # Buttons
        submit_button = tk.Button(scrollable_frame, text="✅ Submit Answer", 
                                 command=self.check_answer,
                                 font=("Comic Sans MS", 18, "bold"), 
                                 fg="white", bg="#2E86AB", 
                                 relief="raised", bd=3, padx=40, pady=15)
        submit_button.pack(pady=15)
        
        next_button = tk.Button(scrollable_frame, text="➡️ Next Problem", 
                               command=self.next_problem,
                               font=("Comic Sans MS", 18), 
                               fg="white", bg="#F18F01", 
                               relief="raised", bd=3, padx=30, pady=12)
        next_button.pack(pady=10)
        
        back_button = tk.Button(scrollable_frame, text="🏠 Back to Menu", 
                               command=self.create_main_menu,
                               font=("Comic Sans MS", 18), 
                               fg="white", bg="#A23B72", 
                               relief="raised", bd=3, padx=30, pady=12)
        back_button.pack(pady=10)
        
        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def check_answer(self):
        """Check if the selected answer is correct"""
        if not self.selected_answer.get():
            self.feedback_label.config(text="❌ Please select an answer!", fg="red")
            return
        
        level = self.current_level.get()
        theme = self.current_theme.get()
        skill = self.current_skill.get()
        problems = self.problems[level][theme][skill]
        problem = problems[self.current_problem]
        
        if self.selected_answer.get() == problem["correct"]:
            self.score += 10
            self.feedback_label.config(text=f"🎉 Correct! +10 points! {problem['explanation']}", fg="green")
            
            # Award badges
            if self.score >= 50 and "Math MVP" not in self.badges and skill == "Math":
                self.badges.append("Math MVP")
                self.feedback_label.config(text=f"🎉 Correct! +10 points! 🏆 New Badge: Math MVP! {problem['explanation']}", fg="green")
            elif self.score >= 50 and "Story Star" not in self.badges and skill == "Reading":
                self.badges.append("Story Star")
                self.feedback_label.config(text=f"🎉 Correct! +10 points! 🏆 New Badge: Story Star! {problem['explanation']}", fg="green")
        else:
            self.feedback_label.config(text=f"❌ Wrong! Correct answer: {problem['correct']}. {problem['explanation']}", fg="red")
    
    def next_problem(self):
        """Move to the next problem"""
        print(f"Moving to next problem. Current: {self.current_problem}")
        self.current_problem += 1
        self.show_problem()
    
    def show_results(self):
        """Show the results after completing all problems"""
        # Clear existing widgets (except menu)
        for widget in self.root.winfo_children():
            if not isinstance(widget, tk.Menu):
                widget.destroy()
        
        # Results
        congrats_label = tk.Label(self.root, text="🎉 Congratulations!", 
                                 font=("Comic Sans MS", 36, "bold"), 
                                 fg="#2E86AB", bg="#E8F4FD")
        congrats_label.pack(pady=50)
        
        score_label = tk.Label(self.root, text=f"Final Score: {self.score} points", 
                              font=("Comic Sans MS", 28, "bold"), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack(pady=25)
        
        if self.badges:
            badges_label = tk.Label(self.root, text=f"Badges Earned: {', '.join(self.badges)}", 
                                   font=("Comic Sans MS", 24), 
                                   fg="#A23B72", bg="#E8F4FD")
            badges_label.pack(pady=25)
        
        # Buttons
        play_again_button = tk.Button(self.root, text="🔄 Play Again", 
                                     command=self.create_main_menu,
                                     font=("Comic Sans MS", 20, "bold"), 
                                     fg="white", bg="#2E86AB", 
                                     relief="raised", bd=3, padx=40, pady=15)
        play_again_button.pack(pady=35)
    
    def show_badges(self):
        """Show all earned badges"""
        badge_window = tk.Toplevel(self.root)
        badge_window.title("🏅 Your Badges")
        badge_window.geometry("500x400")
        badge_window.configure(bg="#E8F4FD")
        
        title_label = tk.Label(badge_window, text="🏅 Your Achievement Badges", 
                              font=("Comic Sans MS", 24, "bold"), 
                              fg="#2E86AB", bg="#E8F4FD")
        title_label.pack(pady=25)
        
        if self.badges:
            for badge in self.badges:
                badge_label = tk.Label(badge_window, text=f"🏆 {badge}", 
                                      font=("Comic Sans MS", 18), 
                                      fg="#F18F01", bg="#E8F4FD")
                badge_label.pack(pady=15)
        else:
            no_badges_label = tk.Label(badge_window, text="No badges earned yet.\nKeep learning to earn badges!", 
                                      font=("Comic Sans MS", 16), 
                                      fg="#A23B72", bg="#E8F4FD")
            no_badges_label.pack(pady=60)
        
        close_button = tk.Button(badge_window, text="Close", 
                                command=badge_window.destroy,
                                font=("Comic Sans MS", 16), 
                                fg="white", bg="#2E86AB", 
                                relief="raised", bd=3, padx=25, pady=8)
        close_button.pack(pady=25)
    
    def show_help(self):
        """Show help information"""
        help_text = """
🎓 Adventure Learning - Help Guide

How to Play:
1. Use the menu bar to choose your Level, Theme, and Skill
2. Click "Start Adventure" to begin
3. Read the fun story and answer the questions
4. Click "Submit Answer" to check your answer
5. Click "Next Problem" to continue
6. Earn points and unlock badges!

Menu Options:
• 📊 Choose Level: Easy, Medium, Advanced
• 🎨 Choose Theme: Sports, Music, Painting, Swimming, Adventure
• 🧠 Choose Skill: Math or Reading
• ❓ Help: View help and badges

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
