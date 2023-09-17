import logging
from flask import Flask, render_template, request, abort
from fetch import create_adverse_events_chart
from waitress import serve

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
        if chart_html == 'no data':
            logging.warning('No data found for the selected criteria')
            return render_template('no_data.html')
        
        logging.info('Chart generated successfully')
        return chart_html
    except Exception as e:
        logging.error(f'An error has occuews: {str(e)}')
        abort(500)


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    serve(app)