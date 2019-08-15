var map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 37.777, lng: -122.417},
    zoom: 15
  });
}
