from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 가짜 사용자 인증
users = {"user1": "pass1", "admin": "admin123"}

# 샘플 투두 데이터 (카테고리별 항목들)
todo_data = {
    '마음': {
        'icon': '❤️',
        'tasks': ['명상 10분 하기', '감사일기 작성하기', '긍정적인 생각 유지하기'],
        'checked': [True, False, False]
    },
    '공부': {
        'icon': '⭐',
        'tasks': ['프로그래밍 강의 듣기', '영어 단어 30개 외우기', '알고리즘 문제 풀기', '프로젝트 계획 세우기'],
        'checked': [True, False, False, False]
    },
    '운동': {
        'icon': '🏃‍♀️',
        'tasks': ['아침 조깅 30분', '스트레칭 10분', '근력 운동 20분'],
        'checked': [True, False, False]
    }
}


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username'] = username
        return redirect(url_for('todo'))  # ✅ 로그인 성공 시 투두페이지로 이동
    else:
        return "로그인 실패"


@app.route('/todo', methods=['GET', 'POST'])
def todo():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('test.html', todos=todo_data)

    if request.method == 'POST':
        task = request.form['task']
        session.setdefault('tasks', []).append(task)

    tasks = session.get('tasks', [])
    return render_template('todo.html', tasks=tasks)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
