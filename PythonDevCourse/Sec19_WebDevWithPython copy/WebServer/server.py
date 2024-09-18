from flask import Flask, render_template
app = Flask(__name__)
# print(__name__)


@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):
    return render_template('index.html', name=username, post_id=post_id)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return 'Today I have not done much, mostly wasted my time watching shitty short videos on social media app.'


@app.route('/blog/2024/dogs')
def blog2():
    return 'My pet dog name was dogya, now he is no more. He was really cute and agressive dog and I miss him very much.'


if __name__ == '__main__':
    app.run(debug=True)
