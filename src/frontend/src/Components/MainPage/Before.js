import React from "react";
import ImageUploading from "react-images-uploading";
import trashStatic from "./trash-static.png";
import trash from "./trash.gif";

import "./Before.css";

const Before = () => {
  const [images, setImages] = React.useState([]);
  const [compressedImg, setCompressedImg] = React.useState();
  const [removeButtonState, setRemoveButtonState] = React.useState(true);
  const [isConverting, setIsConverting] = React.useState(false);
  const [isImgFetched, setIsImgFetched] = React.useState(false);
  const [rate, setRate] = React.useState(50);
  const [rt, setRt] = React.useState();
  const maxNumber = 1;
  const onChange = (imageList, addUpdateIndex) => {
    // data for submit
    setRate(50)
    console.log(imageList, addUpdateIndex);
    setImages(imageList);
    setRt()
    if (imageList.length === 0) {
      setIsImgFetched(false);
    }
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
    download(compressedImg, "Compressed.jpg");
  };

  const fetchImage = () => {
    setIsConverting(true);
    console.log("test");
    console.log(images);
    fetch("http://127.0.0.1:5000/", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ data: images[0].data_url, percent: rate }),
    })
      .then((res) => res.json())
      .then((res) => {
        console.log(res);
        console.log(base64toimg(res.Response));
        setCompressedImg(base64toimg(res.Response));
        setIsConverting(false);
        setIsImgFetched(true);
        setRt(Math.round(res.time * 1000) / 1000);
      });

    // fetch('http://127.0.0.1:5000/')
    // .then((res) => res.json())
    // .then((resp) => {console.log("halo")})
  };

  const base64toimg = (string) => {
    string = string.slice(2, string.length - 1);
    return `data:image/jpeg;base64,${string}`;
  };

  const showResult = () => {
    return isImgFetched && !isConverting;
  };

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
          {isImgFetched ? null : <h2>Compression Rate: {rate.toString()}%</h2>}
          {isImgFetched ? null : (
            <input
              type="range"
              min="1"
              max="100"
              className="slider"
              onChange={rangeHandler}
              disabled={isConverting ? "disabled" : ""}
            ></input>
          )}
          {isImgFetched ? null : (
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
          )}
          {isConverting ? (
            <div class="loader">
              <div class="loaderBar"></div>
            </div>
          ) : null}
          {isImgFetched ? (
            <div className="before__download-page">
              <div className="before__download-container">
                <div className="image-container">
                  <div className="img-container">
                    <img src={compressedImg} alt="" />
                  </div>
                </div>
              </div>
              <h4 className="runtime">runtime: {rt} s</h4>
              &nbsp;
              <button className="download-button" onClick={downloadHandler}>
                Download
              </button>
            </div>
          ) : null}
        </div>
      )}
    </div>
  );
};

export default Before;
