import requests
import plotly.graph_objects as go


def create_adverse_events_chart(userChoices):
    # Construct the url to retrieve the data from user choices
    base_url = 'https://api.fda.gov/drug/event.json'
    
    # check if drug is selected
    if userChoices['drug'] != "":
        url2search = base_url + f'?search=patient.drug.openfda.generic_name:"{userChoices["drug"]}"&count=patient.reaction.reactionmeddrapt.exact&limit=20'

        response = requests.get(url2search)
        data = response.json()

        adverse_events = [entry['term'] for entry in data['results']]
        event_counts = [entry['count'] for entry in data['results']]
    
        chart_traces = []
        chart_type = userChoices['chartType']

        if chart_type == 'Bar Chart':
            # Add Bar chart trace
            chart_traces.append(go.Bar(x=adverse_events, y=event_counts, marker=dict(color='orange'), name='Bar'))
        
        if chart_type == 'Histogram':
            # Add Histogram chart trace
            chart_traces.append(go.Histogram(x=event_counts, y=adverse_events, marker=dict(color='orange'), name='Histogram'))

        if chart_type == 'Pie Chart':
            # Add Pie chart trace
            chart_traces.append(go.Pie(labels=adverse_events,
                                       values=event_counts,
                                       hole=0.4,
                                       textinfo='percent',
                                       hoverinfo='label+value',
                                       name='Pie'))
        
        # Create a Plotly figure using the selected traces
        fig = go.Figure(chart_traces)

        # Customize the chart layout
        fig.update_layout(title=f'Adverse Events of {userChoices["drug"].capitalize()}',
                        xaxis_title='Adverse Events',
                        yaxis_title='Number of Adverse Events')
    
    else:
        url2search = base_url + '?search=receivedate:[20040101+TO+20230912]&count=patient.drug.drugindication.exact&limit=20'
    
        response = requests.get(url2search)
        data = response.json()

        drug_names = [entry['term'] for entry in data['results']]
        event_counts = [entry['count'] for entry in data['results']]

        # Create a list to store traces based on selected chart types
        chart_traces = []
        chart_type = userChoices['chartType']

        if chart_type == 'Bar Chart':
            # Add Bar chart trace
            chart_traces.append(go.Bar(x=drug_names, y=event_counts, name='Bar'))

        if chart_type == 'Histogram':
            # Add Histogram chart trace
            chart_traces.append(go.Histogram(x=event_counts, name='Histogram'))

        if chart_type == 'Pie Chart':
            # Add Pie chart trace
            chart_traces.append(go.Pie(labels=drug_names, values=event_counts, name='Pie'))

        # Create a Plotly figure using the selected traces
        fig = go.Figure(chart_traces)

        # Customize the chart layout
        fig.update_layout(title='Adverse Events by Drug Indication',
                        xaxis_title='Drug Indication',
                        yaxis_title='Number of Adverse Events')

    return fig.to_html()