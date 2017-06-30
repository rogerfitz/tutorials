function initAutocomplete() {
  var input_starting = document.getElementById('startingAddress');
  var input_destination = document.getElementById('destinationAddress');
  
  var autocomplete_starting = new google.maps.places.Autocomplete(input_starting);
  var autocomplete_destination = new google.maps.places.Autocomplete(input_destination);
  
  function geolocate() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var geolocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        var circle = new google.maps.Circle({
          center: geolocation,
          radius: position.coords.accuracy
        });
        autocomplete_starting.setBounds(circle.getBounds());
        autocomplete_destination.setBounds(circle.getBounds());
      });
    }
  }
  var format = d3.time.format("%Y-%m-%dT%H:%M")
  document.getElementById("leaveAfter").value = format(new Date());

}


function showLoader(show){
     console.log(show)
    if (show){
        document.getElementById("loader-1").style.visibility="visible";
        document.getElementById("loader-1").style.height="100px";
    } else{
        document.getElementById("loader-1").style.visibility="hidden";
        document.getElementById("loader-1").style.height="0px";
    }
}

function addGMapsLink(){
    //format https://www.google.com/maps/dir/Chicago,+IL+60607/Mariano's+Fresh+Market,+40+S+Halsted+St,+Chicago,+IL+60661
    document.getElementById("gmapsP").style.visibility="visible";
    document.getElementById("gmapsHref").href="https://www.google.com/maps/dir/"+document.getElementById("startingAddress").value+"/"+document.getElementById("destinationAddress").value;
}


function submit(){
    var params={}
    params['startingAddress'] = document.getElementById("startingAddress").value;
    params['destinationAddress'] = document.getElementById("destinationAddress").value;
    params['leaveAfter'] = (new Date(document.getElementById("leaveAfter").value)).getTime();
    params['API_KEY'] = document.getElementById("apiKeyInput").value;
    url_string="/data?"
    for (var key in params) {
        if (params[key]){
            url_string+=key+"="+params[key]+"&"
        }
    }
    console.log(url_string);
    showLoader(true);
    d3.json(url_string, function(error, response) {
        if (error){
            console.log(error);
            console.log("ERR");
            document.getElementById("apiKeyLabel").style.visibility="visible";
            document.getElementById("apiKeyInput").style.visibility="visible";
        }else{
            genChart(response);
            addGMapsLink();
            }
        showLoader(false);
    });
}

//So we don't waste free api calls
function dummySubmit(){
    var params={}
    params['startingAddress'] = document.getElementById("startingAddress").value;
    params['destinationAddress'] = document.getElementById("destinationAddress").value;
    params['leaveAfter'] = document.getElementById("leaveAfter").value;

    url_string="/data?"
    for (var key in params) {
        url_string+=key+"="+params[key]+"&"
    }
    
    console.log(url_string);
    showLoader(true);
    setTimeout(function(){
        genChart(col_data)
        showLoader(false);
        }, 3000);
}

var col_data=[['best_guess',
  35.0,
  35.0,
  34.0,
  34.0,
  34.0,
  34.0,
  34.0,
  34.0,
  35.0,
  36.0,
  38.0,
  43.0,
  48.0,
  49.0,
  52.0,
  53.0,
  57.0,
  57.0,
  58.0,
  57.0,
  57.0,
  57.0,
  57.0,
  55.0,
  53.0,
  50.0,
  48.0,
  45.0,
  42.0,
  39.0,
  36.0,
  33.0,
  32.0],
 ['optimistic',
  27.0,
  27.0,
  27.0,
  28.0,
  28.0,
  29.0,
  29.0,
  30.0,
  30.0,
  31.0,
  32.0,
  35.0,
  39.0,
  40.0,
  42.0,
  43.0,
  46.0,
  47.0,
  47.0,
  46.0,
  46.0,
  46.0,
  46.0,
  45.0,
  44.0,
  42.0,
  41.0,
  38.0,
  36.0,
  34.0,
  31.0,
  30.0,
  28.0],
 ['pessimistic',
  41.0,
  41.0,
  41.0,
  42.0,
  43.0,
  43.0,
  43.0,
  45.0,
  46.0,
  48.0,
  53.0,
  61.0,
  67.0,
  70.0,
  74.0,
  78.0,
  82.0,
  83.0,
  82.0,
  83.0,
  83.0,
  80.0,
  77.0,
  73.0,
  72.0,
  66.0,
  62.0,
  58.0,
  54.0,
  50.0,
  45.0,
  42.0,
  40.0],
 ['x',
  1498753657000,
  1498753800000,
  1498754700000,
  1498755600000,
  1498756500000,
  1498757400000,
  1498758300000,
  1498759200000,
  1498760100000,
  1498761000000,
  1498761900000,
  1498762800000,
  1498763700000,
  1498764600000,
  1498765500000,
  1498766400000,
  1498767300000,
  1498768200000,
  1498769100000,
  1498770000000,
  1498770900000,
  1498771800000,
  1498772700000,
  1498773600000,
  1498774500000,
  1498775400000,
  1498776300000,
  1498777200000,
  1498778100000,
  1498779000000,
  1498779900000,
  1498780800000,
  1498781700000]]
  
var now = new Date().toString();
var TZ = now.indexOf('(') > -1 ?
now.match(/\([^\)]+\)/)[0].match(/[A-Z]/g).join('') :
now.match(/[A-Z]{3,4}/)[0];
if (TZ == "GMT" && /(GMT\W*\d{4})/.test(now)) TZ = RegExp.$1;
document.getElementById("timezone").innerHTML+=TZ;
genChart(col_data);

function genChart(col_data){
    var chart = c3.generate({
        data: {
            x: 'x',
            xFormat: '%Y-%m-%d %H:%M:%S', // 'xFormat' can be used as custom format of 'x'
            columns: col_data
                      
        },
        axis: {
            x: {
                type: 'timeseries',
                tick: {
                    format: '%I:%M %p'
                },
                label: 'Departure Time (starting timezone)'
            },
            y: {
                label: 'Trip Duration (minutes)'
                },
                
        }
    });
}

