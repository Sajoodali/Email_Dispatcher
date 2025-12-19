# import streamlit as st
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# import re
# from email_template import get_email_template
# import os
# from dotenv import load_dotenv
# import base64

# # Load environment variables
# load_dotenv()

# # Page configuration
# st.set_page_config(
#     page_title="Globium Cloud | Dispatcher",
#     page_icon="📨",
#     layout="centered", 
#     initial_sidebar_state="collapsed"
# )

# # Load configuration from .env
# SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
# SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "")
# COMPANY_NAME = os.getenv("COMPANY_NAME", "Globium Cloud")
# COMPANY_ADDRESS = os.getenv("COMPANY_ADDRESS", "Official Business Address")
# COMPANY_WEBSITE = os.getenv("COMPANY_WEBSITE", "www.globiumcloud.com")

# # Helper: Load and encode logo
# def get_base64_logo(file_path):
#     try:
#         with open(file_path, "rb") as f:
#             data = f.read()
#             return base64.b64encode(data).decode()
#     except:
#         return None

# LOGO_BASE64 = get_base64_logo("GC-Logo.jpg")

# def is_valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#     return re.match(pattern, email) is not None

# # -----------------------------------------------------------------------------
# # PREMIUM GLOBIUM CLOUD THEME (Responsive & Blue)
# # -----------------------------------------------------------------------------
# st.markdown(f"""
#     <style>
#     /* 1. Global Reset & Modern Typography */
#     @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap');
    
#     html, body, [class*="css"] {{
#         font-family: 'Plus Jakarta Sans', sans-serif;
#         font-size: 16px;
#         color: #e2e8f0;
#     }}

#     /* 2. Enhanced Premium Dark Background */
#     .stApp {{
#         background: 
#             radial-gradient(at 0% 0%, hsla(222, 47%, 11%, 1) 0, transparent 50%), 
#             radial-gradient(at 100% 0%, hsla(210, 40%, 15%, 1) 0, transparent 50%), 
#             radial-gradient(at 50% 100%, hsla(222, 47%, 10%, 1) 0, transparent 50%),
#             #0f172a;
#         background-attachment: fixed;
#     }}
    
#     /* 3. Responsive & Centered Container */
#     .block-container {{
#         padding-top: 4rem !important;
#         padding-bottom: 6rem !important;
#         max-width: 800px !important;
#     }}
    
#     @media (max-width: 768px) {{
#         .block-container {{
#             padding-top: 2rem !important;
#             padding-bottom: 4rem !important;
#             max-width: 100% !important;
#         }}
#     }}

#     /* 4. Elegant Header Section */
#     .brand-header {{
#         text-align: center;
#         margin-bottom: 4rem;
#         animation: fadeInDown 0.8s ease-out;
#     }}
    
#     .brand-title {{
#         background: linear-gradient(135deg, #f8fafc 0%, #94a3b8 100%);
#         -webkit-background-clip: text;
#         -webkit-text-fill-color: transparent;
#         font-family: 'Outfit', sans-serif;
#         font-size: clamp(2.5rem, 6vw, 4.5rem) !important;
#         font-weight: 800 !important;
#         letter-spacing: -0.04em;
#         margin-bottom: 0.5rem;
#         line-height: 1.1;
#     }}
    
#     .brand-subtitle {{
#         color: #94a3b8;
#         font-size: clamp(0.8rem, 2vw, 1.1rem) !important;
#         font-weight: 600;
#         text-transform: uppercase;
#         letter-spacing: 0.15em;
#     }}

#     /* 5. Modern Glass Cards (Dark) */
#     div[data-testid="stVerticalBlock"] > div:has(div.stTextInput),
#     div[data-testid="stVerticalBlock"] > div:has(div.stTextArea) {{
#         background: rgba(30, 41, 59, 0.7);
#         backdrop-filter: blur(24px);
#         -webkit-backdrop-filter: blur(24px);
#         padding: 2.5rem;
#         border-radius: 28px;
#         box-shadow: 
#             0 4px 20px -2px rgba(0, 0, 0, 0.3), 
#             0 0 0 1px rgba(255, 255, 255, 0.05) inset;
#         border: 1px solid rgba(255, 255, 255, 0.08);
#         margin-bottom: 1.5rem;
#         transition: all 0.3s ease;
#     }}
    
#     @media (max-width: 768px) {{
#         div[data-testid="stVerticalBlock"] > div:has(div.stTextInput),
#         div[data-testid="stVerticalBlock"] > div:has(div.stTextArea) {{
#             padding: 1.5rem !important;
#             border-radius: 20px !important;
#         }}
        
#         .brand-header {{ margin-bottom: 2rem !important; }}
#     }}
    
#     div[data-testid="stVerticalBlock"] > div:has(div.stTextInput):hover,
#     div[data-testid="stVerticalBlock"] > div:has(div.stTextArea):hover {{
#         transform: translateY(-2px);
#         box-shadow: 
#             0 12px 30px -5px rgba(0, 0, 0, 0.4),
#             0 0 0 1px rgba(255, 255, 255, 0.1) inset;
#         background: rgba(30, 41, 59, 0.8);
#     }}

#     /* 6. Refined Inputs (Dark) */
#     .stTextInput input, .stTextArea textarea {{
#         background: #020617 !important;
#         border: 1px solid #334155 !important;
#         border-radius: 16px !important;
#         padding: 1.1rem 1.4rem !important;
#         font-size: 1.05rem !important;
#         font-family: 'Plus Jakarta Sans', sans-serif !important;
#         color: #f1f5f9 !important;
#         transition: all 0.2s ease;
#     }}

#     .stTextInput input:focus, .stTextArea textarea:focus {{
#         border-color: #3b82f6 !important;
#         box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.2) !important;
#         transform: translateY(-1px);
#     }}
    
#     .stTextInput label, .stTextArea label {{
#         font-size: 0.9rem !important;
#         font-weight: 700 !important;
#         color: #94a3b8 !important;
#         margin-bottom: 0.6rem !important;
#         text-transform: uppercase;
#         letter-spacing: 0.05em;
#     }}

#     /* 7. Primary Action Button (Dark) */
#     .stButton button {{
#         background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
#         color: white !important;
#         font-weight: 700 !important;
#         padding: 1.1rem 3rem !important;
#         border-radius: 18px !important;
#         border: none !important;
#         width: 100% !important;
#         font-size: 1.15rem !important;
#         letter-spacing: 0.02em !important;
#         box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3) !important;
#         transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
#     }}

#     .stButton button:hover {{
#         transform: translateY(-3px);
#         box-shadow: 0 20px 30px -8px rgba(37, 99, 235, 0.4) !important;
#         background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%) !important;
#     }}
    
#     .stButton button:active {{
#         transform: translateY(-1px);
#     }}

#     /* 9. Utility & Hiding */
#     [data-testid="stSidebar"] {{ display: none !important; }}
#     [data-testid="collapsedControl"] {{ display: none !important; }}
    
#     /* 10. Expander Customization (Dark) */
#     .streamlit-expanderHeader {{
#         background: rgba(30, 41, 59, 0.6) !important;
#         border: 1px solid #334155 !important;
#         border-radius: 14px !important;
#         color: #cbd5e1 !important;
#         font-weight: 600 !important;
#         font-size: 1rem !important;
#     }}
    
#     /* Animations */
#     @keyframes fadeInDown {{
#         from {{ opacity: 0; transform: translateY(-20px); }}
#         to {{ opacity: 1; transform: translateY(0); }}
#     }}
    
#     @keyframes fadeInUp {{
#         from {{ opacity: 0; transform: translateY(20px); }}
#         to {{ opacity: 1; transform: translateY(0); }}
#     }}
    
#     div[data-testid="stVerticalBlock"] > div {{
#         animation: fadeInUp 0.6s ease-out forwards;
#     }}
#     </style>
# """, unsafe_allow_html=True)

# # -----------------------------------------------------------------------------
# # MAIN DASHBOARD
# # -----------------------------------------------------------------------------

# # Header with Logo
# if LOGO_BASE64:
#     st.markdown(f"""
#         <div style="display: flex; justify-content: center; margin-bottom: 25px;">
#             <div style="background: white; padding: 15px; border-radius: 50%; 
#                         box-shadow: 0 10px 25px rgba(0, 100, 255, 0.15); 
#                         width: 130px; height: 130px; display: flex; align-items: center; justify-content: center;">
#                 <img src="data:image/jpeg;base64,{LOGO_BASE64}" width="90" style="border-radius: 5px;">
#             </div>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("""
#     <div class="brand-header">
#         <h1 class="brand-title">Globium Cloud</h1>
#         <div class="brand-subtitle">Enterprise-Grade Dispatch System</div>
#     </div>
# """, unsafe_allow_html=True)

# # Dashboard Status
# is_connected = bool(SENDER_EMAIL and SENDER_APP_PASSWORD)
# col_stat1, col_stat2 = st.columns(2)


# with col_stat1:
#     st.markdown(f"""
#         <div style="background: rgba(30, 41, 59, 1); 
#                     box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
#                     border: 1px solid #334155;
#                     padding: 1rem; border-radius: 16px; text-align: center;
#                     display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
#             <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.2rem;">System Status</div>
#             <div style="display: flex; align-items: center; gap: 0.5rem;">
#                 <span style="height: 8px; width: 8px; background-color: {'#4ade80' if is_connected else '#ef4444'}; border-radius: 50%; display: inline-block;"></span>
#                 <span style="font-size: 1rem; color: {'#4ade80' if is_connected else '#ef4444'}; font-weight: 600;">{'System Online' if is_connected else 'Disconnected'}</span>
#             </div>
#         </div>
#     """, unsafe_allow_html=True)


# with col_stat2:
#     st.markdown(f"""
#         <div style="background: rgba(30, 41, 59, 1); 
#                     box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
#                     border: 1px solid #334155;
#                     padding: 1rem; border-radius: 16px; text-align: center;
#                      display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%;">
#             <div style="font-size: 0.75rem; color: #94a3b8; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.2rem;">Active Entity</div>
#             <div style="font-size: 1rem; color: #f8fafc; font-weight: 600;">{COMPANY_NAME}</div>
#         </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)

# # Manage Session State for Inputs
# if 'email_to' not in st.session_state: st.session_state.email_to = ""
# if 'email_subject' not in st.session_state: st.session_state.email_subject = ""
# if 'email_body' not in st.session_state: st.session_state.email_body = ""

# # Main Form
# receiver_email = st.text_input("📧 Recipient Email Address", placeholder="Enter official email...", key="email_to")

# if receiver_email:
#     valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', receiver_email) is not None
#     validation_color = "#22c55e" if valid else "#ef4444"
#     validation_msg = "✅ Valid Email Address" if valid else "❌ Invalid Email Format"
#     st.caption(f"<span style='color: {validation_color}; font-weight: 600;'>{validation_msg}</span>", unsafe_allow_html=True)
# else:
#     st.caption("Please enter a valid recipient email address.")

# subject = st.text_input("🗞️ Campaign Subject Line", placeholder="What is this email about?", key="email_subject")
# message = st.text_area("✍️ Message Body", placeholder="Craft your message here... HTML is supported.", height=300, key="email_body")

# # Preview
# if message:
#     with st.expander("👁️ Live Branding Preview", expanded=False):
#         preview_html = get_email_template(message, COMPANY_NAME, COMPANY_ADDRESS, COMPANY_WEBSITE, LOGO_BASE64)
#         st.components.v1.html(preview_html, height=500, scrolling=True)

# st.divider()

# # Dispatch
# if st.button("🚀 Dispatch Campaign"):
#     if not is_connected:
#         st.error("System disconnected. Check .env credentials.")
#     elif not receiver_email or not is_valid_email(receiver_email):
#         st.error("Invalid recipient email.")
#     elif not subject or not message:
#         st.warning("Subject and Message cannot be empty.")
#     else:
#         with st.status("Transmitting...", expanded=True) as status:
#             try:
#                 msg = MIMEMultipart('alternative')
#                 msg['From'] = f"{COMPANY_NAME} <{SENDER_EMAIL.strip()}>"
#                 msg['To'] = receiver_email
#                 msg['Subject'] = subject
                
#                 html_content = get_email_template(message, COMPANY_NAME, COMPANY_ADDRESS, COMPANY_WEBSITE, LOGO_BASE64)
#                 msg.attach(MIMEText(html_content, 'html'))
                
#                 with smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=15) as server:
#                     server.login(SENDER_EMAIL.strip(), SENDER_APP_PASSWORD.strip().replace(" ", ""))
#                     server.send_message(msg)
                
#                 status.update(label="Dispatched Successfully", state="complete", expanded=False)
#                 st.success(f"✅ Sent to {receiver_email}")
#                 st.balloons()
                
#                 # Clear inputs after success
#                 st.session_state.email_to = ""
#                 st.session_state.email_subject = ""
#                 st.session_state.email_body = ""
                
#                 # Allow user to see the success message for 2 seconds then rerun to clear
#                 import time
#                 time.sleep(2)
#                 st.rerun()
                
#             except Exception as e:
#                 status.update(label="Dispatch Failed", state="error")
#                 st.error(f"❌ Error: {str(e)}")

# # Footer
# st.markdown(f"""
#     <div style="text-align: center; margin-top: 4rem; padding-bottom: 2rem;">
#         <p style="color: #64748b; font-size: 0.9rem;">
#             Powered by <b>{COMPANY_NAME}</b> • Enterprise Dispatcher
#         </p>
#     </div>
# """, unsafe_allow_html=True)




import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
from email_template import get_email_template
import os
from dotenv import load_dotenv
import base64
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Globium Cloud | Dispatcher",
    page_icon="📨",
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# --- CONFIGURATION ---
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "")
COMPANY_NAME = os.getenv("COMPANY_NAME", "Globium Cloud")
COMPANY_ADDRESS = os.getenv("COMPANY_ADDRESS", "Official Business Address")
COMPANY_WEBSITE = os.getenv("COMPANY_WEBSITE", "www.globiumcloud.com")

# --- HELPER FUNCTIONS ---
def get_base64_logo(file_path):
    try:
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

def is_valid_email(email):
    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

LOGO_BASE64 = get_base64_logo("GC-Logo.jpg")
is_connected = bool(SENDER_EMAIL and SENDER_APP_PASSWORD)

# --- MINIMAL STYLING (Background & Clean up) ---
st.markdown("""
    <style>
    /* Sirf background aur basic coloring k liye global css zaruri hai */
    .stApp {
        background: radial-gradient(at 0% 0%, #0f172a 0, #020617 100%);
        color: #e2e8f0;
    }
    /* Input Fields ko clean look dena */
    .stTextInput input, .stTextArea textarea {
        background-color: rgba(30, 41, 59, 0.5) !important;
        color: white !important;
        border: 1px solid #334155 !important;
    }
    /* Button Styling */
    .stButton button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%) !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
    }
    /* Remove Header/Footer defaults */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- UI HEADER (Inline Styles) ---
if LOGO_BASE64:
    st.markdown(f"""
        <div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <div style="background: white; padding: 10px; border-radius: 50%; width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; box-shadow: 0 0 20px rgba(59, 130, 246, 0.3);">
                <img src="data:image/jpeg;base64,{LOGO_BASE64}" width="70" style="border-radius: 4px;">
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="background: linear-gradient(to right, #f8fafc, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 800; margin: 0;">{COMPANY_NAME}</h1>
        <p style="color: #64748b; font-size: 0.9rem; letter-spacing: 2px; text-transform: uppercase; margin-top: 5px;">Enterprise Dispatcher</p>
    </div>
""", unsafe_allow_html=True)

# --- STATUS CARDS (Inline Styles) ---
col1, col2 = st.columns(2)
with col1:
    status_color = '#4ade80' if is_connected else '#ef4444'
    status_text = 'System Online' if is_connected else 'Disconnected'
    st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.4); border: 1px solid #334155; padding: 15px; border-radius: 12px; text-align: center;">
            <div style="font-size: 0.7rem; color: #94a3b8; text-transform: uppercase; font-weight: bold;">SMTP Status</div>
            <div style="color: {status_color}; font-weight: 600; margin-top: 5px;">● {status_text}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style="background: rgba(30, 41, 59, 0.4); border: 1px solid #334155; padding: 15px; border-radius: 12px; text-align: center;">
            <div style="font-size: 0.7rem; color: #94a3b8; text-transform: uppercase; font-weight: bold;">Active Entity</div>
            <div style="color: white; font-weight: 600; margin-top: 5px;">{COMPANY_NAME}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- FORM LOGIC ---
if 'email_to' not in st.session_state: st.session_state.email_to = ""
if 'email_subject' not in st.session_state: st.session_state.email_subject = ""
if 'email_body' not in st.session_state: st.session_state.email_body = ""

receiver_email = st.text_input("Recipient Email", placeholder="name@example.com", key="email_to")
subject = st.text_input("Subject Line", placeholder="Email Subject...", key="email_subject")
message = st.text_area("Message Body", placeholder="Type your message here (HTML supported)...", height=250, key="email_body")

# --- PREVIEW SECTION ---
if message:
    with st.expander("👁️ Live Preview"):
        preview_html = get_email_template(message, COMPANY_NAME, COMPANY_ADDRESS, COMPANY_WEBSITE, LOGO_BASE64)
        st.components.v1.html(preview_html, height=400, scrolling=True)

st.divider()

# --- SEND LOGIC ---
if st.button("🚀 Dispatch Campaign", use_container_width=True):
    if not is_connected:
        st.error("❌ System disconnected. Check .env file.")
    elif not receiver_email or not is_valid_email(receiver_email):
        st.error("❌ Invalid email format.")
    elif not subject or not message:
        st.warning("⚠️ Subject and Message are required.")
    else:
        with st.status("Transmitting data...", expanded=True) as status:
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
                st.success(f"✅ Email sent to {receiver_email}")
                
                # Clear State & Refresh
                st.session_state.email_to = ""
                st.session_state.email_subject = ""
                st.session_state.email_body = ""
                time.sleep(1.5)
                st.rerun()
                
            except Exception as e:
                status.update(label="Failed", state="error")
                st.error(f"Error: {str(e)}")

# --- FOOTER (Inline Styles) ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; color: #475569; font-size: 0.8rem;">
        Powered by <b>{COMPANY_NAME}</b> System
    </div>
""", unsafe_allow_html=True)