var map;
var markers;
var labels = '12345';

/*
initMap()

Using Google Maps JavaScript API, this function creates the map onto the shops
page.The coordinates are centered at Yelp HQ in San Francisco, CA

https://developers.google.com/maps/documentation/javascript/tutorial
*/

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.787, lng: -122.400},
    zoom: 11
  });
  changeMap();
}

/*
changeMap()

Uses Google's Geocoder API to convert the user input into coordinates which will
be the new center of the map with a marker.

https://developers.google.com/maps/documentation/javascript/geocoding
*/

function changeMap(){
  var address = JSON.parse(document.getElementById('boba_loc').textContent);
  var geocoding = new google.maps.Geocoder();
  geocoding.geocode({'address': address}, (results, status) => {
    if (status == 'OK') {
      map.setCenter(results[0].geometry.location);
      markers = new google.maps.Marker({
        map: map,
        position: results[0].geometry.location
      });
    }
    else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
  markBobaShops();
}

/*
markBobaShops()

Using the coordinates queried from the Yelp API, add markers to each bubble tea
shop

https://developers.google.com/maps/documentation/javascript/markers
*/
function markBobaShops(){
  var bobaData = JSON.parse(document.getElementById('boba_list').textContent);
  for(let i = 0; i < bobaData.length; i++){
    var latitude = bobaData[i]["coordinates"]["latitude"];
    var longitude = bobaData[i]["coordinates"]["longitude"];
    markers = new google.maps.Marker({
      map: map,
      position: {lat: latitude, lng: longitude},
      label: labels[i]
    });
  }
}
