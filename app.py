from flask import Flask, render_template, request
from fetch import create_adverse_events_chart
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('viz.html')


@app.route('/generate_chart', methods=['POST'])
def generate_chart():
    # Get selected checkboxes from the request
    chart_types = request.json

    # Generate the chart based on selected types
    chart_html = create_adverse_events_chart(chart_types)
    return chart_html


if __name__ == '__main__':
    serve(app)