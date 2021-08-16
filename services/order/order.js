const express = require("express");
const uuid = require("uuid");
const fs = require("fs");

const app = express();

app.use(express.json());

app.get("/orders", (req, res) => {

    const data = fs.readFileSync('orders.json');
    const orders = JSON.parse(data);

    return res.json(orders);
});

app.get("/orders/:id", (req, res) => {

    const { id } = req.params;

    const data = fs.readFileSync('orders.json');
    const orders = JSON.parse(data);

    const order = orders.find(ord => ord.id == id);

    if (order) {
        return res.json(order);
    } else {
        return res.status(404).json({'error': 'not found'});
    }
});

app.post("/orders", (req, res) => {
    
    const { customer, total, lineItems } = req.body;

    const order = {
        id: uuid.v4(),
        date: (new Date).toLocaleDateString('pt-BR'),
        total,
        customer,
        lineItems
    }

    const data = fs.readFileSync('orders.json');
    const orders = JSON.parse(data);

    orders.push(order);

    fs.writeFileSync('orders.json', JSON.stringify(orders));

    return res.status(201).json({'order': order});
});

app.listen(5050);