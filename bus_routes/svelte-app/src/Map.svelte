<script>
    import { onMount } from "svelte";
    import axios from 'axios';
    import { Map, View } from "ol";
    import TileLayer from "ol/layer/Tile";
    import VectorLayer from "ol/layer/Vector";
    import VectorSource from "ol/source/Vector";
    import Point from "ol/geom/Point";
    import Feature from "ol/Feature";
    import {Icon, Style} from "ol/style";
    import OSM from "ol/source/OSM";
    import { fromLonLat } from "ol/proj";
    import { LineString } from "ol/geom";
    import { Stroke } from "ol/style";

    let routeVectorSource = new VectorSource();
let routeLayer = new VectorLayer({
    source: routeVectorSource
});

    let map;

    async function createRoutes() {
    try {
        const coordinates = []; 
        // Assuming you have a list of features (pins) on the map, 
        // you'd loop through them and extract their coordinates.
        // This is a placeholder and should be replaced with actual logic.
        // features.forEach(feature => {
        //     coordinates.push(feature.getGeometry().getCoordinates());
        // });

        const response = await axios.post('/api/calculate_routes/', { coordinates });
        const routes = response.data.routes;

        // Clear any existing routes from the map
        routeVectorSource.clear();

        const colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FFA500', '#800080', '#A52A2A', '#008080'];

        // Loop through each route received from the backend and display it on the map
        routes.forEach((route, index) => {
            const lineFeature = new Feature({
                geometry: new LineString(route)
            });
            lineFeature.setStyle(new Style({
                stroke: new Stroke({
                    color: colors[index % colors.length],  // Cycle through colors
                    width: 3
                })
            }));
            routeVectorSource.addFeature(lineFeature);
        });
    } catch (error) {
        console.error("Error creating routes:", error);
    }
}


  
    onMount(() => {
      const vectorSource = new VectorSource();
  
      map = new Map({
        target: "map",
        layers: [
    new TileLayer({
        source: new OSM()
    }),
    new VectorLayer({
        source: vectorSource  // This is for the pins
    }),
    routeLayer  // This is for the routes
],

        view: new View({
          center: fromLonLat([76.66501949986178, 12.136039536554538]),
          zoom: 14
        })
      });
  
      map.on('click', function(event) {
        const feature = new Feature({
          geometry: new Point(event.coordinate)
        });
  
        feature.setStyle(new Style({
          image: new Icon({
            anchor: [0.5, 46],
            anchorXUnits: 'fraction',
            anchorYUnits: 'pixels',
            src: 'https://openlayers.org/en/latest/examples/data/icon.png'
          })
        }));
  
        vectorSource.addFeature(feature);
      });
    });
</script>

<style>
    #map {
      width: 100%;
      height: 100vh;
    }
</style>

<div id="map"></div>
<button on:click={createRoutes}>Create Routes</button>
