import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random
import os
from PIL import Image, ImageTk
import threading
import time
from problem_data import PROBLEMS_DATA

class EducationalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Adventure Learning - Fun Math & Reading!")
        self.root.geometry("1200x800")  # Increased window size
        self.root.configure(bg="#E8F4FD")
        
        # Make window resizable
        self.root.resizable(True, True)
        
        # Initialize variables
        self.current_level = tk.StringVar(value="Easy")
        self.current_theme = tk.StringVar(value="Sports")
        self.current_skill = tk.StringVar(value="Math")
        self.score = 0
        self.badges = []
        self.current_problem = 0
        self.problems_per_session = 5
        self.consecutive_wrong = 0
        self.voice_enabled = tk.BooleanVar(value=False)
        
        # Load problems data
        self.problems = PROBLEMS_DATA
        
        # Create main menu
        self.create_main_menu()
        
    def create_main_menu(self):
        """Create the main menu interface"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create main frame with better layout
        main_frame = tk.Frame(self.root, bg="#E8F4FD")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Main title with animation effect
        title_frame = tk.Frame(main_frame, bg="#E8F4FD")
        title_frame.pack(pady=20)
        
        title_label = tk.Label(title_frame, text="🎓 Adventure Learning", 
                              font=("Comic Sans MS", 32, "bold"), 
                              fg="#2E86AB", bg="#E8F4FD")
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame, text="Fun Math & Reading Adventures!", 
                                 font=("Comic Sans MS", 18), 
                                 fg="#A23B72", bg="#E8F4FD")
        subtitle_label.pack()
        
        # Score and stats display
        stats_frame = tk.Frame(main_frame, bg="#E8F4FD")
        stats_frame.pack(pady=10)
        
        score_label = tk.Label(stats_frame, text=f"🏆 Total Score: {self.score}", 
                              font=("Comic Sans MS", 16, "bold"), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack()
        
        # Badges display
        if self.badges:
            badges_label = tk.Label(stats_frame, text=f"🏅 Badges: {', '.join(self.badges)}", 
                                   font=("Comic Sans MS", 14), 
                                   fg="#C73E1D", bg="#E8F4FD")
            badges_label.pack()
        
        # Settings frame
        settings_frame = tk.LabelFrame(main_frame, text="⚙️ Settings", 
                                      font=("Comic Sans MS", 16, "bold"), 
                                      fg="#2E86AB", bg="#E8F4FD", bd=3)
        settings_frame.pack(pady=10, fill="x")
        
        # Voice support toggle
        voice_check = tk.Checkbutton(settings_frame, text="🔊 Enable Voice Support (Read Aloud)", 
                                    variable=self.voice_enabled,
                                    font=("Comic Sans MS", 14), 
                                    fg="#2E86AB", bg="#E8F4FD", 
                                    selectcolor="#F8F9FA")
        voice_check.pack(anchor="w", padx=20, pady=5)
        
        # Selection frame
        selection_frame = tk.Frame(main_frame, bg="#E8F4FD")
        selection_frame.pack(pady=20, fill="x")
        
        # Level selection
        level_frame = tk.LabelFrame(selection_frame, text="📊 Choose Your Level", 
                                   font=("Comic Sans MS", 16, "bold"), 
                                   fg="#2E86AB", bg="#E8F4FD", bd=3)
        level_frame.pack(pady=10, fill="x")
        
        levels = ["Easy", "Medium", "Advanced"]
        for level in levels:
            rb = tk.Radiobutton(level_frame, text=level, variable=self.current_level, 
                               value=level, font=("Comic Sans MS", 14), 
                               fg="#2E86AB", bg="#E8F4FD", selectcolor="#F8F9FA")
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Theme selection
        theme_frame = tk.LabelFrame(selection_frame, text="🎨 Choose Your Theme", 
                                   font=("Comic Sans MS", 16, "bold"), 
                                   fg="#A23B72", bg="#E8F4FD", bd=3)
        theme_frame.pack(pady=10, fill="x")
        
        themes = ["Sports", "Music", "Painting", "Swimming", "Adventure"]
        for theme in themes:
            rb = tk.Radiobutton(theme_frame, text=theme, variable=self.current_theme, 
                               value=theme, font=("Comic Sans MS", 14), 
                               fg="#A23B72", bg="#E8F4FD", selectcolor="#F8F9FA")
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Skill selection
        skill_frame = tk.LabelFrame(selection_frame, text="🧠 Choose Your Skill", 
                                   font=("Comic Sans MS", 16, "bold"), 
                                   fg="#F18F01", bg="#E8F4FD", bd=3)
        skill_frame.pack(pady=10, fill="x")
        
        skills = ["Math", "Reading"]
        for skill in skills:
            rb = tk.Radiobutton(skill_frame, text=skill, variable=self.current_skill, 
                               value=skill, font=("Comic Sans MS", 14), 
                               fg="#F18F01", bg="#E8F4FD", selectcolor="#F8F9FA")
            rb.pack(anchor="w", padx=20, pady=5)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="#E8F4FD")
        buttons_frame.pack(pady=30)
        
        start_button = tk.Button(buttons_frame, text="🚀 Start Adventure!", 
                                command=self.start_adventure,
                                font=("Comic Sans MS", 18, "bold"), 
                                fg="white", bg="#2E86AB", 
                                relief="raised", bd=3, padx=30, pady=10)
        start_button.pack(side="left", padx=10)
        
        badges_button = tk.Button(buttons_frame, text="🏅 View Badges", 
                                 command=self.show_badges,
                                 font=("Comic Sans MS", 16), 
                                 fg="white", bg="#A23B72", 
                                 relief="raised", bd=3, padx=20, pady=8)
        badges_button.pack(side="left", padx=10)
        
        help_button = tk.Button(buttons_frame, text="❓ Help", 
                               command=self.show_help,
                               font=("Comic Sans MS", 16), 
                               fg="white", bg="#F18F01", 
                               relief="raised", bd=3, padx=20, pady=8)
        help_button.pack(side="left", padx=10)
        
        # Progress indicator
        if self.score > 0:
            progress_frame = tk.Frame(main_frame, bg="#E8F4FD")
            progress_frame.pack(pady=20)
            
            progress_text = f"📈 Learning Progress: {self.score} points earned!"
            progress_label = tk.Label(progress_frame, text=progress_text,
                                     font=("Comic Sans MS", 14, "bold"),
                                     fg="#2E86AB", bg="#E8F4FD")
            progress_label.pack()
        
        # Ensure window is properly sized
        self.root.update_idletasks()
        self.root.minsize(1000, 600)
    
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
            self.consecutive_wrong = 0
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
        
        # Create main frame for problem display
        main_frame = tk.Frame(self.root, bg="#E8F4FD")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Problem header with progress bar
        header_frame = tk.Frame(main_frame, bg="#E8F4FD")
        header_frame.pack(pady=20, fill="x")
        
        progress_text = f"Problem {self.current_problem + 1} of {len(problems)}"
        progress_label = tk.Label(header_frame, text=progress_text,
                                 font=("Comic Sans MS", 16, "bold"), 
                                 fg="#2E86AB", bg="#E8F4FD")
        progress_label.pack()
        
        # Progress bar
        progress_bar = ttk.Progressbar(header_frame, length=400, mode='determinate')
        progress_bar['value'] = (self.current_problem / len(problems)) * 100
        progress_bar.pack(pady=5)
        
        score_label = tk.Label(header_frame, text=f"Score: {self.score}", 
                              font=("Comic Sans MS", 14), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack()
        
        # Story frame with enhanced styling
        story_frame = tk.Frame(main_frame, bg="#F8F9FA", relief="raised", bd=3)
        story_frame.pack(pady=20, fill="both", expand=True)
        
        story_label = tk.Label(story_frame, text=problem["story"], 
                              font=("Comic Sans MS", 16), 
                              fg="#2E86AB", bg="#F8F9FA", 
                              wraplength=800, justify="left", padx=20, pady=20)
        story_label.pack()
        
        # Voice read button if enabled
        if self.voice_enabled.get():
            voice_button = tk.Button(story_frame, text="🔊 Read Story Aloud", 
                                    command=lambda: self.read_aloud(problem["story"]),
                                    font=("Comic Sans MS", 12), 
                                    fg="white", bg="#A23B72", 
                                    relief="raised", bd=2, padx=15, pady=5)
            voice_button.pack(pady=10)
        
        # Question frame
        question_frame = tk.Frame(main_frame, bg="#E8F4FD")
        question_frame.pack(pady=20, fill="x")
        
        question_label = tk.Label(question_frame, text=problem["question"], 
                                 font=("Comic Sans MS", 18, "bold"), 
                                 fg="#A23B72", bg="#E8F4FD", 
                                 wraplength=800, justify="center")
        question_label.pack()
        
        # Options frame with better styling
        options_frame = tk.Frame(main_frame, bg="#E8F4FD")
        options_frame.pack(pady=20, fill="x")
        
        self.selected_answer = tk.StringVar()
        
        for i, option in enumerate(problem["options"]):
            option_frame = tk.Frame(options_frame, bg="#E8F4FD", relief="solid", bd=1)
            option_frame.pack(fill="x", pady=5)
            
            rb = tk.Radiobutton(option_frame, text=option, 
                               variable=self.selected_answer, value=option,
                               font=("Comic Sans MS", 16), 
                               fg="#2E86AB", bg="#E8F4FD", 
                               selectcolor="#F8F9FA", padx=20, pady=10)
            rb.pack(anchor="w")
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg="#E8F4FD")
        buttons_frame.pack(pady=30)
        
        submit_button = tk.Button(buttons_frame, text="✅ Submit Answer", 
                                 command=self.check_answer,
                                 font=("Comic Sans MS", 16, "bold"), 
                                 fg="white", bg="#2E86AB", 
                                 relief="raised", bd=3, padx=30, pady=10)
        submit_button.pack(side="left", padx=10)
        
        hint_button = tk.Button(buttons_frame, text="💡 Get Hint", 
                               command=lambda: self.show_hint(problem),
                               font=("Comic Sans MS", 16), 
                               fg="white", bg="#F18F01", 
                               relief="raised", bd=3, padx=20, pady=8)
        hint_button.pack(side="left", padx=10)
        
        back_button = tk.Button(buttons_frame, text="🏠 Back to Menu", 
                               command=self.create_main_menu,
                               font=("Comic Sans MS", 16), 
                               fg="white", bg="#A23B72", 
                               relief="raised", bd=3, padx=20, pady=8)
        back_button.pack(side="left", padx=10)
    
    def read_aloud(self, text):
        """Simulate voice reading (in a real app, this would use text-to-speech)"""
        messagebox.showinfo("🔊 Voice Support", 
                          f"Reading aloud: {text[:100]}...\n\n(In a real app, this would use text-to-speech technology!)")
    
    def check_answer(self):
        """Check if the selected answer is correct with adaptive difficulty"""
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
            self.consecutive_wrong = 0  # Reset wrong streak
            
            # Bonus points for streak
            if self.score % 50 == 0:
                bonus_message = "\n🎉 Bonus: Perfect score milestone!"
                self.score += 5
            else:
                bonus_message = ""
            
            messagebox.showinfo("🎉 Correct!", 
                              f"Great job! You got it right!\n\n{problem['explanation']}\n\n+10 points!{bonus_message}")
            
            # Award badges based on performance
            self.award_badges(skill)
            
        else:
            self.consecutive_wrong += 1
            
            # Adaptive difficulty: offer easier problems after multiple wrong answers
            if self.consecutive_wrong >= 3:
                messagebox.showinfo("💪 Keep Going!", 
                                  f"That's not quite right. The correct answer is: {problem['correct']}\n\n{problem['explanation']}\n\n💡 Tip: Consider trying an easier level next time!")
            else:
                messagebox.showinfo("❌ Try Again!", 
                                  f"That's not quite right. The correct answer is: {problem['correct']}\n\n{problem['explanation']}\n\nKeep trying!")
        
        self.current_problem += 1
        self.show_problem()
    
    def award_badges(self, skill):
        """Award badges based on performance"""
        if self.score >= 50 and "Math MVP" not in self.badges and skill == "Math":
            self.badges.append("Math MVP")
            messagebox.showinfo("🏆 New Badge!", "Congratulations! You earned the 'Math MVP' badge!")
        elif self.score >= 50 and "Story Star" not in self.badges and skill == "Reading":
            self.badges.append("Story Star")
            messagebox.showinfo("🏆 New Badge!", "Congratulations! You earned the 'Story Star' badge!")
        
        if self.score >= 100 and "Learning Champion" not in self.badges:
            self.badges.append("Learning Champion")
            messagebox.showinfo("🏆 New Badge!", "Amazing! You earned the 'Learning Champion' badge!")
        
        if self.score >= 200 and "Master Explorer" not in self.badges:
            self.badges.append("Master Explorer")
            messagebox.showinfo("🏆 New Badge!", "Incredible! You earned the 'Master Explorer' badge!")
    
    def show_hint(self, problem):
        """Show a hint for the current problem"""
        hint_text = f"💡 Hint: {problem['explanation']}"
        messagebox.showinfo("Hint", hint_text)
    
    def show_results(self):
        """Show the results after completing all problems"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Results frame
        results_frame = tk.Frame(self.root, bg="#E8F4FD")
        results_frame.pack(expand=True, fill="both")
        
        # Congratulations message
        congrats_label = tk.Label(results_frame, text="🎉 Congratulations!", 
                                 font=("Comic Sans MS", 32, "bold"), 
                                 fg="#2E86AB", bg="#E8F4FD")
        congrats_label.pack(pady=50)
        
        # Final score
        score_label = tk.Label(results_frame, text=f"Final Score: {self.score} points", 
                              font=("Comic Sans MS", 24, "bold"), 
                              fg="#F18F01", bg="#E8F4FD")
        score_label.pack(pady=20)
        
        # Badges earned
        if self.badges:
            badges_label = tk.Label(results_frame, text=f"Badges Earned: {', '.join(self.badges)}", 
                                   font=("Comic Sans MS", 20), 
                                   fg="#A23B72", bg="#E8F4FD")
            badges_label.pack(pady=20)
        
        # Performance message
        if self.score >= 40:
            performance_text = "🌟 Outstanding! You're a learning superstar!"
        elif self.score >= 30:
            performance_text = "👍 Great job! You're doing really well!"
        else:
            performance_text = "💪 Good effort! Keep practicing and you'll improve!"
        
        performance_label = tk.Label(results_frame, text=performance_text, 
                                    font=("Comic Sans MS", 16), 
                                    fg="#2E86AB", bg="#E8F4FD")
        performance_label.pack(pady=30)
        
        # Learning tips
        tips_frame = tk.Frame(results_frame, bg="#F8F9FA", relief="raised", bd=3)
        tips_frame.pack(pady=20, padx=40, fill="x")
        
        tips_label = tk.Label(tips_frame, text="💡 Learning Tips:\n• Practice regularly to improve your skills\n• Try different themes to stay engaged\n• Use hints when you're stuck\n• Challenge yourself with harder levels!", 
                             font=("Comic Sans MS", 14), 
                             fg="#2E86AB", bg="#F8F9FA", 
                             justify="left", padx=20, pady=15)
        tips_label.pack()
        
        # Buttons
        buttons_frame = tk.Frame(results_frame, bg="#E8F4FD")
        buttons_frame.pack(pady=50)
        
        play_again_button = tk.Button(buttons_frame, text="🔄 Play Again", 
                                     command=self.create_main_menu,
                                     font=("Comic Sans MS", 18, "bold"), 
                                     fg="white", bg="#2E86AB", 
                                     relief="raised", bd=3, padx=30, pady=10)
        play_again_button.pack(side="left", padx=10)
        
        new_theme_button = tk.Button(buttons_frame, text="🎨 Try New Theme", 
                                    command=self.create_main_menu,
                                    font=("Comic Sans MS", 16), 
                                    fg="white", bg="#A23B72", 
                                    relief="raised", bd=3, padx=20, pady=8)
        new_theme_button.pack(side="left", padx=10)
    
    def show_badges(self):
        """Show all earned badges"""
        badge_window = tk.Toplevel(self.root)
        badge_window.title("🏅 Your Badges")
        badge_window.geometry("600x400")
        badge_window.configure(bg="#E8F4FD")
        
        title_label = tk.Label(badge_window, text="🏅 Your Achievement Badges", 
                              font=("Comic Sans MS", 24, "bold"), 
                              fg="#2E86AB", bg="#E8F4FD")
        title_label.pack(pady=20)
        
        if self.badges:
            for badge in self.badges:
                badge_label = tk.Label(badge_window, text=f"🏆 {badge}", 
                                      font=("Comic Sans MS", 18), 
                                      fg="#F18F01", bg="#E8F4FD")
                badge_label.pack(pady=10)
        else:
            no_badges_label = tk.Label(badge_window, text="No badges earned yet.\nKeep learning to earn badges!", 
                                      font=("Comic Sans MS", 16), 
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
• 💡 Get hints when you're stuck
• 🎨 Colorful, child-friendly interface
• 📚 Math and Reading comprehension
• 🔊 Voice support (read-aloud feature)
• 📊 Progress tracking
• 🎯 Adaptive difficulty

Badges You Can Earn:
• Math MVP - For math excellence
• Story Star - For reading comprehension
• Learning Champion - For reaching 100 points
• Master Explorer - For reaching 200 points

Tips:
• Read the story carefully before answering
• Use the hint button if you need help
• Practice regularly to improve your skills
• Try different themes and difficulty levels
• Enable voice support for reading assistance

Have fun learning! 🌟
        """
        
        messagebox.showinfo("Help", help_text)

def main():
    root = tk.Tk()
    app = EducationalApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 