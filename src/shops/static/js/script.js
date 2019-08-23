var map;

function initMap() {
  var value = JSON.parse(document.getElementById('boba_loc').textContent);
  console.log(value);
  var list = JSON.parse(document.getElementById('boba_list').textContent);
  console.log(list);

  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.777, lng: -122.417},
    zoom: 15
  });
}
