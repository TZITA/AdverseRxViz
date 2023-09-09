# AdverseRxViz

![logo](static/assets/logo.jpg)
  
## Overview

**AdverseRxViz** (Adverse Reaction Visualizer) is a web-based tool designed for healthcare professionals, researchers, and pharmaceutical experts. It interacts with open-source health-related databases, specifically focusing on adverse events related to drugs. The primary goal of this project is to provide users with a user-friendly tool for visualizing and analyzing data related to adverse events associated with various drugs.

## Features

- **Interactive Data Visualization**: The application allows users to interactively visualize health-related data, enabling them to gain insights into disease prevalence, risk factors, and healthcare trends.

- **Database Integration**: The application fetches data from open-source health-related databases, ensuring that users have access to up-to-date and reliable information.

- **Chart Types**: Users can choose from a variety of chart types, including bar charts, histograms, pie charts, and line charts, to visualize data in the most suitable format.

- **User-Friendly Interface**: The intuitive user interface makes it easy for users to select data parameters, chart types, and generate visualizations.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript, Plotly.js
- **Backend**: Python, Flask
- **Database**: [OpenFDA API](https://open.fda.gov/)
- **Third-party Services**: [Plotly](https://plotly.com/)

## Getting Started

To run the application locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Flask application with `python app.py`.
4. Access the application in your web browser at `http://localhost:5500`.

## Usage

1. Select the desired chart type from the dropdown list.
2. Choose additional parameters such as gender, age, and drug name (if applicable).
3. Click the "Generate Chart" button to create the visualization.
4. Explore the interactive chart to gain insights from the data.

## Contact

- **Thomas Beyene**
- LinkedIn: [Thomas Beyene](https://www.linkedin.com/in/thomas-beyene-habtemariam-967245173/)
- GitHub: [TZITA](https://github.com/TZITA)

## License

This project is licensed under the MIT License.
