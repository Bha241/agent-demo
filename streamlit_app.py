import streamlit as st
import requests
import pandas as pd
import os

# Configure the Backend API URL (useful for Docker & Azure deployments)
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")


# Set page configuration with wide layout
st.set_page_config(
    page_title="AI Investment Research System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom premium styling via markdown
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #2563EB;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar - Agent system description
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.markdown("### 🤖 Agentic Architecture")
    st.write(
        "This Investment Research System orchestrates 8 specialized AI Agents using **LangGraph**:"
    )
    st.markdown("""
    * **Planner Agent**: Structures research goals.
    * **Researcher Agent**: Collects market and financial data.
    * **Financial Analyst**: Evaluates financial statements.
    * **Sentiment Agent**: Assesses market news.
    * **Validation Node**: Audits data integrity.
    * **Risk Assessor**: Inspects regulatory & promoter risk.
    * **Report Writer**: Drafts the investment thesis.
    * **Report Reviewer**: Audits reports for accuracy.
    """)
    st.markdown("---")
    st.caption("Backend running on FastAPI & Groq (Llama-3.1-8B)")

# Main Header
st.markdown('<div class="main-header">📊 AI Investment Research System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Programmatic multi-agent equity analysis for Indian equities</div>', unsafe_allow_html=True)

# Input parameters
company_input = st.text_input("Enter Indian Company Name (e.g., SBI, Reliance, Infosys, Wipro, TCS):", value="sbi")

# Research Trigger
if st.button("🚀 Analyze & Generate Report", type="primary"):
    company_query = company_input.strip().lower()
    
    with st.spinner("Our AI agents are analyzing stock prices, compiling news, auditing financial statements, and assessing investment risks... This may take up to a minute."):
        try:
            # Call local or configured FastAPI server
            response = requests.post(f"{BACKEND_URL}/research?company={company_query}", timeout=240)
            
            if response.status_code == 200:
                result = response.json()
                
                # Retrieve individual agent data from LangGraph state output
                company_info = result.get("company", {})
                stock_price = result.get("stock_price", {})
                financials = result.get("financials", {})
                news = result.get("news", [])
                sentiment_info = result.get("sentiment", {})
                risks_info = result.get("risks", {})
                report = result.get("report", "")
                
                # Check if company resolved successfully
                if not company_info:
                    st.warning(f"Could not resolve info for '{company_input}'. Please make sure it is in our supported Indian companies list.")
                
                # Display metrics summary at the top
                st.markdown("### ⚡ Live Market Snapshot")
                col1, col2, col3, col4 = st.columns(4)
                if stock_price:
                    col1.metric("Current Price", f"₹ {stock_price.get('Current Price', 'N/A')}")
                    col2.metric("Previous Close", f"₹ {stock_price.get('Previous Close', 'N/A')}")
                    col3.metric("Open", f"₹ {stock_price.get('Open', 'N/A')}")
                    col4.metric("Day High", f"₹ {stock_price.get('Day High', 'N/A')}")
                else:
                    st.write("Live market price not available.")
                
                # Create tabs for interactive output
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "📄 Investment Report", 
                    "🏢 Company Profile", 
                    "📈 Financial Statements", 
                    "📰 News & Sentiment", 
                    "⚠️ Risk Analysis"
                ])
                
                # Tab 1: Final Report
                with tab1:
                    st.markdown("### 📋 Final Investment Thesis")
                    if report:
                        st.markdown(report)
                    else:
                        st.write("No report drafted.")
                        
                # Tab 2: Profile
                with tab2:
                    st.markdown("### 🏢 Corporate Information")
                    if company_info:
                        st.write(f"**Company:** {company_info.get('Company', 'N/A')}")
                        st.write(f"**Sector:** {company_info.get('Sector', 'N/A')}")
                        st.write(f"**Industry:** {company_info.get('Industry', 'N/A')}")
                        st.write(f"**Country:** {company_info.get('Country', 'N/A')}")
                        st.write(f"**Employees:** {company_info.get('Employees', 'N/A')}")
                        st.write(f"**Website:** {company_info.get('Website', 'N/A')}")
                        st.markdown(f"**Business Overview:**\n{company_info.get('Summary', 'N/A')}")
                    else:
                        st.write("Company profile data not found.")
                        
                # Tab 3: Financials
                with tab3:
                    st.markdown("### 📈 Historical Financial Statements")
                    if financials:
                        statement_type = st.selectbox("Select Statement:", ["Income Statement", "Balance Sheet", "Cash Flow"])
                        
                        stmt_dict = {}
                        if statement_type == "Income Statement":
                            stmt_dict = financials.get("income_statement", {})
                        elif statement_type == "Balance Sheet":
                            stmt_dict = financials.get("balance_sheet", {})
                        else:
                            stmt_dict = financials.get("cashflow", {})
                            
                        if stmt_dict:
                            df = pd.DataFrame(stmt_dict)
                            st.dataframe(df, use_container_width=True)
                        else:
                            st.write("Financial statement values not available.")
                    else:
                        st.write("No financials statement found.")
                        
                # Tab 4: News & Sentiment
                with tab4:
                    st.markdown("### 📰 Sentiment & Media Analysis")
                    if sentiment_info:
                        st.markdown("#### Sentiment Score & Analysis")
                        st.write(sentiment_info.get("analysis", "No analysis content."))
                    
                    st.markdown("---")
                    st.markdown("#### Retrieved Media Articles")
                    if news:
                        for idx, article in enumerate(news):
                            st.markdown(f"**{idx+1}. {article.get('title', 'Market Announcement')}**")
                            st.write(article.get("body", "No description available."))
                            if "href" in article:
                                st.write(f"[Read Article]({article['href']})")
                            st.markdown("---")
                    else:
                        st.write("No recent news fetched.")
                        
                # Tab 5: Risk
                with tab5:
                    st.markdown("### ⚠️ Agentic Risk Assessment")
                    if risks_info:
                        st.write(risks_info.get("analysis", "No risk analysis generated."))
                    else:
                        st.write("No risk analysis available.")
                        
            else:
                st.error(f"Backend Server Error: Status Code {response.status_code}")
                st.write(response.text)
                
        except requests.exceptions.ConnectionError:
            st.error("🔌 Connection Failed!")
            st.write(
                f"Could not connect to the FastAPI backend at `{BACKEND_URL}`. "
                "Please make sure your FastAPI backend is running (e.g. by running `uvicorn api.app:app` in your terminal)."
            )
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
