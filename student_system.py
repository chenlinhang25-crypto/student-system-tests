"""
学生成绩管理系统 - 有 Bug 的版本
运行：python student_system.py
"""

from flask import Flask, request, jsonify

app = Flask(__name__)
students = {}


@app.route('/')
def index():
    return {
        "message": "学生成绩管理系统",
        "apis": [
            "POST /student - 添加学生",
            "GET  /student/<id> - 查询学生",
            "POST /score - 录入成绩",
            "GET  /score/<id> - 查询成绩",
            "GET  /average/<id> - 计算平均分"
        ]
    }


@app.route('/student', methods=['POST'])
def add_student():
    """Bug 1: 没校验重复"""
    data = request.get_json()
    student_id = data.get('id')
    name = data.get('name')

    students[student_id] = {
        'id': student_id,
        'name': name,
        'scores': {}
    }

    return jsonify({'code': 0, 'message': '添加成功'})


@app.route('/student/<student_id>', methods=['GET'])
def get_student(student_id):
    """Bug 2: 404 返回 200"""
    student = students.get(student_id)

    if not student:
        return jsonify({'code': 404, 'message': '学生不存在'}), 200

    return jsonify({'code': 0, 'data': student})


@app.route('/score', methods=['POST'])
def add_score():
    """Bug 3: 分数可以超过 100"""
    data = request.get_json()
    student_id = data.get('student_id')
    subject = data.get('subject')
    score = data.get('score')

    if student_id not in students:
        return jsonify({'code': 404, 'message': '学生不存在'}), 404

    students[student_id]['scores'][subject] = score

    return jsonify({'code': 0, 'message': '录入成功'})


@app.route('/score/<student_id>', methods=['GET'])
def get_scores(student_id):
    """Bug 4: 没处理无成绩的情况"""
    if student_id not in students:
        return jsonify({'code': 404, 'message': '学生不存在'}), 404

    scores = students[student_id]['scores']
    return jsonify({'code': 0, 'data': scores})


@app.route('/average/<student_id>', methods=['GET'])
def get_average(student_id):
    """Bug 5: 除零错误"""
    if student_id not in students:
        return jsonify({'code': 404, 'message': '学生不存在'}), 404

    scores = students[student_id]['scores']

    total = sum(scores.values())
    average = total / len(scores)  # 除零错误！

    return jsonify({
        'code': 0,
        'data': {'average': round(average, 2), 'count': len(scores)}
    })


if __name__ == '__main__':
    print("访问: http://127.0.0.1:5001")
    app.run(host='127.0.0.1', port=5001, debug=True)