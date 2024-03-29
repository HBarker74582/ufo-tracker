console.log("hi");
// Create a map object
var myMap = L.map("map", {
    center: [39.0997222, -94.5783333],
    zoom: 5
});

var sightings = d3.json('/alien_data').then(alien_data => {

    // console.log(alien_data);

    // Loop through the  array and create one marker for each city object
    for (var i = 0; i < alien_data.length; i++) {
        var loc = [alien_data[i].lat, alien_data[i].long];
        return new L.CircleMarker(loc, {
            fillOpacity: 0.75,
            color: "green",
            radius: 10,
        }).bindPopup("<h2>" + alien_data[i].city_state + "</h2> <hr> <h3>Quote: " + alien_data[i].short_description + "</h3>").addTo(myMap);
    }
});

var all_sightings = L.layerGroup([sightings]);

var bases = d3.json('/military').then(bases => {



    // Loop through the  array and create one marker for each city object
    for (var i = 0; i < bases.length; i++) {
        var loc = [bases[i].lat, bases[i].long];
        // console.log(loc);
        L.circle(loc, {
            // fillOpacity: 1,
            color: "red",
            radius: 20,

        }).bindPopup("<h1>" + bases[i].mil_base_name + "</h1> <hr> <h3>Population: " + bases[i].operational_status + "</h3>").addTo(myMap);
    }

});
var all_bases = L.layerGroup([bases]);


var heatMapPoints = d3.json('/alien_data').then(alien_data => {

    var heatArray = [];

    for (var i = 0; i < alien_data.length; i++) {
        var location = [alien_data[i].lat, alien_data[i].long];
        // console.log(location);
        if (location) {
            heatArray.push([location[0], location[1]]);
        }
    }
    var heat = L.heatLayer(heatArray, {
        radius: 100,
        blur: 20
    }).addTo(myMap);
});


var basemap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.comic",
    accessToken: API_KEY
}).addTo(myMap);

var overlayMaps = {
    "Sightings": all_sightings,
    "Military Bases": all_bases
};

var baseMaps = {
    "Main": basemap
    // "Heat Map": heat
};

L.control.layers(baseMaps, overlayMaps).addTo(myMap);



