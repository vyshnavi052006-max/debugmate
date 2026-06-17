import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os

# Set page config
st.set_page_config(
    page_title="DebugMate - Code Debugger",
    page_icon="🐛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 20px;
    }
    .description-box {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        border-left: 4px solid #1f77b4;
    }
    .example-box {
        background-color: #e8f4f8;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .disclaimer-box {
        background-color: #fff3cd;
        padding: 12px;
        border-radius: 5px;
        margin: 20px 0;
        border-left: 4px solid #ff9800;
    }
    .footer {
        text-align: center;
        color: #666;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #ddd;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for API key
if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = False

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Header
st.markdown('<h1 class="main-header">🐛 DebugMate - Your Code Debugging Assistant</h1>', unsafe_allow_html=True)

# Sidebar for API Key setup
with st.sidebar:
    st.header("⚙️ Setup")
    st.write("**Step 1:** Get your free Gemini API key from [here](https://aistudio.google.com/app/apikey)")
    
    api_key = st.text_input(
        "Enter your Gemini API Key:",
        type="password",
        help="Your API key is never stored. It's used only for this session."
    )
    
    if api_key:
        try:
            genai.configure(api_key=api_key)
            st.session_state.api_key_set = True
            st.success("✅ API Key configured successfully!")
        except Exception as e:
            st.error(f"❌ Invalid API key: {str(e)}")
            st.session_state.api_key_set = False
    
    st.divider()
    st.write("**Made for GENAI Internship**")

def is_code_related(query):
    """Check if the query is code-related"""
    code_keywords = [
        "code", "error", "bug", "debug", "fix", "function", "loop", "variable",
        "syntax", "exception", "traceback", "python", "javascript", "java", "c++",
        "html", "css", "sql", "api", "class", "method", "array", "string",
        "import", "module", "library", "algorithm", "logic", "line", "error message",
        "why", "what's wrong", "how do i fix", "problem with", "issue with"
    ]
    
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in code_keywords)

def get_debugmate_response(user_query, api_key):
    """Get response from Gemini AI"""
    
    model = genai.GenerativeModel('gemini-pro')
    
    system_prompt = """You are DebugMate, an expert code debugging assistant. Your responsibilities:

1. ANALYZE code snippets for errors and issues
2. EXPLAIN what's wrong in simple, clear language
3. SUGGEST fixes with code examples
4. TEACH best practices to prevent similar bugs
5. STAY FOCUSED on code debugging only

When responding:
- Be concise but thorough
- Provide code examples in markdown blocks with language specified
- Explain the error cause, not just the fix
- Suggest prevention strategies
- If the code is correct, say so and explain why it works

If the question is NOT about code debugging, politely decline and redirect to coding questions."""
    
    try:
        chat = model.start_chat()
        
        message = f"""{system_prompt}

User Question: {user_query}

Please analyze and provide debugging help."""
        
        response = chat.send_message(message)
        return response.text
    
    except Exception as e:
        raise Exception(f"Failed to get response from Gemini: {str(e)}")

# Main content
if not st.session_state.api_key_set:
    st.warning("⚠️ Please enter your Gemini API key in the sidebar to get started!")
    st.info("""
    **How to get your free Gemini API key:**
    1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
    2. Click "Create API Key"
    3. Copy the key and paste it in the sidebar
    4. Start debugging!
    """)
else:
    # Project Description
    st.markdown("""
    <div class="description-box">
    <h3>📋 What is DebugMate?</h3>
    <p>DebugMate is an AI-powered code debugging assistant that helps you:</p>
    <ul>
    <li><strong>Analyze</strong> your code for errors and issues</li>
    <li><strong>Explain</strong> what's wrong and why</li>
    <li><strong>Suggest</strong> fixes and improvements</li>
    <li><strong>Learn</strong> best practices from your mistakes</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Example Questions
    st.markdown("### 💡 Example Questions You Can Ask:")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="example-box">
        <strong>✓ "Why is my loop not working?"</strong><br/>
        Paste your Python loop code and I'll debug it.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="example-box">
        <strong>✓ "Fix this JavaScript error"</strong><br/>
        Share the error message and code snippet.
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="example-box">
        <strong>✓ "What's wrong with this function?"</strong><br/>
        Paste the function code for analysis.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="example-box">
        <strong>✓ "How do I fix this error?"</strong><br/>
        Share the error message and code.
        </div>
        """, unsafe_allow_html=True)
    
    # Disclaimer
    st.markdown("""
    <div class="disclaimer-box">
    <strong>⚠️ Disclaimer:</strong>
    <ul>
    <li>DebugMate is an AI assistant and may not catch all bugs</li>
    <li>Always test suggested fixes thoroughly</li>
    <li>For production code, use dedicated debugging tools</li>
    <li>This tool is best for learning and quick debugging</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat Interface
    st.markdown("### 💬 Chat with DebugMate")
    
    # Display chat history
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])
    
    # User input
    user_input = st.chat_input(
        "Paste your code or ask a debugging question...",
        placeholder="Example: Why is this function not working?"
    )
    
    if user_input:
        # Check if input is related to code debugging
        if not is_code_related(user_input):
            response = "I'm DebugMate, a code debugging specialist. I can only help with code-related questions like:\n\n✓ Debugging code errors\n✓ Explaining bugs\n✓ Suggesting fixes\n✓ Learning best practices"
        else:
            # Add user message to chat
            st.session_state.chat_history.append({
                "role": "user",
                "content": user_input
            })
            
            # Display user message
            st.chat_message("user").write(user_input)
            
            # Get response from Gemini
            try:
                response = get_debugmate_response(user_input, api_key)
            except Exception as e:
                response = f"❌ Error: {str(e)}\n\nPlease make sure your API key is valid and you have internet connection."
        
        # Add assistant message to chat
        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })
        
        # Display assistant message
        st.chat_message("assistant").write(response)
    
    # Footer
    st.markdown("""
    <div class="footer">
    <p>🐛 <strong>DebugMate</strong> - Code Debugger Assistant</p>
    <p>Built for GENAI Internship by <strong>Vyshnavi</strong></p>
    <p>Powered by Google Gemini AI | 2026</p>
    </div>
    """, unsafe_allow_html=True)
