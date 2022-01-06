import React, { useEffect } from "react";
import * as Style from "./style";
import { MapContainer, TileLayer } from "react-leaflet";
import { useSelector } from "react-redux";

const LeafletMap = (props) => {
  const mapSettings = useSelector((state) => state.map.settings);

  return (
    <Style.LeafletMapWrapper>
      <MapContainer
        style={{ height: "100%" }}
        center={mapSettings.center}
        zoom={mapSettings.zoom}
      >
        {props.children}

        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
      </MapContainer>
    </Style.LeafletMapWrapper>
  );
};

export default LeafletMap;
