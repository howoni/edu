from flask import Flask, render_template, request, g, redirect
from flask_cors import CORS
from dbc import BoardDB
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def set_chrome_options() -> Options:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

FLAG ='FLAG{SECRET IS MUST BE SECRET}'
app = Flask(__name__)
app.config['DATABASE'] = 'example.db'

CORS(app, resources={r"/*": {"origins": "localhost"}})

def callbot(num):
    driver = webdriver.Chrome(options=set_chrome_options())
    url = f'http://localhost:5001/board/{num}'
    e = driver.get(url)
    time.sleep(4)
    driver.quit()

def get_db():
    if 'db' not in g:
        g.db = BoardDB(app.config['DATABASE'])
    return g.db

def xss_filter(data):
    return data.replace('<', '&lt;').replace('>','&gt;')

with app.app_context():
    def init_db():
        db = get_db()
        db.init_board_table()

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def board_list():
    db = get_db()
    rows = db.get_all_boards()
    return render_template('board_list.html', rows=rows)

@app.route('/board/write')
def board_write():
    return render_template('board_write.html')

@app.route('/board/write_process', methods=['POST'])
def board_write_process():
    title = request.form['title']
    content = request.form['content']
    db = get_db()
    num = db.insert_board(title, xss_filter(content))
    callbot(num)
    return redirect('/')

@app.route('/board/<int:id>')
def board_detail(id):
    db = get_db()
    row = db.get_board_by_id(id)
    return render_template('board_detail.html', row=row)

@app.route('/flag')
def flag():
    print(request.remote_addr)#for debug
    if request.remote_addr == "127.0.0.1":
        return FLAG
    else:
        return "Access denied"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
