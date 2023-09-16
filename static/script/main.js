// Create an object to store user choices
var userChoices = {
    drug: "",
    dosageForm: "",
    adverseEvent: "",
    startDate: "",
    endDate: "",
    ageFrom: "",
    ageTo: "",
    sex: "",
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

    // Update user choices on input change
    $("input[type='text'], input[type='date'], input[type='number']").on("input", function() {
        var fieldName = $(this).attr("name");
        var fieldValue = $(this).val();
        userChoices[fieldName] = fieldValue;
    });

    // Update user choices for sex selection
    $("input[type='text'][list='sex']").on("input", function() {
        var sexValue = $(this).val();
        userChoices.sex = sexValue;
    });

    // Update user choices for chart type selection
    $("#selectedChart").on("input", function() {
        var chartTypeValue = $(this).val();
        userChoices.chartType = chartTypeValue;
    });
});

// Search button
document.getElementById('searchButton').addEventListener('click', function() {
    console.log(userChoices);
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

        // Open the chart in a new tab
        var newTab = window.open();
        newTab.document.write(chartHtml);
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