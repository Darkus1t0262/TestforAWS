from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head><title>Frontend</title></head>
    <body>
        <h1>Welcome to the Python Frontend!</h1>
        <p>This is served by Flask.</p>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
