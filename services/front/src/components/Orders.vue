<template>
  <div class="container">
    <h1>Pedidos</h1>
    <div class="row">
      <div class="col-md-3">
        <h4 class="mb-3">Novo Pedido</h4>
        
        <label class="input-label" for="customer">Cliente</label>
        <select id="customer" class="form-control mb-3" v-model="customer">
            <option value="">Selecione...</option>
            <option v-for="(c, i) in customers" :key="i" :value="c.id">
                {{ c.firstName + ' ' + c.lastName }}
            </option>
        </select>

        <label class="input-label" for="product1">Produto</label>
        <select id="product1" class="form-control mb-3" v-model="items[0].product" @change="calctotal">
            <option value="">Selecione...</option>
            <option v-for="(p, i) in products" :key="i" :value="p.id">
                {{ p.name + ' - R$' + p.cost }}
            </option>
        </select>
        <label class="input-label" for="q1">Quantidade</label>
        <input id="q1" class="form-control mb-3" type="number" v-model="items[0].quantity" @change="calctotal">

        <label class="input-label" for="product2">Produto</label>
        <select id="product2" class="form-control mb-3" v-model="items[1].product" @change="calctotal">
            <option value="">Selecione...</option>
            <option v-for="(p, i) in products" :key="i" :value="p.id">
                {{ p.name + ' - R$' + p.cost }}
            </option>
        </select>
        <label class="input-label" for="q2">Quantidade</label>
        <input id="q2" class="form-control mb-3" type="number" v-model="items[1].quantity" @change="calctotal">

        <label class="input-label" for="product3">Produto</label>
        <select id="product3" class="form-control mb-3" v-model="items[2].product" @change="calctotal">
            <option value="">Selecione...</option>
            <option v-for="(p, i) in products" :key="i" :value="p.id">
                {{ p.name + ' - R$' + p.cost }}
            </option>
        </select>
        <label class="input-label" for="q3">Quantidade</label>
        <input id="q3" class="form-control mb-3" type="number" v-model="items[2].quantity" @change="calctotal">
        
        <h5>Total: {{ total }}</h5>
        <button class="btn btn-primary m-1" v-on:click="newOrder">Criar</button>
      </div>
      
      <div class="col-md-6 mx-auto">
        <div class="card mb-3" v-for="o in orders" :key="o.id">
          <div class="card-body">
            <span>{{ getCustomer(o.customer) }}</span><br>
            <span>{{ o.date }}</span><br>
            <span class="mb-3" v-for="(i, j) in o.lineItems" :key="j">
                {{ getProduct(i.product).name + ' ' + i.quantity + 'x ' +  getProduct(i.product).cost }}<br>
            </span>
            <span>Total: R$ {{ o.total }}</span>
          </div>
        </div>
      </div>

      <div class="col-md-3">
        <h4>Navegação</h4>
        <router-link :to="'/'">Início</router-link><br>
        <router-link :to="'/products'">Produtos</router-link><br>
        <router-link :to="'/customers'">Clientes</router-link><br>
        <router-link :to="'/orders'">Pedidos</router-link><br>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'Products',
  data() {
    return {
      customer: "",
      customers: [],
      products: [],
      items: [{ product: "", quantity: 0}, { product: "", quantity: 0}, { product: "", quantity: 0}],
      orders: [],
      total: 0
    }
  },
  created() {
    this.getOrders();
    this.getProducts();
    this.getCustomers();
  },
  methods: {
    calctotal() {
      let a = 0;
      for(let i = 0; i < 3; i++) {
        let p = this.getProduct(this.items[i].product);
        if (p != undefined) a += this.items[i].quantity * p.cost;
      }
      this.total = a.toFixed(2);
    },
    getOrders() {
      axios.get("http://order-service:5050/orders").then(({ data }) => {
        this.orders = data;
      });
    },
    getCustomers() {
      axios.get("http://customer-service:5000/customers").then(({ data }) => {
        this.customers = data;
      });
    },
    getCustomer(id) {
        let filtered = this.customers.filter(c => c.id == id);
        return filtered.length ? filtered[0].firstName + " " + filtered[0].lastName : "??";
    },
    getProduct(id) {
        let filtered = this.products.filter(p => p.id == id);
        return filtered[0];
    },
    getProducts() {
      axios.get("http://product-service:5005/products").then(({ data }) => {
        this.products = data;
      });
    },
    newOrder() {
      this.calctotal()
      const data = {
        customer: this.customer,
        total: this.total,
        lineItems: this.items.filter(i => i.quantity > 0 && i.product != ""),
      };
      axios.post("http://order-service:5050/orders", data).then((res) => {
        console.log(res);
        window.alert("Pedido criado!");
        this.getORders();
        this.customer = "";
        this.total = 0;
        this.items = [{ product: "", quantity: 0}, { product: "", quantity: 0}, { product: "", quantity: 0}];
      })
    }
  }
}
</script>


<style>
</style>
