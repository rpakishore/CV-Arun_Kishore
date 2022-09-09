cd /D "%~dp0"
@echo Started: %date% %time%
"venv\Scripts\activate.bat" && python -m streamlit run Curriculum_Vitae.py