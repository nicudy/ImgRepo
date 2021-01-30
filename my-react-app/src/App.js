import React from 'react';
import './App.css';
import ImageUploader from 'react-images-upload';

class App extends React.Component {
  constructor(props) {
    super(props);

    this.handleChange = this.handleChange.bind(this);
  } 

  handleChange(image) {
    const formData = new FormData(); 
    formData.append('file', image[0]);
    fetch('http://127.0.0.1:5000/apiUpload/', {
      method: 'POST',
      body: formData
    })
  }

  render() {
    return (
      <>
        <ImageUploader
          withIcon={true}
          buttonText='Choose images'
          onChange={this.handleChange}
          imgExtension={['.jpg', '.png']}
          maxFileSize={5242880}
        />
        <header>
          My Pictures 
        </header>
      </>
    );
  }
}

export default App;

