url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

console.log(url)

d3.json(url, function(data) {
    console.log(data)
    generateMap(data)
})

/**
 * Generates Map
 * @param {json} earthquakes 
 */
function generateMap(earthquakes) {

    // Create earthquake layer group
    var eqLayer = new L.layerGroup();
    // Create new map and a layer
    var myMap = L.map("map", {
        center: [19.8968,-180.5828],
        zoom: 4,
        layers: [eqLayer]
    });

    // Base tile layers
    var satelliteMap = generateLayers("satellite-v9").addTo(myMap);
    var grayscaleMap = generateLayers("light-v9").addTo(myMap);
    var outdoorMap = generateLayers("outdoors-v10").addTo(myMap);

    var baseMaps = {
        "Satellite":satelliteMap,
        "Grayscale": grayscaleMap,
        "Outdoor": outdoorMap
    };

    var overlayMaps= {
        "Earthquakes":eqLayer
    }

    //Populate earthquake layer
    var features = earthquakes.features;
    generateCircles(features,eqLayer)
    

    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    legendArea = L.control();

    legendArea.onAdd = function (map) {
        return L.DomUtil.create("div","info");
    }

    var legend = L.control({ position: "bottomright" });

    legend.onAdd = function (map) {
        var div = L.DomUtil.create("div","legend info"), mag = [0,5,10,15,20,40]
        div.innerHTML = '<p>Magnitudes</p>'
    
    for (var i =0; i<mag.length;i++) {
        div.innerHTML += '<i style="background:'+getColor(mag[i]+1)+'"></i>' +
        +mag[i]+ (mag[i+1]?'&ndash;'+mag[i+1]+'<br>':'+');
    }
    return div;
    };
    legend.addTo(myMap)
}

/**
 * Create circles on the layer from data
 * @param {object} features 
 * @param {object} Leaflet layer
 */
function generateCircles(features,eqLayer) {
    for (var i = 0; i < features.length; i++) {
        var radius = features[i].properties.mag * 2000
        var color = getColor(features[i].geometry.coordinates[2])
        var long = features[i].geometry.coordinates[0]
        var lat = features[i].geometry.coordinates[1]

    // Add circle markers to earthquake_layer
    L.circle([lat,long], {
        fillOpacity: 0.75,
        color: color,
        fillColor: color,
        radius: radius
        })
    .bindPopup("<h2>"+features[i].properties.title+
    "</h2><h3>Type: "+ features[i].properties.type+"</h3>"+
    "<h3>Magnitude: "+ features[i].properties.mag+"</h3>"+
    "<h3>Date: "+ new Date(features[i].properties.time)+"</h3>")
    .addTo(eqLayer)
    }
}

/**
 * Generates color depending on magnitudes
 * @returns {string} Color codes
 * @param {number} Magnitude
 */
function getColor(dp) {
    return dp > 40 ? "#ff0303":
        dp > 25 ? "#ff8040":
        dp > 15 ? "#ffcc40":
        dp > 10 ? "#efff40":
        dp > 5 ? "#a3fa57":
        "#99ff40";
}

/**
 * Generate Layers from mapbox
 * @returns {object} Layer 
 * @param {string} Layer - layer type
 */
function generateLayers(layer_id) {
    var m_id = "mapbox/"+layer_id
    console.log(m_id)
    var layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: m_id,
        tileSize: 512,
        zoomOffset: -1,
        accessToken: API_KEY
    });
    return layer
}
