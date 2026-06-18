```python
import streamlit as st
import google.generativeai as genai

# Page Configuration
st.set_page_config(
    page_title="DebugMate - Code Debugger",
    page_icon="🐛",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    text-align: center;
    color: #1f77b4;
}

.description-box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "api_key_set" not in st.session_state:
    st.session_state.api_key_set = False

# Header
st.markdown(
    "<h1 class='main-header'>🐛 DebugMate - Code Debugger Assistant</h1>",
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("⚙️ Setup")

    st.write(
        "Get your Gemini API key from:\nhttps://aistudio.google.com/app/apikey"
    )

    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

    if api_key:
        try:
            genai.configure(api_key=api_key)

            test_model = genai.GenerativeModel(
                "gemini-1.5-flash"
            )

            test_model.generate_content("Hello")

            st.session_state.api_key_set = True
            st.success("✅ API Key verified")

        except Exception as e:
            st.session_state.api_key_set = False
            st.error(f"❌ {str(e)}")

# Helper Function
def is_code_related(query):
    keywords = [
        "code", "bug", "debug", "error", "python",
        "javascript", "java", "html", "css",
        "sql", "api", "function", "loop",
        "variable", "class", "exception",
        "traceback", "syntax"
    ]

    query = query.lower()

    return any(word in query for word in keywords)

# Gemini Response
def get_debugmate_response(user_query):

    system_prompt = """
You are DebugMate, an expert code debugging assistant.

Your responsibilities:
1. Analyze code.
2. Find bugs and errors.
3. Explain problems clearly.
4. Suggest fixes.
5. Provide corrected code.
6. Share best practices.

Always answer in a beginner-friendly way.
"""

    try:
        model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

        response = model.generate_content(
            f"{system_prompt}\n\nUser Query:\n{user_query}"
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"

# Main UI
if not st.session_state.api_key_set:

    st.warning(
        "⚠️ Please enter your Gemini API key in the sidebar."
    )

    st.info("""
1. Visit Google AI Studio
2. Create API Key
3. Paste it in the sidebar
4. Start debugging
""")

else:

    st.markdown("""
    <div class="description-box">
    <h3>📋 About DebugMate</h3>

    DebugMate helps you:

    ✔ Debug code

    ✔ Fix errors

    ✔ Understand exceptions

    ✔ Learn coding best practices

    ✔ Improve your programming skills
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💡 Example Questions")

    st.write("""
- Why am I getting a TypeError?
- Fix my Python loop.
- Debug this JavaScript function.
- Explain this SQL error.
- Improve my code performance.
""")

    st.subheader("💬 Chat with DebugMate")

    for msg in st.session_state.chat_history:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input(
        "Paste your code or ask a debugging question..."
    )

    if user_input:

        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.write(user_input)

        if is_code_related(user_input):

            with st.spinner("Analyzing code..."):
                response = get_debugmate_response(
                    user_input
                )

        else:
            response = """
I'm DebugMate 🐛

Please ask code-related questions such as:

• Debugging errors
• Fixing bugs
• Explaining code
• Optimizing functions
• Understanding exceptions
"""

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)

    st.markdown("""
    <div class="footer">
    <hr>
    <p>🐛 DebugMate - AI Code Debugger</p>
    <p>Built by Vyshnavi</p>
    <p>Powered by Google Gemini 1.5 Flash</p>
    </div>
    """, unsafe_allow_html=True)
```
