from flask import flask,jsonify
app=flask(__name__)

students = [
    {"id": 1, "name": "Alice",   "grade": "A"},
    {"id": 2, "name": "Bob",     "grade": "B+"},
    {"id": 3, "name": "Charlie", "grade": "A+"},
]

@app.route('/')
def home ():
    return '''
      <html>
    <head>
        <title>DevOps Demo App</title>
        <style>
            body { font-family: Arial; text-align: center; margin-top: 80px; background: #f0f4f8; }
            h1   { color: #2d3748; }
            p    { color: #718096; }
            .badge { background: #48bb78; color: white; padding: 6px 16px; border-radius: 20px; }
        </style>
    </head>
    <body>
        <h1>🚀 DevOps Pipeline Demo</h1>
        <p>Flask App running inside <span class="badge">Docker</span></p>
        <p>Built by Jenkins CI/CD Pipeline</p>
        <p><a href="/students">View Students API →</a></p>
    </body>
    </html>
    '''
@app.route('/student')
def get_student():
    return jsonify({
        "status":"success".
        "count": len(students),
        "data": students
    })
@app.route('/health')
def health():
    return jsonify({"student":"healty"})

if __name__= '__main__':
    app.run(host:'0.0.0.0',port:5000,debug=false)
    