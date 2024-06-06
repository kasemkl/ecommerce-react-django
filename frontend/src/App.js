import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './style/nav.css'
import './style/slide.css'
import './style/style.css'
import './style/products.css'
import NavBar from './components/NavBar';
import SlideShow from './components/SlideShow';
import Products from './components/Products';
// import SideBar from './components/SideBar';
import Sidebar from './components/Sidebar';
import TopRated from './components/TopRated'
function App() {
  return (
    <div className="App">
      {/* <SideBar/> */}
      {/* <Sidebar/> */}
      <NavBar/>
      <SlideShow/>
      <TopRated/>
      <Products/>
    </div>
  );
}

export default App;
