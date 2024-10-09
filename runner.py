import sys
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "Aplicativo web.py"]
sys.exit(stcli.main())