from flask import Flask, render_template_string
import subprocess
import pytz
from datetime import datetime
import getpass

app = Flask(__name__)

@app.route('/htop')
def htop():
   
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f %Z')

  
    username = getpass.getuser()
    
   
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
   
    html_template = """
    <pre>
Name: Muzammil Muzaffar
user: {{ username }}
Server Time (IST): {{ server_time }}
TOP output:

{{ top_output }}
    </pre>
    """
    
    return render_template_string(html_template, username=username, server_time=server_time, top_output=top_output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
