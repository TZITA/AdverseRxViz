// Create an object to store user choices
var userChoices = {
    drug: "",
    dosageForm: "",
    adverseEvent: "",
    timeFrame: "",
    startDate: "",
    endDate: "",
    chartType: ""
};

// Dark mode
$(document).ready(function() {
    $( ".change" ).on("click", function() {
        if( $( "body" ).hasClass( "dark" )) {
            $( "body" ).removeClass( "dark" );
            $( ".change" ).text( "OFF" );
        } else {
            $( "body" ).addClass( "dark" );
            $( ".change" ).text( "ON" );
        }
    });

    // Time period more button
    $("#selectedTime").on("input", function() {
        var timeFrame = $(this).val();

        if (timeFrame === "Custom") {
            $("#customDate").show();
        } else {
            $("#customDate").hide();
        }

        userChoices.timeFrame = timeFrame;
    });

    // Update user choices on input change
    $("input[type='text'], input[type='date'], input[type='number']").on("input", function() {
        var fieldName = $(this).attr("name");
        var fieldValue = $(this).val();
        userChoices[fieldName] = fieldValue;
    });

    // Update user choices for chart type selection
    $("#selectedChart").on("input", function() {
        var chartTypeValue = $(this).val();
        userChoices.chartType = chartTypeValue;
    });
});

// Search button
document.getElementById('searchButton').addEventListener('click', function() {
    // Check if chart type is selected and
    if (userChoices.chartType == "") {
        alert("Please select a chart type.");
        return;
    }

    // Show loading gif
    document.getElementById('loading-gif').style.display = 'flex';

    // Make an HTTP request to the Flask endpoint using Fetch API
    fetch('/generate_chart', {
        method: 'POST',
        body: JSON.stringify(userChoices),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.text())
    .then(chartHtml => {
        // Hide loading gif
        document.getElementById('loading-gif').style.display = 'none';

        //Open the chart in a new tab
        var newTab = window.open();
        newTab.document.write(chartHtml);

        // Customise the new tab
        // title
        if (userChoices.drug && userChoices.adverseEvent) {
            newTab.document.title = userChoices.drug + " and " + userChoices.adverseEvent;
        } else if (userChoices.drug) {
            newTab.document.title = userChoices.drug;
        } else if (userChoices.adverseEvent) {
            newTab.document.title = userChoices.adverseEvent;
        } else {
            newTab.document.title = "Adverse Event " + userChoices.chartType;
        }
    });
});

// guidelines more button
var btn = document.getElementsByClassName("collapse");
          
btn[0].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.parentElement.nextElementSibling;
    if (content.style.display === "block") {
        content.style.display = "none";
    } else {
        content.style.display = "block";
    }
});