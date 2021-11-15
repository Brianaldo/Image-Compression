import React, { useEffect, useState } from "react";
import Before from "./Before";
import "./MainPage.css";

const MainPage = () => {
  return (
    <div className="main-page">
      <div className="main-page--header">
        <h1 className="main-page--header-title">image compression</h1>
      </div>
      <Before />
    </div>
  );
};

export default MainPage;
