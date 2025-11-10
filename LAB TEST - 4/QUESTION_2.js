function buildInitialProducts() {
  return {
    101: { name: "Espresso Machine", price: 12999, qty: 5 },
    102: { name: "Blender", price: 3499, qty: 10 },
    103: { name: "Toaster", price: 1999, qty: 0 },
    104: { name: "Air Fryer", price: 5499, qty: 3 },
  };
}

function processProducts(products) {
  products[105] = { name: "Slow Cooker", price: 2599, qty: 7 };
  products[101].qty += 2;

  for (const pid in products) {
    if (products[pid].qty === 0) {
      delete products[pid];
    }
  }

  let totalValue = 0;
  const expensiveItems = [];

  for (const pid in products) {
    const p = products[pid];
    totalValue += p.price * p.qty;
    if (p.price > 5000) {
      expensiveItems.push({ id: parseInt(pid), name: p.name, price: p.price });
    }
  }

  const sortedByPrice = Object.entries(products)
    .map(([id, p]) => ({ id: parseInt(id), ...p }))
    .sort((a, b) => b.price - a.price);

  return {
    products,
    total_value: totalValue,
    expensive_items: expensiveItems,
    sorted_by_price: sortedByPrice,
  };
}

const products = buildInitialProducts();
const result = processProducts(products);

console.log(JSON.stringify(result, null, 2));