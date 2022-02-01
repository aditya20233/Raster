import {Component} from 'react'
import GeoTIFF, { fromUrl, fromUrls, fromArrayBuffer, fromBlob } from 'geotiff';
import './App.css'

class App extends Component {
  state = {
    img: "",
  }

 change=async(event)=>{
  const tiff = await fromBlob(event.target.files[0]);
  const image = await tiff.getImage();
  const data = await image.readRasters();
  console.log(data[0])
}
  
  render() {
    const {img} = this.state
    return (
      <input type="file" id="file" onChange={this.change}/>
    )
  }
}

export default App