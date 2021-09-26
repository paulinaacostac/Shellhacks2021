import React, { useState } from "react";
import "./video.css";
import { Link } from "react-router-dom";
import { useReactMediaRecorder } from "react-media-recorder";
import { render } from "react-dom";
import VideoRecorder from "react-video-recorder";
import "../home/home.css";

export default function Video(props) {
  const { status, startRecording, stopRecording, mediaBlobUrl } =
    useReactMediaRecorder({ video: true });
  const id = props.id;
  const [video, setVideo] = useState([]);

  function handleBlob(blob) {
    let r = (Math.random() + 1).toString(36).substring(7);

    const file = new File([blob], r, {
      lastModified: new Date().getTime(),
      type: blob.type,
    });
    var reader = new FileReader();
    if (file) {
      reader.readAsDataURL(file);
      reader.onload = () => {
        var Base64 = reader.result;

        setVideo(Base64);
      };
      reader.onerror = (error) => {
        console.log("error: ", error);
      };
    }
  }

  function handleSubmit(id) {
    console.log(video);
  }

  return (
    <div>
      <Link to="/Main" style={{ textDecoration: "none", margin: "5px" }}>
        {" "}
        &#10094;{" "}
      </Link>
      <div style={{ marginTop: "20px" }}>
        <VideoRecorder
          onRecordingComplete={(videoBlob) => {
            handleBlob(videoBlob);
            console.log("videoBlob", videoBlob);
          }}
        />
      </div>

      <div
        style={{
          margin: "20px auto",
          display: "flex",
          justifyContent: "center",
        }}
      >
        <button className="button" onClick={() => handleSubmit()}>
          Submit
        </button>
      </div>
    </div>
  );
}

/*



*/
