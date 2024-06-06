import React, { useEffect, useState } from 'react';
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBCardImage,
  MDBIcon,
} from "mdb-react-ui-kit";


import ProductCard from './ProductCard';

const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await fetch('http://localhost:8000/products/');
        const data = await response.json(); // Use await here

        console.log(data);
        setProducts(data);
      } catch (error) {
        console.error('Error fetching products:', error);
      }
    };

    fetchProducts();
  }, []);

  return (
    <div>
      {/* Render your products here using the ProductCard component */}
      <MDBContainer fluid className="my-5">

        <h1 style={{textAlign:'start'}}>Top Rated</h1>
      <div className='scrolling-wrapper'>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
      
      </div>
      </MDBContainer>
    </div>
  );
};

export default Products;
