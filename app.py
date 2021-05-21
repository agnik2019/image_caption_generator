from flask import Flask, render_template, request
import caption_it

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/', methods = ['POST'])
def cap():
    if request.method == 'POST':
        f = request.files['userfile']
        path = "./static/{}".format(f.filename)
        f.save(path)

    caption = caption_it.caption_this_image(path)
    result_dic = {
        'image':path,
        'caption': caption
    }

    return render_template("index.html", your_result = result_dic )

if __name__ == '__main__':
    app.run(debug = True)