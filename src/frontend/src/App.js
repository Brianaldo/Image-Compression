import logo from "./logo.svg";
import "./App.css";
import ImageCanvas from "./Components/ImageCanvas/ImageCanvas";

function App() {
  return (
    <div className="App">
      <ImageCanvas
        scrollHeight={4000}
        width={1440}
        height={1080}
        numFrames={299}
      />
    </div>
  );
}

export default App;
