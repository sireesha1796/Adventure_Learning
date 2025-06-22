"""
Problem data for the educational app
Contains story-based problems for Math and Reading across different themes and difficulty levels
"""

PROBLEMS_DATA = {
    "Easy": {
        "Sports": {
            "Math": [
                {
                    "story": "🏀 Emma is at basketball practice! She scored 3 baskets in the first quarter and 2 baskets in the second quarter. How many baskets did she score in total?",
                    "question": "How many baskets did Emma score in total?",
                    "options": ["4", "5", "6", "7"],
                    "correct": "5",
                    "explanation": "3 + 2 = 5 baskets total!"
                },
                {
                    "story": "⚽ Jake's soccer team played 4 games this season. They won 2 games and lost 1 game. How many games ended in a tie?",
                    "question": "How many games ended in a tie?",
                    "options": ["0", "1", "2", "3"],
                    "correct": "1",
                    "explanation": "4 total games - 2 wins - 1 loss = 1 tie!"
                },
                {
                    "story": "🏈 The football team has 24 players. 8 players are on offense, 8 are on defense, and the rest are special teams. How many players are on special teams?",
                    "question": "How many players are on special teams?",
                    "options": ["6", "8", "10", "12"],
                    "correct": "8",
                    "explanation": "24 total - 8 offense - 8 defense = 8 special teams!"
                }
            ],
            "Reading": [
                {
                    "story": "🏈 The big football game was about to begin! Sarah was the team captain and felt nervous but excited. Her team, the Thunder Hawks, had practiced hard all week. The stadium was filled with cheering fans wearing blue and gold colors. Sarah looked at her teammates and smiled - they were ready to play their best!",
                    "question": "What was the name of Sarah's football team?",
                    "options": ["Thunder Hawks", "Blue Eagles", "Gold Lions", "Sarah's Team"],
                    "correct": "Thunder Hawks",
                    "explanation": "The story mentions 'Her team, the Thunder Hawks'"
                },
                {
                    "story": "⚽ Carlos loved playing soccer with his friends. Every Saturday morning, they would meet at the park to practice their skills. Carlos was the fastest runner on the team and could dribble the ball better than anyone else. His coach always said he had 'natural talent' for the sport.",
                    "question": "What day did Carlos and his friends practice soccer?",
                    "options": ["Friday", "Saturday", "Sunday", "Monday"],
                    "correct": "Saturday",
                    "explanation": "The story says 'Every Saturday morning, they would meet at the park'"
                }
            ]
        },
        "Music": {
            "Math": [
                {
                    "story": "🎵 In the school band, there are 12 students playing instruments. 5 students play the flute, 3 play the trumpet, and the rest play the drums. How many students play the drums?",
                    "question": "How many students play the drums?",
                    "options": ["3", "4", "5", "6"],
                    "correct": "4",
                    "explanation": "12 total - 5 flutes - 3 trumpets = 4 drums!"
                },
                {
                    "story": "🎼 The music class has 15 students. They need to share 45 sheet music books equally. How many books will each student get?",
                    "question": "How many books will each student get?",
                    "options": ["2", "3", "4", "5"],
                    "correct": "3",
                    "explanation": "45 books ÷ 15 students = 3 books each!"
                }
            ],
            "Reading": [
                {
                    "story": "🎼 The school orchestra was preparing for their spring concert. Maria practiced her violin every day for 30 minutes. She loved the beautiful sound of classical music and dreamed of becoming a famous musician one day. Her favorite piece was 'Spring Symphony' by Mozart.",
                    "question": "How long did Maria practice her violin each day?",
                    "options": ["15 minutes", "30 minutes", "45 minutes", "60 minutes"],
                    "correct": "30 minutes",
                    "explanation": "The story says 'Maria practiced her violin every day for 30 minutes'"
                },
                {
                    "story": "🎵 The school choir was getting ready for the winter concert. There were 20 singers in the choir, and they were all wearing matching red sweaters. The conductor, Mrs. Johnson, was very excited about their performance of 'Jingle Bells' and 'Silent Night'.",
                    "question": "What color sweaters were the choir members wearing?",
                    "options": ["Blue", "Red", "Green", "White"],
                    "correct": "Red",
                    "explanation": "The story says 'they were all wearing matching red sweaters'"
                }
            ]
        },
        "Painting": {
            "Math": [
                {
                    "story": "🎨 The art class has 20 students. They need to share 60 paintbrushes equally. How many paintbrushes will each student get?",
                    "question": "How many paintbrushes will each student get?",
                    "options": ["2", "3", "4", "5"],
                    "correct": "3",
                    "explanation": "60 paintbrushes ÷ 20 students = 3 paintbrushes each!"
                },
                {
                    "story": "🖼️ Lisa bought 8 tubes of paint for $24. If each tube costs the same amount, how much does one tube of paint cost?",
                    "question": "How much does one tube of paint cost?",
                    "options": ["$2", "$3", "$4", "$5"],
                    "correct": "$3",
                    "explanation": "$24 ÷ 8 tubes = $3 per tube!"
                }
            ],
            "Reading": [
                {
                    "story": "🖼️ Alex loved painting with watercolors. His favorite colors were blue and green because they reminded him of the ocean and trees. Today, he was creating a landscape painting of a mountain scene with a beautiful sunset.",
                    "question": "What were Alex's favorite colors?",
                    "options": ["Red and yellow", "Blue and green", "Purple and pink", "Orange and brown"],
                    "correct": "Blue and green",
                    "explanation": "The story says 'His favorite colors were blue and green'"
                },
                {
                    "story": "🎨 The art museum was hosting a children's painting contest. Emma was nervous but excited to show her painting of a rainbow butterfly. The judges walked around looking at all the colorful artwork created by the young artists.",
                    "question": "What did Emma paint for the contest?",
                    "options": ["A rainbow butterfly", "A sunset", "A mountain", "A flower"],
                    "correct": "A rainbow butterfly",
                    "explanation": "The story says 'Emma was nervous but excited to show her painting of a rainbow butterfly'"
                }
            ]
        },
        "Swimming": {
            "Math": [
                {
                    "story": "🏊 The swimming pool is 25 meters long. If Sarah swims 4 laps, how many meters does she swim in total?",
                    "question": "How many meters does Sarah swim in total?",
                    "options": ["75", "100", "125", "150"],
                    "correct": "100",
                    "explanation": "25 meters × 4 laps = 100 meters total!"
                },
                {
                    "story": "🏊‍♀️ There are 16 kids at swimming lessons. 6 kids are in the beginner group, 5 are in the intermediate group, and the rest are in the advanced group. How many kids are in the advanced group?",
                    "question": "How many kids are in the advanced group?",
                    "options": ["3", "4", "5", "6"],
                    "correct": "5",
                    "explanation": "16 total - 6 beginners - 5 intermediate = 5 advanced!"
                }
            ],
            "Reading": [
                {
                    "story": "🏊‍♀️ The swimming competition was about to begin! Michael was excited to race in the 50-meter freestyle event. He had been practicing every day for months and felt ready to do his best. The pool was filled with cheering spectators.",
                    "question": "What swimming event was Michael competing in?",
                    "options": ["50-meter freestyle", "100-meter backstroke", "200-meter butterfly", "400-meter medley"],
                    "correct": "50-meter freestyle",
                    "explanation": "The story says 'Michael was excited to race in the 50-meter freestyle event'"
                }
            ]
        },
        "Adventure": {
            "Math": [
                {
                    "story": "🏔️ The hiking trail is 12 kilometers long. If the group has already hiked 7 kilometers, how many more kilometers do they need to hike to reach the end?",
                    "question": "How many more kilometers do they need to hike?",
                    "options": ["3", "4", "5", "6"],
                    "correct": "5",
                    "explanation": "12 total - 7 already hiked = 5 kilometers remaining!"
                },
                {
                    "story": "🏕️ The camping trip has 18 people. They need to set up 6 tents equally. How many people will sleep in each tent?",
                    "question": "How many people will sleep in each tent?",
                    "options": ["2", "3", "4", "5"],
                    "correct": "3",
                    "explanation": "18 people ÷ 6 tents = 3 people per tent!"
                }
            ],
            "Reading": [
                {
                    "story": "🏔️ The mountain climbing expedition was challenging but exciting! Sarah and her friends were climbing Mount Adventure, which was 2,000 feet tall. They packed warm clothes, food, and safety equipment for their journey to the summit.",
                    "question": "How tall was Mount Adventure?",
                    "options": ["1,000 feet", "1,500 feet", "2,000 feet", "2,500 feet"],
                    "correct": "2,000 feet",
                    "explanation": "The story says 'Mount Adventure, which was 2,000 feet tall'"
                }
            ]
        }
    },
    "Medium": {
        "Sports": {
            "Math": [
                {
                    "story": "🏀 The basketball team scored 24 points in the first half and 18 points in the second half. If they made 6 three-point shots, how many two-point shots did they make? (Each three-pointer is worth 3 points, each two-pointer is worth 2 points)",
                    "question": "How many two-point shots did the team make?",
                    "options": ["12", "15", "18", "21"],
                    "correct": "15",
                    "explanation": "Total points: 24 + 18 = 42. Three-pointers: 6 × 3 = 18. Remaining points: 42 - 18 = 24. Two-pointers: 24 ÷ 2 = 12"
                },
                {
                    "story": "⚽ A soccer team played 12 games this season. They won 7 games, lost 3 games, and tied 2 games. If they get 3 points for a win, 1 point for a tie, and 0 points for a loss, how many total points did they earn?",
                    "question": "How many total points did the team earn?",
                    "options": ["20", "23", "26", "29"],
                    "correct": "23",
                    "explanation": "Wins: 7 × 3 = 21 points. Ties: 2 × 1 = 2 points. Total: 21 + 2 = 23 points"
                }
            ],
            "Reading": [
                {
                    "story": "⚽ The championship soccer match was intense! Both teams played with incredible skill and determination. The crowd of 15,000 fans cheered loudly as the players ran across the field. In the final minutes, the home team scored a dramatic goal, winning the game 2-1. The stadium erupted in celebration!",
                    "question": "How many fans were at the championship match?",
                    "options": ["10,000", "12,000", "15,000", "20,000"],
                    "correct": "15,000",
                    "explanation": "The story mentions 'The crowd of 15,000 fans'"
                },
                {
                    "story": "🏈 The football championship was the most exciting game of the season! The final score was 28-21, with the winning team scoring 4 touchdowns and 4 extra points. The losing team scored 3 touchdowns but missed one extra point attempt.",
                    "question": "What was the final score of the championship game?",
                    "options": ["24-21", "28-21", "32-21", "28-24"],
                    "correct": "28-21",
                    "explanation": "The story says 'The final score was 28-21'"
                }
            ]
        },
        "Music": {
            "Math": [
                {
                    "story": "🎼 The orchestra has 48 musicians. 1/4 of them play string instruments, 1/3 play wind instruments, and the rest play percussion. How many musicians play percussion instruments?",
                    "question": "How many musicians play percussion instruments?",
                    "options": ["12", "16", "20", "24"],
                    "correct": "20",
                    "explanation": "Strings: 48 ÷ 4 = 12. Winds: 48 ÷ 3 = 16. Percussion: 48 - 12 - 16 = 20"
                }
            ],
            "Reading": [
                {
                    "story": "🎵 The music festival featured performances from over 50 different bands and solo artists. The main stage was set up in the center of the park, surrounded by food vendors and merchandise booths. Thousands of music lovers attended the three-day event, enjoying everything from classical symphonies to rock concerts.",
                    "question": "How many days did the music festival last?",
                    "options": ["1 day", "2 days", "3 days", "4 days"],
                    "correct": "3 days",
                    "explanation": "The story mentions 'the three-day event'"
                }
            ]
        },
        "Painting": {
            "Math": [
                {
                    "story": "🎨 An art gallery has 60 paintings on display. 1/5 of them are landscapes, 1/3 are portraits, and the rest are abstract art. How many abstract paintings are there?",
                    "question": "How many abstract paintings are there?",
                    "options": ["16", "20", "24", "28"],
                    "correct": "28",
                    "explanation": "Landscapes: 60 ÷ 5 = 12. Portraits: 60 ÷ 3 = 20. Abstract: 60 - 12 - 20 = 28"
                }
            ]
        }
    },
    "Advanced": {
        "Sports": {
            "Math": [
                {
                    "story": "🏈 A football team has 45 players. 1/3 of them are quarterbacks, 1/5 are running backs, and the rest are defensive players. How many defensive players are on the team?",
                    "question": "How many defensive players are on the team?",
                    "options": ["15", "18", "21", "24"],
                    "correct": "21",
                    "explanation": "Quarterbacks: 45 ÷ 3 = 15. Running backs: 45 ÷ 5 = 9. Defensive players: 45 - 15 - 9 = 21"
                },
                {
                    "story": "🏀 A basketball player made 12 out of 20 free throw attempts. What percentage of free throws did the player make?",
                    "question": "What percentage of free throws did the player make?",
                    "options": ["50%", "60%", "70%", "80%"],
                    "correct": "60%",
                    "explanation": "12 made ÷ 20 total = 0.6 = 60%"
                }
            ],
            "Reading": [
                {
                    "story": "🏈 The professional football league implemented new safety rules to protect players from concussions. These regulations required teams to limit full-contact practices to once per week and mandated that all players wear approved helmets with advanced padding technology. The changes were made after extensive research showed the long-term effects of repeated head injuries.",
                    "question": "What was the main reason for implementing the new safety rules?",
                    "options": ["To save money", "To protect players from concussions", "To make games shorter", "To increase scoring"],
                    "correct": "To protect players from concussions",
                    "explanation": "The story says 'new safety rules to protect players from concussions'"
                }
            ]
        },
        "Music": {
            "Math": [
                {
                    "story": "🎼 A symphony orchestra has 80 musicians. 30% play string instruments, 25% play wind instruments, 20% play brass instruments, and the rest play percussion. How many musicians play percussion instruments?",
                    "question": "How many musicians play percussion instruments?",
                    "options": ["16", "20", "24", "28"],
                    "correct": "20",
                    "explanation": "Strings: 80 × 0.30 = 24. Winds: 80 × 0.25 = 20. Brass: 80 × 0.20 = 16. Percussion: 80 - 24 - 20 - 16 = 20"
                }
            ]
        }
    }
} 
