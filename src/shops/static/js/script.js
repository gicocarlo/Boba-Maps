var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.777, lng: -122.417},
    zoom: 12
  });

  var value = JSON.parse(document.getElementById('boba_loc').textContent);
  console.log(value);
  var geocoding = new google.maps.Geocoder();
  geocoding.geocode({'address': value}, (results, status) => {
    if (status == 'OK') {
      map.setCenter(results[0].geometry.location);
      // var marker = new google.maps.Marker({
      //   map: map,
      //   position: results[0].geometry.location
      // });
    }
    else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
  // var list = JSON.parse(document.getElementById('boba_list').textContent);
  // console.log(list);
}
