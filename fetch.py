import requests
import plotly.graph_objects as go


def create_adverse_events_chart(chart_types):
    base_url = 'https://api.fda.gov/drug/event.json'
    url2 = base_url + '?search=receivedate:[20040101+TO+20230829]&count=patient.drug.drugindication.exact'
    response = requests.get(url2)
    data = response.json()

    drug_names = [entry['term'] for entry in data['results']]
    event_counts = [entry['count'] for entry in data['results']]

    # Create a list to store traces based on selected chart types
    chart_traces = []

    if chart_types.get('bar'):
        # Add Bar chart trace
        chart_traces.append(go.Bar(x=drug_names, y=event_counts, name='Bar'))

    if chart_types.get('histogram'):
        # Add Histogram chart trace
        chart_traces.append(go.Histogram(x=event_counts, name='Histogram'))

    if chart_types.get('pie'):
        # Add Pie chart trace
        chart_traces.append(go.Pie(labels=drug_names, values=event_counts, name='Pie'))

    # Create a Plotly figure using the selected traces
    fig = go.Figure(chart_traces)

    # Customize the chart layout
    fig.update_layout(title='Adverse Events by Drug Indication',
                      xaxis_title='Drug Indication',
                      yaxis_title='Number of Adverse Events')

    return fig.to_html()