import streamlit as st

# Uncomment these lines to use API instead of direct function calls
# from frontend.api import chatbot_ui    
# from frontend.api import analytics_ui  

from frontend.streamlit_files import chatbot_analytics

# Streamlit Page Config
st.set_page_config(page_title="AI Customer Support System", page_icon="🤖", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        /* Advanced Dark Theme Styles (No Black) */
        .stApp {
            background: linear-gradient(rgba(30, 27, 75, 0.9), rgba(30, 27, 75, 0.9)), url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ49QzWaMyGl_Z6_xmSqLny5yFTtjawDVPpxw&s');
            background-size: cover;
            background-attachment: fixed;
            color: #a5b4fc;
            font-family: 'Poppins', sans-serif;
        }
        .main-container {
            background: linear-gradient(135deg, rgba(55, 48, 163, 0.85), rgba(76, 29, 149, 0.85));
            border-radius: 15px;
            padding: 30px;
            margin: 20px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.6);
            border: 2px solid #60a5fa;
            backdrop-filter: blur(10px);
        }
        h1, h2, h3 {
            color: #f9a8d4;
            text-shadow: 0 0 12px rgba(249, 168, 212, 0.8);
            animation: pulseGlow 2s ease-in-out infinite;
        }
        .stButton>button {
            background: linear-gradient(45deg, #ec4899, #7c3aed);
            color: #fef08a;
            border-radius: 12px;
            padding: 14px 30px;
            font-weight: 600;
            font-size: 1.1em;
            border: none;
            box-shadow: 0 0 15px rgba(236, 72, 153, 0.8);
            transition: all 0.4s ease;
            position: relative;
            overflow: hidden;
        }
        .stButton>button:hover {
            background: linear-gradient(45deg, #db2777, #6d28d9);
            box-shadow: 0 0 25px rgba(236, 72, 153, 1);
            transform: scale(1.1);
            color: #e0e7ff;
        }
        .stButton>button::after {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300%;
            height: 300%;
            background: rgba(96, 165, 250, 0.2);
            transition: all 0.6s ease;
            transform: translate(-50%, -50%) scale(0);
            border-radius: 50%;
        }
        .stButton>button:hover::after {
            transform: translate(-50%, -50%) scale(1);
        }
        .stRadio label, .stRadio div[role="radiogroup"] {
            color: #a5b4fc;
            font-size: 1.1em;
        }
        .stRadio div[data-baseweb="radio"] {
            background: linear-gradient(135deg, rgba(55, 48, 163, 0.9), rgba(76, 29, 149, 0.9));
            border-radius: 10px;
            padding: 10px;
            border: 2px solid #60a5fa;
        }
        .stRadio div[data-baseweb="radio"] input:checked + div {
            background: #ec4899;
            border-color: #fef08a;
        }
        .stImage {
            border-radius: 12px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.4);
            animation: scaleIn 0.8s ease-in-out;
        }
        .stMarkdown p, .stMarkdown li {
            color: #a5b4fc;
            font-size: 1.15em;
            line-height: 1.9;
        }
        .stMarkdown ul li::marker {
            color: #60a5fa;
        }
        .stSidebar {
            background: linear-gradient(135deg, rgba(55, 48, 163, 0.9), rgba(76, 29, 149, 0.9));
            color: #a5b4fc;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(8px);
        }
        .stSidebar h3 {
            color: #fef08a;
            text-shadow: 0 0 8px rgba(254, 240, 138, 0.8);
        }
        .stSidebar p {
            color: #a5b4fc;
        }
        /* Animations */
        @keyframes pulseGlow {
            0% { text-shadow: 0 0 10px rgba(249, 168, 212, 0.8); }
            50% { text-shadow: 0 0 20px rgba(249, 168, 212, 1); }
            100% { text-shadow: 0 0 10px rgba(249, 168, 212, 0.8); }
        }
        @keyframes scaleIn {
            from { transform: scale(0.95); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        @keyframes slideInLeft {
            from { transform: translateX(-30px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/295/295128.png", width=100)
    st.markdown("<h3>📌 Navigation</h3>", unsafe_allow_html=True)
    page = st.radio("Select Page", ["🏠 Home", "💬 Chatbot", "🔧 Fine Tuned Bot", "📶 Analytics Dashboard", "📖 FAQs"])

# Home Page
if page == "🏠 Home":
    st.markdown("""
        <div class="main-container">
            <h1>🤖 AI Customer Support System</h1>
            <h2 style="animation: slideInLeft 0.6s ease-in-out;">🌟 Welcome to the AI-Powered Customer Support System!</h2>
            <p>
                This intelligent chatbot system is designed to <b>enhance customer interactions</b> by providing instant support, analyzing sentiment, and tracking trends.
            </p>
            <hr style="border: 1px solid #60a5fa;">
            <h3 style="animation: slideInLeft 0.8s ease-in-out;">🚀 Key Features:</h3>
            <ul>
                <li>💬 <b>Smart AI Chatbot:</b> Answers customer queries using a mix of <b>predefined FAQs & AI-generated responses</b>.</li>
                <li>🔧 <b>Fine-Tuned LLM:</b> Leverages a custom-trained language model for more accurate and context-specific responses.</li>
                <li>📊 <b>Analytics Dashboard:</b> Gain insights into customer interactions, trends, and engagement.</li>
                <li>🧠 <b>Sentiment Analysis:</b> Tracks and categorizes customer emotions (Positive, Negative, Neutral).</li>
                <li>📅 <b>Time-Based Engagement Tracking:</b> Analyze <b>peak user activity hours</b> for better customer support.</li>
                <li>📉 <b>Trend Analysis:</b> Discover emerging trends in customer inquiries.</li>
            </ul>
            <h3 style="animation: slideInLeft 1s ease-in-out;">🔍 How It Works:</h3>
            <ul>
                <li>1️⃣ <b>User asks a question</b> 💬</li>
                <li>2️⃣ The chatbot <b>retrieves the best-matching FAQ answer</b> 🔍</li>
                <li>3️⃣ If no match is found, <b>AI or fine-tuned LLM generates a dynamic response</b> 🧠</li>
                <li>4️⃣ The system <b>analyzes sentiment & classifies the question category</b> 📊</li>
                <li>5️⃣ All interactions are stored for future <b>trend analysis & reporting</b> 📈</li>
            </ul>
            <h3 style="animation: slideInLeft 1.2s ease-in-out;">🛠 How to Use It:</h3>
            <ul>
                <li><b>Go to the Chatbot Page</b> 🗨️ → Ask any question and get real-time responses.</li>
                <li><b>Explore the Fine-Tuned Bot Page</b> 🔧 → Experience enhanced responses with our custom-trained LLM.</li>
                <li><b>Explore the Analytics Dashboard</b> 📊 → Visualize customer trends and insights.</li>
                <li><b>Track Sentiment Over Time</b> 📅 → Understand customer emotions and engagement.</li>
            </ul>
            <h3 style="animation: slideInLeft 1.4s ease-in-out;">🏆 Why This System is Powerful?</h3>
            <ul>
                <li>✅ <b>Faster Response Times:</b> AI-driven support for instant answers.</li>
                <li>✅ <b>Better Customer Insights:</b> Learn what customers are talking about.</li>
                <li>✅ <b>Improved Business Decisions:</b> Make data-driven improvements to services.</li>
                <li>✅ <b>Enhanced User Experience:</b> Provide <b>personalized & engaging</b> interactions with fine-tuned LLM capabilities.</li>
            </ul>
            <p>
                <b>Ready to get started? Head over to the Chatbot, Fine-Tuned Bot, & Analytics sections now!</b> 🚀
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3203/3203165.png", width=600)

# Chatbot Page
elif page == "💬 Chatbot":
    # chatbot_ui.chatbot()          # Uncomment these lines to use API instead of direct function calls
    chatbot_analytics.chatbot()
elif page == "🔧 Fine Tuned Bot":
    chatbot_analytics.show_finetuned_llm_details()
# Analytics Dashboard Page
elif page == "📶 Analytics Dashboard":
    # analytics_ui.analytics()      # Uncomment these lines to use API instead of direct function calls
    chatbot_analytics.analytics()
elif page == "📖 FAQs":
    chatbot_analytics.faq_page()