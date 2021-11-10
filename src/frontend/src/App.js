// import logo from "./logo.svg";
import "./App.css";
import ImageCanvas from "./Components/ImageCanvas/ImageCanvas";
import MainPage from "./Components/MainPage/MainPage";

function App() {
  console.log(window.innerWidth);
  return (
    <div className="App">
      <ImageCanvas
        scrollHeight={10000}
        width={1920}
        height={1080}
        numFrames={775}
      />
      <MainPage/>
    </div>
  );
}

export default App;
