from flask import Flask, render_template, request, abort
from fetch import create_adverse_events_chart
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('viz.html')


@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    # Get selected checkboxes from the request
    userChoices = request.json

    # Generate the chart based on selected types
    try:
        chart_html = create_adverse_events_chart(userChoices)
        return chart_html
    except Exception:
        abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    #serve(app)
    app.run(debug=True)