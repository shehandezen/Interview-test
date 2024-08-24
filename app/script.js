window.onload = function () {
    let resultBox = document.getElementsByClassName('result-box')[0]
    let latitudeElement = document.getElementsByTagName('input')[0]
    let longitudeElement = document.getElementsByTagName('input')[1]
    let find = document.getElementById('find')
    let nearest_location = document.getElementById('location')
    let distance = document.getElementById('distance')
    let country = document.getElementById('country')
    let lat = document.getElementById('lat')
    let lon = document.getElementById('lon')
    let latitude
    let longitude


    latitudeElement.addEventListener('change', (e) => {
        latitude = e.target.value
    })

    longitudeElement.addEventListener('change', (e) => {
        longitude = e.target.value
    })

    find.addEventListener('click', () => {

        if (!(longitude == undefined || longitude == null || latitude == undefined || latitude == null)) {
            let headers = new Headers();

            headers.append('Content-Type', 'application/json');
            headers.append('Accept', 'application/json');

            headers.append('Access-Control-Allow-Origin', '*');

            fetch(`https://nearest-location-finder.onrender.com/location/${latitude}/${longitude}`,
                {
                    method: 'GET',
                    headers: headers
                }
            ).then(response => response.json()).then(data => {
                nearest_location.innerHTML = `Location: ${data.data.nearest_location}`
                distance.innerHTML = `Distance: ${data.data.distance}km`
                country.innerHTML = `Country: ${data.data.country}`
                lat.innerHTML = `Latitude: ${data.data.latitude}`
                lon.innerHTML = `Longitude: ${data.data.longitude}`


            }).catch(e => console.error(e))
        } else {
            console.log('Enter valid coordinates')
        }


    })
}

