import React from 'react';
import axios from 'axios';

class MapContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {lat1: -20,
                  long1: -20,
                  lat2: 20,
                  long2: 20,
                  predictions: []};
  }

  componentDidMount() {
    var req = "/predictions/?lat1=" + this.state.lat1 + "&long1=" + this.state.long1
               + "&lat2=" + this.state.lat2 + "&long2=" + this.state.long2;

    axios.get(req)
      .then(res => {
        const preds = res.data.preds;
        var predsToShow = []
        preds.forEach(function(pred){
          predsToShow.push("(" + pred.latitude + ", " + pred.longitude +
                          "), label: " + pred.label + "      ")
        })
        this.setState({ predictions: predsToShow });
      })
  }

  render() {
    return <div className="mapcontainer">
              <h1>This is the MapContainer component</h1>
              <p>Input lat/long:({this.state.lat1}, {this.state.long1}),
                                ({this.state.lat2}, {this.state.long2})</p>
              <div>
                <p>Response:</p>
                <p>Number of responses: {this.state.predictions.length}</p>
                <div>
                  {this.state.predictions.map(entry => {
                    return <p>{entry}</p>
                  })}
                </div>
              </div>
           </div>
  }
}

export default MapContainer;
