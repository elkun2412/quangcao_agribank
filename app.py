from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="static")

@app.route("/")
def slideshow():
    return render_template("slideshow.html")

# Nếu vẫn lỗi, thêm route để kiểm tra file trực tiếp
@app.route("/static/videos/<path:filename>")
def serve_video(filename):
    return send_from_directory("static/videos", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)