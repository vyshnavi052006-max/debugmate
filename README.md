# 🐛 DebugMate - Code Debugger Assistant

**A GENAI Internship Project by Vyshnavi**

DebugMate is an AI-powered chatbot that helps you debug code, understand errors, and learn best practices. It analyzes code snippets, explains what's wrong, and suggests fixes using Google Gemini AI.

## Features

✅ **Code Analysis** - Analyze your code for errors and issues
✅ **Error Explanation** - Get clear explanations of what went wrong
✅ **Fix Suggestions** - Receive actionable fixes with code examples
✅ **Best Practices** - Learn how to prevent similar bugs
✅ **Multi-Language Support** - Works with Python, JavaScript, Java, C++, SQL, and more
✅ **Clean UI** - Professional, user-friendly interface
✅ **Domain-Specific** - Focuses only on code debugging

## Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Model**: Google Gemini API
- **Deployment**: Streamlit Cloud
- **Language**: Python 3.8+

## How to Run Locally

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Free Gemini API key

### Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/vyshnavi052006-max/debugmate.git
cd debugmate
```

2. **Create a virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Get your free Gemini API key**:
   - Visit: https://aistudio.google.com/app/apikey
   - Click "Create API Key"
   - Copy the key

5. **Run the app**:
```bash
streamlit run app.py
```

6. **Open in browser**:
   - The app will open at `http://localhost:8501`
   - Paste your Gemini API key in the sidebar

## How to Deploy on Streamlit Cloud (FREE)

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Initial DebugMate project"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Click "New app"
3. Select your GitHub repository (vyshnavi052006-max/debugmate)
4. Select branch: `main`
5. Set main file path: `app.py`
6. Click "Deploy"

### Step 3: Add Secret (API Key)
1. Go to your app's settings
2. Click "Secrets"
3. Add your Gemini API key:
```
GEMINI_API_KEY = "your-api-key-here"
```

## Usage Examples

### Example 1: Debug a Python Error
```
User: "Why is this not working?"
[Paste Python code with error]

DebugMate: [Analyzes the code, explains the bug, suggests fix]
```

### Example 2: Understand an Exception
```
User: "What does this error mean?"
[Paste error message and code]

DebugMate: [Explains the error and how to fix it]
```

### Example 3: Improve Code
```
User: "Is this JavaScript function correct?"
[Paste JavaScript function]

DebugMate: [Reviews code, identifies issues, suggests improvements]
```

## Project Requirements Met

✅ Frontend webpage with header, description, and chat interface
✅ Working chat input and response display
✅ Instructions and example questions
✅ Disclaimer about limitations
✅ Footer with name and internship attribution
✅ Domain-specific responses (code debugging only)
✅ Error handling for API failures
✅ API key securely handled (not hardcoded)
✅ Deployed on public URL
✅ Code on GitHub repository

## Disclaimer

⚠️ **Important:**
- DebugMate is an AI assistant and may not catch all bugs
- Always test suggested fixes thoroughly before production use
- For production code, use dedicated debugging tools and code analysis
- This tool is best for learning and quick debugging
- Always review AI-generated suggestions carefully

## Point System

| Component | Points |
|-----------|--------|
| Submission & Deployment | 15 |
| Demo & Evaluation | 35 |
| **Base Total** | **50** |
| Bonus (if top 3) | +50 |
| **Total Possible** | **100** |

## Files Structure

```
debugmate/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .gitignore         # Hide sensitive files
└── README.md          # This file
```

## Support

For questions during the internship:
- Discord: Real-time doubt clarification
- MS Teams: Official announcements
- GitHub: Code repository

## Author

**Vyshnavi** - GENAI Internship 2026

---

**Built for GENAI Internship Challenge**
*Deadline: 18-06-2026, 7:00 PM IST*