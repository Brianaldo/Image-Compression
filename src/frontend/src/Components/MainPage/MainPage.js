import React, { useEffect, useState } from "react";
import After from "./After";
import Before from "./Before";
import "./MainPage.css";

const MainPage = () => {
  return (
    <div className="main-page">
      <div className="main-page--header">
        <h1 className="main-page--header-title">image compression</h1>
      </div>
      <Before />
      <After />
    </div>
  );
};

export default MainPage;
