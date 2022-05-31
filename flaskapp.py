from flask import Flask ,send_from_directory
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER']='/home/githubaccount/mysite'


@app.route('/uploads', methods=['GET', 'POST'])
def download():
    filename="DowellWifi.exe"
    print(app.root_path)
    full_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
    print(full_path)
    return send_from_directory(full_path, filename)
