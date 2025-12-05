const map = L.map("map").setView([53.3498, -6.2603], 13); // Example: Dublin

// OSM tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
  attribution: "&copy; OpenStreetMap contributors",
}).addTo(map);

const placesLayer = L.geoJSON(null, {
  onEachFeature: (feature, layer) => {
    const props = feature.properties;
    layer.bindPopup(
      `<strong>${props.name}</strong><br>${props.description || ""}<br><em>${props.category}</em>`
    );
  },
}).addTo(map);

function renderPlacesList(features) {
  const list = document.getElementById("places-list");
  list.innerHTML = "";
  features.forEach((f) => {
    const li = document.createElement("div");
    li.className = "place-item";
    li.textContent = `${f.properties.name} (${f.properties.category})`;
    li.addEventListener("click", () => {
      const [lng, lat] = f.geometry.coordinates;
      map.setView([lat, lng], 16);
    });
    list.appendChild(li);
  });
}

async function loadPlaces() {
  try {
    const response = await fetch("/api/places/");
    const data = await response.json(); // GeoJSON
    placesLayer.clearLayers();
    placesLayer.addData(data);
    renderPlacesList(data.features);

    if (data.features.length > 0) {
      const bounds = placesLayer.getBounds();
      map.fitBounds(bounds);
    }
  } catch (err) {
    console.error("Error loading places:", err);
  }
}

document.getElementById("locate-btn").addEventListener("click", () => {
  if (!navigator.geolocation) {
    alert("Geolocation not supported");
    return;
  }
  navigator.geolocation.getCurrentPosition(
    (pos) => {
      const { latitude, longitude } = pos.coords;
      map.setView([latitude, longitude], 15);
      L.marker([latitude, longitude]).addTo(map).bindPopup("You are here").openPopup();
    },
    (err) => {
      console.error(err);
      alert("Could not get location");
    }
  );
});

// Initial load
loadPlaces();

const form = document.getElementById("place-form");

if (form) {
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    if (!navigator.geolocation) {
      alert("Geolocation is not supported by your browser");
      return;
    }

    navigator.geolocation.getCurrentPosition(
      async (pos) => {
        const { latitude, longitude } = pos.coords;

        const payload = {
          name: document.getElementById("place-name").value,
          category: document.getElementById("place-category").value,
          description: document.getElementById("place-description").value,
          location: {
            type: "Point",
            coordinates: [longitude, latitude], // GeoJSON: [lng, lat]
          },
        };

        try {
          const response = await fetch("/api/places/", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(payload),
          });

          if (!response.ok) {
            const errText = await response.text();
            console.error("Error from API:", errText);
            alert("Error creating place (check console)");
            return;
          }

          // Success
          alert("Place created!");
          form.reset();
          loadPlaces(); // refresh markers & list

        } catch (err) {
          console.error("Network error:", err);
          alert("Network error – see console");
        }
      },
      (err) => {
        console.error("Geolocation error:", err);
        alert("Could not get your location");
      }
    );
  });
}
