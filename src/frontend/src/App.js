// import logo from "./logo.svg";

import { useEffect, useState } from "react";
import "./App.css";
// import ImageCanvas from "./Components/ImageCanvas/ImageCanvas";
// import LandingPage from "./Components/LandingPage/LandingPage";
import MainPage from "./Components/MainPage/MainPage";

function App() {
  // console.log(window.innerWidth);

  // const [scroll, setScroll] = useState(0)
  const [isFixed, setIsFixed] = useState(true);
  useEffect(() => {
    document.addEventListener("scroll", () => {
      // console.log(window.scrollY)
      // const scrollCheck = window.scrollY > 900
      // if (scrollCheck !== scroll) {
      //   setScroll(scrollCheck)
      //   console.log("yey")
      // }
      if (window.scrollY > 9000) {
        // console.log("yeys")
        setIsFixed(false);
      } else {
        setIsFixed(true);
      }
    });
  });

  return (
    <div className="App">
      {/* <div
        class="scroll-downs"
        style={isFixed ? { opacity: "100%" } : { opacity: "0%" }}
      >
        <div class="mousey">
          <div class="scroller"></div>
        </div>
      </div> */}
      {/* <LandingPage />
      <ImageCanvas
        scrollHeight={10000}
        width={1920}
        height={1080}
        numFrames={775}
      /> */}
      <MainPage />
    </div>
  );
}

export default App;
