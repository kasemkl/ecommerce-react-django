import React from 'react';
import { Fade } from 'react-slideshow-image';
import 'react-slideshow-image/dist/styles.css'
import 'react-animated-slider/build/horizontal.css';
import 'react-slideshow-image/dist/styles.css'
const slides = 
[{
    url: 'https://static.vecteezy.com/system/resources/previews/004/299/835/original/online-shopping-on-phone-buy-sell-business-digital-web-banner-application-money-advertising-payment-ecommerce-illustration-search-free-vector.jpg',
    caption: 'First Slide'
  },
  {
    url: 'https://static.vecteezy.com/system/resources/previews/001/937/856/large_2x/paper-art-shopping-online-on-smartphone-sale-promotion-backgroud-banner-for-market-ecommerce-free-vector.jpg',
    caption: 'Second Slide'
  },
  {
    url: 'https://static.vecteezy.com/system/resources/previews/002/006/774/large_2x/paper-art-shopping-online-on-smartphone-and-new-buy-sale-promotion-backgroud-for-banner-market-ecommerce-free-vector.jpg',
    caption: 'Third Slide'
  },
];

const fadeImages = [
  {
    url: 'https://images.unsplash.com/photo-1509721434272-b79147e0e708?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80',
    caption: 'First Slide'
  },
  {
    url: 'https://images.unsplash.com/photo-1506710507565-203b9f24669b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1536&q=80',
    caption: 'Second Slide'
  },
  {
    url: 'https://images.unsplash.com/photo-1536987333706-fc9adfb10d91?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1500&q=80',
    caption: 'Third Slide'
  },
];

const SlideShow = () => {
  return (
 
    
    <div className="slide-container">
      <Fade infinite duration={2000} transitionDuration={1000}>
        {slides.map((fadeImage, index) => (
          <div key={index}>
            <img style={{ width: '100%' ,maxHeight:'250px'}} src={fadeImage.url} />

          </div>
        ))}
      </Fade>
    </div>
  )
}

export default SlideShow;