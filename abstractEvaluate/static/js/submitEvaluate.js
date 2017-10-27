$(document).ready(function() {
    $("#submit-abstract").click(function(event){
        //console.log("submit clicked");
        event.preventDefault();
        var abstractText = $("#abstract-text").val();
        $.ajax({
            type: "POST",
            url: "/api/evaluate_api/",
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                abstractText: abstractText,
            },
            success: function(response){
                console.log(response);
                var reportableHtml = "<p> Reportable: " + response.reportable + "</p>";
                $("#abstract-reportable-evaluation").html(reportableHtml);
            },
            error: function(xhr, textStatus, errorThrown) {
                alert("Please report this error: "+errorThrown + xhr.status + xhr.responseText);
            }
        });
    });
});