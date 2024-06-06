import React from "react";
import {
  MDBContainer,
  MDBRow,
  MDBCol,
  MDBCard,
  MDBCardBody,
  MDBCardImage,
  MDBIcon,
} from "mdb-react-ui-kit";


const ProductCard = ({product}) => {
  return (
  
    <MDBCol md="4" lg="3" sm="6"   className="mb-4 mb-lg-0 col-6">
          <MDBCard >
            <MDBCardImage
              src="https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Products/4.webp"
              position="top"
              alt="Laptop"
            />
            <MDBCardBody>
              <div className="d-flex justify-content-between">
                <p className="small">
                  <a href="#!" className="text-muted">
                    {product.name}
                  </a>
                </p>
                <p className="small text-danger">
                  <s>$1099</s>
                </p>
              </div>

              <div className="d-flex justify-content-between mb-3">
                <p className="mb-0">{product.name}</p>
                <p className="text-dark mb-0">$ {product.price}</p>
              </div>

              <div class="d-flex justify-content-between mb-2">
                <p class="text-muted mb-0">
                  Available: <span class="fw-bold">6</span>
                </p>
                <div class="ms-auto text-warning ">
                  <MDBIcon fas icon="star" />
                  <MDBIcon fas icon="star" />
                  <MDBIcon fas icon="star" />
                  <MDBIcon fas icon="star" />
                  <MDBIcon fas icon="star" />
                </div>
              </div>
            <div class="d-flex flex-column mt-4">
                  <button class="btn btn-primary btn-sm" type="button">Add to cart</button>
                  <button class="btn btn-outline-primary btn-sm mt-2" type="button">
                    Add to wishlist
                  </button>
                </div>
            </MDBCardBody>
          </MDBCard>
        </MDBCol>
  )
}

export default ProductCard;
