#!/usr/bin/env bash
# Quick launcher for VyaparDost AI
cd "$(dirname "$0")"

echo "=========================================================="
echo "  🇮🇳 Launching VyaparDost AI for Google Build with AI..."
echo "=========================================================="

source venv/bin/activate
streamlit run app.py --server.port 8501 --server.headless false
