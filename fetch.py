import requests
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd


def create_adverse_events_chart(userChoices):
    # Construct the url to retrieve the data from user choices
    base_url = 'https://api.fda.gov/drug/event.json'
    
    # check if drug is selected
    if userChoices['drug'] != "":
        drugSearch = f'patient.drug.openfda.generic_name:"{userChoices["drug"]}"'
    else:
        drugSearch = ""
    
    # check if adverse event is selected
    if userChoices['adverseEvent'] != "":
        eventSearch = f'patient.reaction.reactionmeddrapt.exact:"{userChoices["adverseEvent"].upper()}"'
    else:
        eventSearch = ""

    # Construct the time frame search based on start and end dates
    if userChoices['startDate'] != "":
        startD = userChoices['startDate'].replace('-', '')
    else:
        startD = "20040101"
    
    if userChoices['endDate'] != "":
        endD = userChoices['endDate'].replace('-', '')
    else:
        endD = datetime.today().strftime('%Y%m%d')
    
    timeSearchFrame = f'receivedate:[{startD}+TO+{endD}]'

    # Combine all search criteria with logical operators (AND) if specified
    search_terms = [term for term in [drugSearch, eventSearch, timeSearchFrame] if term]

    # Construct the final search query
    search_query = '+AND+'.join(search_terms)

    # Construct the full URL for the search
    if eventSearch != "":
        url2search = f'{base_url}?search={search_query}&count=patient.patientsex'
    else:
        url2search = f'{base_url}?search={search_query}&count=patient.reaction.reactionmeddrapt.exact&limit=20'

    # Retrieve the data from the API
    response = requests.get(url2search)
    data = response.json()

    # Check if data is available
    # If not, return a message to flask route to handle the error
    if data['results'] is None:
        return "no data"
    
    if eventSearch != "":
        xx = []
        yy = []
        for entry in data['results']:
            if entry['term'] == 0:
                xx.append("Unknown")
            elif entry['term'] == 1:
                xx.append("Male")
            elif entry['term'] == 2:
                xx.append("Female")
            yy.append(entry['count'])
    else:
        xx = [entry['term'] for entry in data['results']]
        yy = [entry['count'] for entry in data['results']]

    
    # Create a Pandas DataFrame with the data
    heatmap_data = pd.DataFrame(data=data['results'])

    # Prepare the chart
    chart_traces = []
    chart_type = userChoices['chartType']

    if chart_type == 'Bar Chart':
        chart_traces.append(go.Bar(x=xx, y=yy, marker=dict(color='orange'), name='Bar'))

    if chart_type == 'Pie Chart':
        chart_traces.append(go.Pie(labels=xx, values=yy, hole=0.4, textinfo='percent', hoverinfo='label+value', name='Pie'))
    
    if chart_type == 'Heatmap':
        chart_traces.append(go.Heatmap(x=heatmap_data['term'], y=heatmap_data['count'], z=heatmap_data['count'], colorscale='Viridis', name='Heatmap'))
        
    # Create a Plotly figure using the selected traces
    fig = go.Figure(chart_traces)

    # Customize the chart layout
    # Change date format
    startDate_obj = datetime.strptime(startD, "%Y%m%d")
    formattedStartD = startDate_obj.strftime("%B %d, %Y")

    endDate_obj = datetime.strptime(endD, "%Y%m%d")
    formattedEndD = endDate_obj.strftime("%B %d, %Y")
        
    if userChoices['drug'] != "":
        if userChoices['adverseEvent'] != "":
            fig.update_layout(title=f'{userChoices["adverseEvent"].capitalize()} associated with {userChoices["drug"].capitalize()} reported between {formattedStartD} and {formattedEndD}')
        else:
            fig.update_layout(title=f'Adverse Events of {userChoices["drug"].capitalize()} reported between {formattedStartD} and {formattedEndD}')
    else:
        fig.update_layout(title=f'Adverse Events by Drug Indication reported between {formattedStartD} and {formattedEndD}')
        
    fig.update_layout(xaxis_title='Adverse Events', yaxis_title='Number of Adverse Events')
    
    # Return the chart as HTML
    return fig.to_html()