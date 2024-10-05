# py-chatbot
 
Install PIP
https://pip.pypa.io/en/stable/installation/

Install py-chatbot
pip install git+https://github.com/Mahes2/py-chatbot.git

Install Cert
CERT_PATH=$(python3 -m certifi)
export SSL_CERT_FILE=${CERT_PATH}
export REQUESTS_CA_BUNDLE=${CERT_PATH}

Run main.py
python main.py