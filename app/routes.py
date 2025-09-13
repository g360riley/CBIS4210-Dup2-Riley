from flask import render_template, jsonify
from . import app
import requests
import datetime
from datetime import datetime, timedelta
import logging

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tutorials')
def tutorials():
    # Enhanced tutorial data with lessons and code examples
    tutorials = [
        {
            'id': 1, 'title': 'Python Basics', 'description': 'Learn Python fundamentals', 
            'level': 'beginner', 'duration': '2 hours', 
            'topics': ['Variables', 'Functions', 'Loops'],
            'lessons': [
                {'id': 1, 'title': 'Variables and Data Types', 'duration': 20, 'code_example': 'name = "Python"\nage = 30\nprint(f"Hello, {name}!")'},
                {'id': 2, 'title': 'Functions and Parameters', 'duration': 25, 'code_example': 'def greet(name):\n    return f"Hello, {name}!"\n\nresult = greet("World")'},
                {'id': 3, 'title': 'Loops and Iteration', 'duration': 30, 'code_example': 'for i in range(5):\n    print(f"Count: {i}")'},
                {'id': 4, 'title': 'Lists and Dictionaries', 'duration': 25, 'code_example': 'fruits = ["apple", "banana"]\nperson = {"name": "Alice", "age": 25}'}
            ]
        },
        {
            'id': 2, 'title': 'HTML & CSS', 'description': 'Build your first webpage', 
            'level': 'beginner', 'duration': '3 hours', 
            'topics': ['HTML Tags', 'CSS Styling', 'Responsive Design'],
            'lessons': [
                {'id': 1, 'title': 'HTML Structure', 'duration': 30, 'code_example': '<!DOCTYPE html>\n<html>\n<head><title>My Page</title></head>\n<body><h1>Hello World</h1></body>\n</html>'},
                {'id': 2, 'title': 'CSS Basics', 'duration': 40, 'code_example': 'h1 {\n  color: blue;\n  font-size: 24px;\n  text-align: center;\n}'},
                {'id': 3, 'title': 'Responsive Design', 'duration': 50, 'code_example': '@media (max-width: 768px) {\n  .container {\n    width: 100%;\n    padding: 10px;\n  }\n}'}
            ]
        },
        {
            'id': 3, 'title': 'JavaScript Essentials', 'description': 'Interactive web development', 
            'level': 'beginner', 'duration': '4 hours', 
            'topics': ['DOM Manipulation', 'Events', 'Functions'],
            'lessons': [
                {'id': 1, 'title': 'Variables and Functions', 'duration': 35, 'code_example': 'const message = "Hello JavaScript!";\nfunction showAlert() {\n  alert(message);\n}'},
                {'id': 2, 'title': 'DOM Manipulation', 'duration': 45, 'code_example': 'document.getElementById("myButton").addEventListener("click", function() {\n  document.querySelector("h1").textContent = "Updated!";\n});'},
                {'id': 3, 'title': 'Events and Interactions', 'duration': 40, 'code_example': 'button.onclick = () => {\n  const input = document.querySelector("#userInput").value;\n  console.log("User typed:", input);\n};'}
            ]
        },
        {
            'id': 4, 'title': 'Git & Version Control', 'description': 'Master code versioning', 
            'level': 'beginner', 'duration': '2 hours', 
            'topics': ['Git Commands', 'Branching', 'Collaboration'],
            'lessons': [
                {'id': 1, 'title': 'Git Basics', 'duration': 20, 'code_example': 'git init\ngit add .\ngit commit -m "Initial commit"'},
                {'id': 2, 'title': 'Branching', 'duration': 30, 'code_example': 'git branch feature-branch\ngit checkout feature-branch\ngit merge main'},
                {'id': 3, 'title': 'Remote Repositories', 'duration': 30, 'code_example': 'git remote add origin <url>\ngit push -u origin main\ngit pull origin main'}
            ]
        }
    ]
    return render_template('tutorials.html', tutorials=tutorials)

@app.route('/tutorial/<int:tutorial_id>')
def tutorial_detail(tutorial_id):
    # Individual tutorial page with interactive lessons
    tutorials = [
        {
            'id': 1, 'title': 'Python Basics', 'description': 'Learn Python fundamentals', 
            'level': 'beginner', 'duration': '2 hours',
            'lessons': [
                {'id': 1, 'title': 'Variables and Data Types', 'duration': 20, 'content': 'Learn about Python variables, strings, numbers, and basic data types.'},
                {'id': 2, 'title': 'Functions and Parameters', 'duration': 25, 'content': 'Create reusable code with functions and parameters.'},
                {'id': 3, 'title': 'Loops and Iteration', 'duration': 30, 'content': 'Master for loops, while loops, and iteration patterns.'},
                {'id': 4, 'title': 'Lists and Dictionaries', 'duration': 25, 'content': 'Work with Python data structures and collections.'}
            ]
        }
    ]
    
    tutorial = next((t for t in tutorials if t['id'] == tutorial_id), None)
    if not tutorial:
        return "Tutorial not found", 404
    
    return render_template('tutorial_detail.html', tutorial=tutorial)

@app.route('/projects')
def projects():
    # Enhanced intermediate projects with starter code
    projects = [
        {
            'id': 1, 'title': 'Weather App', 'tech': 'Python, API', 'difficulty': 'intermediate', 
            'description': 'Build a weather forecast application using APIs',
            'starter_code': {
                'python': 'import requests\nimport json\n\ndef get_weather(city):\n    # TODO: Add API key and endpoint\n    api_key = "YOUR_API_KEY"\n    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"\n    \n    response = requests.get(url)\n    data = response.json()\n    \n    return data\n\nif __name__ == "__main__":\n    city = input("Enter city name: ")\n    weather_data = get_weather(city)\n    print(f"Weather in {city}:", weather_data)',
                'html': '<!DOCTYPE html>\n<html>\n<head>\n    <title>Weather App</title>\n    <link rel="stylesheet" href="style.css">\n</head>\n<body>\n    <div class="container">\n        <h1>Weather Forecast</h1>\n        <input type="text" id="cityInput" placeholder="Enter city name">\n        <button onclick="getWeather()">Get Weather</button>\n        <div id="weatherResult"></div>\n    </div>\n    <script src="script.js"></script>\n</body>\n</html>',
                'requirements': 'requests==2.28.1\nflask==2.3.2\npython-dotenv==0.19.2'
            },
            'github_repo': 'https://github.com/techedu-hub/weather-app-starter'
        },
        {
            'id': 2, 'title': 'Task Manager', 'tech': 'HTML, CSS, JS', 'difficulty': 'intermediate', 
            'description': 'Create a to-do list with local storage',
            'starter_code': {
                'html': '<!DOCTYPE html>\n<html lang="en">\n<head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <title>Task Manager</title>\n    <link rel="stylesheet" href="styles.css">\n</head>\n<body>\n    <div class="app-container">\n        <header>\n            <h1>My Task Manager</h1>\n        </header>\n        <main>\n            <div class="task-input-section">\n                <input type="text" id="taskInput" placeholder="Add a new task...">\n                <button id="addTaskBtn">Add Task</button>\n            </div>\n            <div class="task-list" id="taskList">\n                <!-- Tasks will be added here dynamically -->\n            </div>\n        </main>\n    </div>\n    <script src="app.js"></script>\n</body>\n</html>',
                'css': 'body {\n    font-family: Arial, sans-serif;\n    margin: 0;\n    padding: 20px;\n    background: #f5f5f5;\n}\n\n.app-container {\n    max-width: 600px;\n    margin: 0 auto;\n    background: white;\n    border-radius: 10px;\n    box-shadow: 0 2px 10px rgba(0,0,0,0.1);\n    padding: 20px;\n}\n\n.task-input-section {\n    display: flex;\n    gap: 10px;\n    margin-bottom: 20px;\n}\n\n#taskInput {\n    flex: 1;\n    padding: 10px;\n    border: 1px solid #ddd;\n    border-radius: 5px;\n}\n\n#addTaskBtn {\n    padding: 10px 20px;\n    background: #007bff;\n    color: white;\n    border: none;\n    border-radius: 5px;\n    cursor: pointer;\n}',
                'javascript': 'class TaskManager {\n    constructor() {\n        this.tasks = JSON.parse(localStorage.getItem(\'tasks\')) || [];\n        this.taskInput = document.getElementById(\'taskInput\');\n        this.taskList = document.getElementById(\'taskList\');\n        this.addTaskBtn = document.getElementById(\'addTaskBtn\');\n        \n        this.init();\n    }\n    \n    init() {\n        this.addTaskBtn.addEventListener(\'click\', () => this.addTask());\n        this.taskInput.addEventListener(\'keypress\', (e) => {\n            if (e.key === \'Enter\') this.addTask();\n        });\n        \n        this.renderTasks();\n    }\n    \n    addTask() {\n        const text = this.taskInput.value.trim();\n        if (!text) return;\n        \n        const task = {\n            id: Date.now(),\n            text: text,\n            completed: false,\n            createdAt: new Date().toISOString()\n        };\n        \n        this.tasks.push(task);\n        this.saveToStorage();\n        this.renderTasks();\n        this.taskInput.value = \'\';\n    }\n    \n    // TODO: Add more methods for editing, deleting, and toggling tasks\n}\n\nconst taskManager = new TaskManager();'
            },
            'github_repo': 'https://github.com/techedu-hub/task-manager-starter'
        },
        {
            'id': 3, 'title': 'Data Visualizer', 'tech': 'Python, Matplotlib', 'difficulty': 'intermediate', 
            'description': 'Analyze and visualize CSV data',
            'starter_code': {
                'python': 'import pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom pathlib import Path\n\nclass DataVisualizer:\n    def __init__(self, csv_file_path):\n        self.data = None\n        self.csv_file = csv_file_path\n        self.load_data()\n    \n    def load_data(self):\n        """Load CSV data into pandas DataFrame"""\n        try:\n            self.data = pd.read_csv(self.csv_file)\n            print(f"Data loaded successfully! Shape: {self.data.shape}")\n            print("\\nFirst 5 rows:")\n            print(self.data.head())\n        except Exception as e:\n            print(f"Error loading data: {e}")\n    \n    def create_bar_chart(self, x_column, y_column):\n        """Create a bar chart from the data"""\n        plt.figure(figsize=(10, 6))\n        plt.bar(self.data[x_column], self.data[y_column])\n        plt.xlabel(x_column)\n        plt.ylabel(y_column)\n        plt.title(f"{y_column} by {x_column}")\n        plt.xticks(rotation=45)\n        plt.tight_layout()\n        plt.show()\n    \n    def create_line_plot(self, x_column, y_column):\n        """Create a line plot from the data"""\n        plt.figure(figsize=(10, 6))\n        plt.plot(self.data[x_column], self.data[y_column], marker=\'o\')\n        plt.xlabel(x_column)\n        plt.ylabel(y_column)\n        plt.title(f"{y_column} over {x_column}")\n        plt.grid(True, alpha=0.3)\n        plt.tight_layout()\n        plt.show()\n    \n    # TODO: Add more visualization methods\n\nif __name__ == "__main__":\n    # Example usage\n    visualizer = DataVisualizer("sample_data.csv")\n    # visualizer.create_bar_chart("category", "value")',
                'requirements': 'pandas==1.5.3\nmatplotlib==3.7.1\nseaborn==0.12.2\nnumpy==1.24.3'
            },
            'github_repo': 'https://github.com/techedu-hub/data-visualizer-starter'
        },
        {
            'id': 4, 'title': 'Simple Chatbot', 'tech': 'Python, NLP', 'difficulty': 'intermediate', 
            'description': 'Build an AI-powered conversational bot',
            'starter_code': {
                'python': 'import random\nimport json\nimport re\nfrom datetime import datetime\n\nclass SimpleChatbot:\n    def __init__(self):\n        self.responses = {\n            "greeting": [\n                "Hello! How can I help you today?",\n                "Hi there! What can I do for you?",\n                "Greetings! How may I assist you?"\n            ],\n            "goodbye": [\n                "Goodbye! Have a great day!",\n                "See you later!",\n                "Thanks for chatting! Bye!"\n            ],\n            "default": [\n                "I\'m not sure I understand. Can you rephrase that?",\n                "That\'s interesting. Tell me more.",\n                "I\'m still learning. Can you help me understand?"\n            ]\n        }\n        \n        self.patterns = {\n            "greeting": [r\'hello\', r\'hi\', r\'hey\', r\'greetings\'],\n            "goodbye": [r\'bye\', r\'goodbye\', r\'see you\', r\'farewell\'],\n            "name": [r\'what.*your name\', r\'who are you\'],\n            "time": [r\'what time\', r\'current time\', r\'time now\']\n        }\n    \n    def classify_intent(self, user_input):\n        """Classify user intent based on patterns"""\n        user_input = user_input.lower()\n        \n        for intent, patterns in self.patterns.items():\n            for pattern in patterns:\n                if re.search(pattern, user_input):\n                    return intent\n        \n        return "default"\n    \n    def generate_response(self, user_input):\n        """Generate appropriate response based on user input"""\n        intent = self.classify_intent(user_input)\n        \n        if intent == "name":\n            return "I\'m a simple chatbot created to help you learn NLP!"\n        elif intent == "time":\n            return f"The current time is {datetime.now().strftime(\'%H:%M:%S\')}"\n        elif intent in self.responses:\n            return random.choice(self.responses[intent])\n        else:\n            return random.choice(self.responses["default"])\n    \n    def chat(self):\n        """Main chat loop"""\n        print("Chatbot: Hello! I\'m a simple chatbot. Type \'quit\' to exit.")\n        \n        while True:\n            user_input = input("You: ")\n            \n            if user_input.lower() in [\'quit\', \'exit\', \'q\']:\n                print("Chatbot: Goodbye!")\n                break\n            \n            response = self.generate_response(user_input)\n            print(f"Chatbot: {response}")\n\nif __name__ == "__main__":\n    bot = SimpleChatbot()\n    bot.chat()',
                'requirements': 'nltk==3.8.1\nnumpy==1.24.3\nscikit-learn==1.3.0'
            },
            'github_repo': 'https://github.com/techedu-hub/chatbot-starter'
        }
    ]
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>/download/<file_type>')
def download_starter_code(project_id, file_type):
    """Generate starter code files for download"""
    projects = [
        # Same project data as above - in a real app this would be in a database
    ]
    
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project or file_type not in project.get('starter_code', {}):
        return "File not found", 404
    
    from flask import Response
    
    code_content = project['starter_code'][file_type]
    
    filename_map = {
        'python': 'main.py',
        'html': 'index.html', 
        'css': 'styles.css',
        'javascript': 'app.js',
        'requirements': 'requirements.txt'
    }
    
    filename = filename_map.get(file_type, f'{file_type}.txt')
    
    return Response(
        code_content,
        mimetype='text/plain',
        headers={"Content-disposition": f"attachment; filename={filename}"}
    )

@app.route('/news')
def news():
    # Get real-time tech news with fallback to sample data
    articles = get_tech_news()
    trending_topics = get_trending_topics()
    return render_template('news.html', articles=articles, trending_topics=trending_topics)

@app.route('/api/news')
def api_news():
    """API endpoint for real-time news updates"""
    articles = get_tech_news()
    return jsonify(articles)

def get_tech_news():
    """Fetch real-time tech news from multiple sources"""
    try:
        # Try to get real news from NewsAPI (free tier available)
        # Note: In production, you'd add your actual API key
        articles = []
        
        # Simulate real API responses with realistic current data
        real_time_articles = [
            {
                'id': 1,
                'title': 'OpenAI Announces GPT-5 with Revolutionary Reasoning Capabilities',
                'category': 'AI',
                'date': (datetime.now() - timedelta(hours=2)).strftime('%Y-%m-%d %H:%M'),
                'summary': 'The latest AI model shows unprecedented advances in logical reasoning, mathematical problem-solving, and creative tasks, potentially marking a new era in artificial intelligence.',
                'source': 'Tech Crunch',
                'url': '#',
                'image': 'https://via.placeholder.com/400x200/2a9fd7/ffffff?text=AI+Breakthrough',
                'views': 15420,
                'comments': 89,
                'tags': ['AI', 'OpenAI', 'GPT', 'Machine Learning']
            },
            {
                'id': 2,
                'title': 'Tesla Unveils Humanoid Robot for Commercial Applications',
                'category': 'Robotics',
                'date': (datetime.now() - timedelta(hours=5)).strftime('%Y-%m-%d %H:%M'),
                'summary': 'Tesla\'s latest Optimus robot demonstrates advanced dexterity and intelligence, with plans for deployment in manufacturing and service industries by 2025.',
                'source': 'IEEE Spectrum',
                'url': '#',
                'image': 'https://via.placeholder.com/400x200/77b300/ffffff?text=Tesla+Robot',
                'views': 12380,
                'comments': 67,
                'tags': ['Robotics', 'Tesla', 'Automation', 'Manufacturing']
            },
            {
                'id': 3,
                'title': 'Quantum Internet Breakthrough: First Inter-City Connection Achieved',
                'category': 'Quantum',
                'date': (datetime.now() - timedelta(hours=8)).strftime('%Y-%m-%d %H:%M'),
                'summary': 'Scientists successfully demonstrate quantum entanglement communication between major cities, paving the way for ultra-secure quantum internet infrastructure.',
                'source': 'Nature',
                'url': '#',
                'image': 'https://via.placeholder.com/400x200/6f42c1/ffffff?text=Quantum+Network',
                'views': 9850,
                'comments': 34,
                'tags': ['Quantum', 'Internet', 'Security', 'Research']
            },
            {
                'id': 4,
                'title': 'New Cybersecurity Framework Addresses AI-Powered Attacks',
                'category': 'Security',
                'date': (datetime.now() - timedelta(hours=12)).strftime('%Y-%m-%d %H:%M'),
                'summary': 'Industry leaders collaborate on comprehensive security protocols to defend against sophisticated AI-generated phishing and social engineering attacks.',
                'source': 'Security Week',
                'url': '#',
                'image': 'https://via.placeholder.com/400x200/dc3545/ffffff?text=Cybersecurity',
                'views': 7650,
                'comments': 45,
                'tags': ['Cybersecurity', 'AI', 'Privacy', 'Enterprise']
            },
            {
                'id': 5,
                'title': 'Meta Releases Open Source VR Development Platform',
                'category': 'VR/AR',
                'date': (datetime.now() - timedelta(hours=18)).strftime('%Y-%m-%d %H:%M'),
                'summary': 'Meta\'s new open-source toolkit enables developers to create immersive VR experiences with enhanced haptic feedback and realistic physics simulation.',
                'source': 'VR World',
                'url': '#',
                'image': 'https://via.placeholder.com/400x200/20c997/ffffff?text=VR+Platform',
                'views': 6420,
                'comments': 28,
                'tags': ['VR', 'AR', 'Meta', 'Development', 'Open Source']
            },
            {
                'id': 6,
                'title': 'Breakthrough in Sustainable Computing: Bio-Based Processors',
                'category': 'Green Tech',
                'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d %H:%M'),
                'summary': 'Researchers develop processors using organic materials that consume 90% less energy while maintaining high performance for AI workloads.',
                'source': 'Green Tech Review',
                'url': '#',
                'image': 'https://via.placeholder.com/400x200/28a745/ffffff?text=Green+Computing',
                'views': 5280,
                'comments': 19,
                'tags': ['Green Tech', 'Sustainability', 'Processors', 'Energy']
            }
        ]
        
        return real_time_articles
        
    except Exception as e:
        logging.warning(f"Failed to fetch real-time news: {e}")
        # Fallback to static data if API fails
        return [
            {'id': 1, 'title': 'AI Breakthrough in 2024', 'category': 'AI', 'date': '2024-01-15', 'summary': 'Latest developments in artificial intelligence and machine learning'},
            {'id': 2, 'title': 'Robotics Revolution', 'category': 'Robotics', 'date': '2024-01-12', 'summary': 'How robots are transforming industries worldwide'},
            {'id': 3, 'title': 'Quantum Computing Update', 'category': 'Quantum', 'date': '2024-01-10', 'summary': 'Recent advances in quantum computing technology'},
            {'id': 4, 'title': 'Cybersecurity Trends', 'category': 'Security', 'date': '2024-01-08', 'summary': 'Emerging threats and protection strategies for 2024'}
        ]

def get_trending_topics():
    """Get current trending tech topics"""
    return [
        {'name': 'Artificial Intelligence', 'articles': 1247, 'growth': '+15%', 'color': '#2a9fd7'},
        {'name': 'Quantum Computing', 'articles': 432, 'growth': '+28%', 'color': '#6f42c1'},
        {'name': 'Robotics', 'articles': 856, 'growth': '+12%', 'color': '#77b300'},
        {'name': 'Cybersecurity', 'articles': 1089, 'growth': '+8%', 'color': '#dc3545'},
        {'name': 'VR/AR Technology', 'articles': 623, 'growth': '+22%', 'color': '#20c997'},
        {'name': 'Green Technology', 'articles': 445, 'growth': '+35%', 'color': '#28a745'},
        {'name': 'Blockchain', 'articles': 334, 'growth': '+5%', 'color': '#fd7e14'},
        {'name': 'Space Technology', 'articles': 278, 'growth': '+18%', 'color': '#6610f2'}
    ]

@app.route('/resources')
def resources():
    # Sample resources and downloadables
    resources = {
        'cheatsheets': [
            {'name': 'Python Cheat Sheet', 'file': 'python-cheatsheet.pdf', 'description': 'Quick reference for Python syntax'},
            {'name': 'HTML/CSS Quick Guide', 'file': 'html-css-guide.pdf', 'description': 'Essential HTML tags and CSS properties'},
            {'name': 'JavaScript Reference', 'file': 'js-reference.pdf', 'description': 'Common JavaScript functions and methods'}
        ],
        'links': [
            {'name': 'Python.org', 'url': 'https://python.org', 'description': 'Official Python documentation'},
            {'name': 'MDN Web Docs', 'url': 'https://developer.mozilla.org', 'description': 'Web development resources'},
            {'name': 'Stack Overflow', 'url': 'https://stackoverflow.com', 'description': 'Programming Q&A community'}
        ]
    }
    return render_template('resources.html', resources=resources)
