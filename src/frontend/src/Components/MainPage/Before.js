import React from "react";
import ImageUploading from "react-images-uploading";
import trashStatic from "./trash-static.png";
import trash from "./trash.gif";

import "./Before.css";

const Before = () => {
  const [images, setImages] = React.useState([]);
  const [removeButtonState, setRemoveButtonState] = React.useState(true);
  const [isConverting, setIsConverting] = React.useState(false);
  const [rate, setRate] = React.useState(50);
  const maxNumber = 1;
  const onChange = (imageList, addUpdateIndex) => {
    // data for submit
    console.log(imageList, addUpdateIndex);
    setImages(imageList);
  };
  const rangeHandler = (event) => {
    setRate(event.target.value);
  };

  function download(dataurl, filename) {
    const link = document.createElement("a");
    link.href = dataurl;
    link.download = filename;
    link.click();
  }
  
  const downloadHandler = () => {
    download(images[0].data_url, "test.jpg")
  }

  const fetchImage = () => {
    console.log("test")
    console.log(images)
    fetch('http://127.0.0.1:5000/', {
      method: 'POST',
      headers: {
        Accept: "application/json",
        'Content-Type': "application/json"
      },
      body: JSON.stringify(images[0].data_url)
    })
    .then((res) => res.json())
    .then((res) => console.log("halo"))

    // fetch('http://127.0.0.1:5000/')
    // .then((res) => res.json())
    // .then((resp) => {console.log("halo")})
  }

  return (
    <div className="before">
      <div className="before__image-uploading">
        <ImageUploading
          multiple
          value={images}
          onChange={onChange}
          maxNumber={maxNumber}
          dataURLKey="data_url"
        >
          {({
            imageList,
            onImageUpload,
            onImageRemoveAll,
            onImageUpdate,
            onImageRemove,
            isDragging,
            dragProps,
          }) => (
            // write your building UI
            <div className="before__upload-page">
              <button
                className="before__upload-container"
                style={
                  isDragging
                    ? {
                        animation: "shake 0.5s",
                        animationIterationCount: "infinite",
                      }
                    : null
                }
                onClick={imageList.length === 0 ? onImageUpload : null}
                {...dragProps}
              >
                {imageList.length === 0 ? (
                  <h1
                    style={
                      isDragging ? { color: "black" } : { color: "lightgray" }
                    }
                  >
                    Click or Drop here
                  </h1>
                ) : (
                  imageList.map((image) => (
                    <div className="img-container">
                      <img src={image.data_url} alt="" />
                    </div>
                  ))
                )}
              </button>
              &nbsp;
              <div className="remove-button--container">
                {isConverting ? null : (
                  <button
                    onClick={onImageRemoveAll}
                    className="remove-button"
                    onMouseEnter={() => {
                      setRemoveButtonState(false);
                    }}
                    onMouseLeave={() => {
                      setRemoveButtonState(true);
                    }}
                  >
                    {removeButtonState ? (
                      <img src={trashStatic} alt=""></img>
                    ) : (
                      <img src={trash} alt=""></img>
                    )}
                  </button>
                )}
              </div>
            </div>
          )}
        </ImageUploading>
      </div>
      {images.length === 0 ? (
        <div className="before__setting">
          <h1>Please upload an Image</h1>
        </div>
      ) : (
        <div className="before__setting">
          <h2>Compression Rate: {rate.toString()}%</h2>
          <input
            type="range"
            className="slider"
            onChange={rangeHandler}
            disabled={isConverting ? "disabled" : ""}
          ></input>
          <button
            className="button-default"
            onClick={() => {
              setIsConverting(true);
              fetchImage();
            }}
            disabled={isConverting ? "disabled" : ""}
            style={isConverting ? { opacity: "0%" } : { opacity: "100%" }}
          >
            Convert
          </button>
          {isConverting ? (
            <div class="loader">
              <div class="loaderBar"></div>
            </div>
          ) : null}
          <div className="before__download-page">
            <div className="before__download-container">
              <div className="image-container">
                <div className="img-container">
                  <img src={trash} alt="" />
                </div>
              </div>
            </div>
            &nbsp;
            <button className="download-button" onClick={downloadHandler}>
              Download
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Before;
