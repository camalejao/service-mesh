<template>
  <div class="container">
    <h1>Produtos</h1>
    <div class="row">
      <div class="col-md-3">
        <h4 class="mb-3">Novo Produto</h4>
        <label class="input-label" for="name">Nome</label>
        <input id="name" class="form-control mb-3" type="text" v-model="name">
        <label class="input-label" for="cost">Valor</label>
        <input id="cost" class="form-control" type="text" v-model="cost">
        <button class="btn btn-primary m-3" v-on:click="newProduct">Criar</button>
      </div>
      <div class="col-md-6 mx-auto">
        <div class="card mb-3" v-for="p in products" :key="p.id">
          <div class="card-body">
            <span>{{ p.name }}</span><br>
            <span>R$ {{ p.cost }}</span>
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
      name: "",
      cost: "",
      products: [],
    }
  },
  created() {
    this.getProducts();
  },
  methods: {
    getProducts() {
      axios.get("http://product-service:5005/products").then(({ data }) => {
        this.products = data;
      });
    },
    newProduct() {
      const data = {
        name: this.name,
        cost: parseFloat(this.cost),
      };
      axios.post("http://product-service:5005/products", data).then((res) => {
        console.log(res);
        window.alert("Produto criado!");
        this.getProducts();
        this.name = "";
        this.cost = "";
      })
    }
  }
}
</script>


<style>
</style>
