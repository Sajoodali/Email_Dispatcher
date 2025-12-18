import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from email_template import get_email_template
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Globium Cloud | Dispatcher",
    page_icon="📨",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# Load configuration from .env
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "")
COMPANY_NAME = os.getenv("COMPANY_NAME", "Globium Cloud")
COMPANY_ADDRESS = os.getenv("COMPANY_ADDRESS", "Official Business Address")
COMPANY_WEBSITE = os.getenv("COMPANY_WEBSITE", "www.globiumcloud.com")

# Helper: Load and encode logo
def get_base64_logo(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            return base64.b64encode(data).decode()
    except:
        return None

LOGO_BASE64 = get_base64_logo("GC-Logo.jpg")

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# -----------------------------------------------------------------------------
# PREMIUM GLOBIUM CLOUD THEME (Responsive & Blue)
# -----------------------------------------------------------------------------
st.markdown(f"""
    <style>
    /* 1. Global Reset & Modern Typography */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Outfit', 'Inter', sans-serif;
        font-size: 16px;
    }}

    /* 2. Globium Blue Background */
    .stApp {{
        background: radial-gradient(circle at top right, #f0f9ff, #e0f2fe, #bae6fd);
        background-attachment: fixed;
    }}
    
    /* 3. Responsive Container */
    .block-container {{
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
        max-width: 900px !important;
    }}

    @media screen and (max-width: 768px) {{
        .block-container {{
            padding-top: 2rem !important;
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }}
    }}

    /* 4. Elegant Header Section */
    .brand-header {{
        text-align: center;
        margin-bottom: 3rem;
    }}
    
    .brand-title {{
        background: linear-gradient(135deg, #00A3FF 0%, #0077FF 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: clamp(2.5rem, 8vw, 4rem) !important;
        font-weight: 900 !important;
        letter-spacing: -2px;
        margin: 0;
        line-height: 1.1;
    }}
    
    .brand-subtitle {{
        color: #0369a1;
        font-size: clamp(1rem, 4vw, 1.4rem) !important;
        font-weight: 600;
        margin-top: 1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }}

    /* 5. Glassmorphism Main Card */
    div[data-testid="stVerticalBlock"] > div:has(div.stTextInput) {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        padding: clamp(1.5rem, 5vw, 4rem);
        border-radius: 24px;
        box-shadow: 0 20px 50px rgba(0, 100, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.8);
    }}

    /* 6. Optimized Input Fields */
    .stTextInput input {{
        background: #ffffff !important;
        border: 2px solid #bae6fd !important;
        border-radius: 12px !important;
        padding: 1.2rem 1.5rem !important;
        font-size: 1.3rem !important;
        font-weight: 500 !important;
        color: #0c4a6e !important;
    }}

    .stTextArea textarea {{
        background: #ffffff !important;
        border: 2px solid #bae6fd !important;
        border-radius: 12px !important;
        padding: 1rem 1.2rem !important;
        font-size: 1.2rem !important;
        font-weight: 500 !important;
        color: #0c4a6e !important;
    }}

    .stTextInput input:focus, .stTextArea textarea:focus {{
        border-color: #00A3FF !important;
        box-shadow: 0 0 0 4px rgba(0, 163, 255, 0.1) !important;
        outline: none !important;
    }}
    
    /* Elegant Labels */
    .stTextInput label, .stTextArea label {{
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        color: #0369a1 !important;
        margin-bottom: 0.6rem !important;
    }}

    /* 7. Action Button */
    .stButton button {{
        background: linear-gradient(135deg, #00A3FF 0%, #0077FF 100%) !important;
        color: white !important;
        font-weight: 700 !important;
        padding: 1.4rem 3rem !important;
        border-radius: 15px !important;
        border: none !important;
        width: 100% !important;
        font-size: 1.4rem !important;
        box-shadow: 0 10px 20px rgba(0, 163, 255, 0.2) !important;
        transition: all 0.3s ease;
    }}

    .stButton button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(0, 163, 255, 0.3) !important;
    }}

    /* 9. Hide Sidebar */
    [data-testid="stSidebar"] {{ display: none !important; }}
    [data-testid="collapsedControl"] {{ display: none !important; }}
    
    /* 10. Modern Preview Expander */
    .streamlit-expanderHeader {{
        background: rgba(240, 249, 251, 0.8) !important;
        border: 1px solid #bae6fd !important;
        border-radius: 15px !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
    }}
    
    /* Micro-animations */
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    
    div[data-testid="stVerticalBlock"] > div {{
        animation: fadeIn 0.6s ease-out forwards;
    }}
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# MAIN DASHBOARD
# -----------------------------------------------------------------------------

# Header with Logo
if LOGO_BASE64:
    st.markdown(f"""
        <div style="display: flex; justify-content: center; margin-bottom: 25px;">
            <div style="background: white; padding: 15px; border-radius: 50%; 
                        box-shadow: 0 10px 25px rgba(0, 100, 255, 0.15); 
                        width: 130px; height: 130px; display: flex; align-items: center; justify-content: center;">
                <img src="data:image/jpeg;base64,{LOGO_BASE64}" width="90" style="border-radius: 5px;">
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="brand-header">
        <h1 class="brand-title">Globium Cloud</h1>
        <div class="brand-subtitle">Enterprise-Grade Dispatch System</div>
    </div>
""", unsafe_allow_html=True)

# Dashboard Status
is_connected = bool(SENDER_EMAIL and SENDER_APP_PASSWORD)
col_stat1, col_stat2 = st.columns(2)

with col_stat1:
    st.markdown(f"""
        <div style="background: rgba({'34, 197, 94' if is_connected else '239, 68, 68'}, 0.1); 
                    border: 1px solid rgba({'34, 197, 94' if is_connected else '239, 68, 68'}, 0.2); 
                    padding: 1.2rem; border-radius: 15px; text-align: center;">
            <div style="font-size: 0.8rem; color: #15803d; font-weight: 700; text-transform: uppercase;">System Status</div>
            <div style="font-size: 1.1rem; color: #166534; font-weight: 600;">{'🟢 Connected' if is_connected else '🔴 Disconnected'}</div>
        </div>
    """, unsafe_allow_html=True)

with col_stat2:
    st.markdown(f"""
        <div style="background: rgba(0, 163, 255, 0.1); border: 1px solid rgba(0, 163, 255, 0.2); 
                    padding: 1.2rem; border-radius: 15px; text-align: center;">
            <div style="font-size: 0.8rem; color: #0369a1; font-weight: 700; text-transform: uppercase;">Active Entity</div>
            <div style="font-size: 1.1rem; color: #075985; font-weight: 600;">🏢 {COMPANY_NAME}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Manage Session State for Inputs
if 'email_to' not in st.session_state: st.session_state.email_to = ""
if 'email_subject' not in st.session_state: st.session_state.email_subject = ""
if 'email_body' not in st.session_state: st.session_state.email_body = ""

# Main Form
col1, col2 = st.columns([3, 1])
with col1:
    receiver_email = st.text_input("📧 Recipient Email Address", placeholder="Enter official email...", key="email_to")
with col2:
    if receiver_email:
        valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', receiver_email) is not None
        st.markdown(f"<div style='height: 3.6rem; display: flex; align-items: flex-end;'><p style='color: {'#166534' if valid else '#991b1b'}; font-weight: 600;'>{'✅ Valid' if valid else '❌ Invalid'}</p></div>", unsafe_allow_html=True)
    else:
        st.markdown("<div style='height: 3.6rem;'></div>", unsafe_allow_html=True)

subject = st.text_input("🗞️ Campaign Subject Line", placeholder="What is this email about?", key="email_subject")
message = st.text_area("✍️ Message Body", placeholder="Craft your message here... HTML is supported.", height=300, key="email_body")

# Preview
if message:
    with st.expander("👁️ Live Branding Preview", expanded=False):
        preview_html = get_email_template(message, COMPANY_NAME, COMPANY_ADDRESS, COMPANY_WEBSITE, LOGO_BASE64)
        st.components.v1.html(preview_html, height=500, scrolling=True)

st.divider()

# Dispatch
if st.button("🚀 Dispatch Campaign"):
    if not is_connected:
        st.error("System disconnected. Check .env credentials.")
    elif not receiver_email or not is_valid_email(receiver_email):
        st.error("Invalid recipient email.")
    elif not subject or not message:
        st.warning("Subject and Message cannot be empty.")
    else:
        with st.status("Transmitting...", expanded=True) as status:
            try:
                msg = MIMEMultipart('alternative')
                msg['From'] = f"{COMPANY_NAME} <{SENDER_EMAIL.strip()}>"
                msg['To'] = receiver_email
                msg['Subject'] = subject
                
                html_content = get_email_template(message, COMPANY_NAME, COMPANY_ADDRESS, COMPANY_WEBSITE, LOGO_BASE64)
                msg.attach(MIMEText(html_content, 'html'))
                
                with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as server:
                    server.login(SENDER_EMAIL.strip(), SENDER_APP_PASSWORD.strip().replace(" ", ""))
                    server.send_message(msg)
                
                status.update(label="Dispatched Successfully", state="complete", expanded=False)
                st.success(f"✅ Sent to {receiver_email}")
                st.balloons()
                
                # Clear inputs after success
                st.session_state.email_to = ""
                st.session_state.email_subject = ""
                st.session_state.email_body = ""
                
                # Allow user to see the success message for 2 seconds then rerun to clear
                import time
                time.sleep(2)
                st.rerun()
                
            except Exception as e:
                status.update(label="Dispatch Failed", state="error")
                st.error(f"❌ Error: {str(e)}")

# Footer
st.markdown(f"""
    <div style="text-align: center; margin-top: 4rem; padding-bottom: 2rem;">
        <p style="color: #64748b; font-size: 0.9rem;">
            Powered by <b>{COMPANY_NAME}</b> • Enterprise Dispatcher
        </p>
    </div>
""", unsafe_allow_html=True)
