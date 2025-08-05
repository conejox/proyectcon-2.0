import { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/products/")
      .then(response => response.json())
      .then(data => setProducts(data))
      .catch(error => console.error("Error fetching products:", error));
  }, []);

  return (
    <div>
      <h1>Products</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <h3>{product.name} – ${product.price}</h3>
            {product.image && (
              <img
                src={`http://127.0.0.1:8000${product.image}`}
                alt={product.name}
                width="150"
              />
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
