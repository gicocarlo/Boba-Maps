var map;
var markers;
var labels = '12345';

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.777, lng: -122.417},
    zoom: 11
  });
  changeMap();
}

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
