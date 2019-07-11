$.getJSON('static/ratings.json', function (data) {
    console.log(data);
    var output = '<ul>';
    $.each(data, function (key, val) {
        output += '<li>' + val.symbol + " " + val.overallRating + '</li>';
    });
    output += '</ul>';
    $('#update').html(output);
});