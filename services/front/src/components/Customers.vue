<template>
  <div class="container">
    <h1>Clientes</h1>
    <div class="row">
      <div class="col-md-3">
        <h4 class="mb-3">Novo Cliente</h4>
        
        <label class="input-label" for="name">Nome</label>
        <input id="name" class="form-control mb-3" type="text" v-model="customer.firstName">
        
        <label class="input-label" for="lastName">Sobrenome</label>
        <input id="lastName" class="form-control mb-3" type="text" v-model="customer.lastName">

        <label class="input-label" for="street">Rua</label>
        <input id="street" class="form-control mb-3" type="text" v-model="customer.street">
        
        <label class="input-label" for="city">Cidade</label>
        <input id="city" class="form-control mb-3" type="text" v-model="customer.city">

        <label class="input-label" for="state">Estado</label>
        <input id="state" class="form-control mb-3" type="text" v-model="customer.state">

        <label class="input-label" for="country">País</label>
        <input id="country" class="form-control mb-3" type="text" v-model="customer.country">

        <label class="input-label" for="zip">CEP</label>
        <input id="zip" class="form-control" type="text" v-model="customer.zip">

        <button class="btn btn-primary m-3" v-on:click="newCustomer">Criar</button>
      </div>
      <div class="col-md-6 mx-auto">
        <div class="card mb-3" v-for="c in customers" :key="c.id">
          <div class="card-body">
            <span>{{ c.firstName + ' ' + c.lastName }}</span><br>
            <span>{{ c.street }}</span><br>
            <span>{{ c.city + ' - ' + c.state + ' - ' + c.country }}</span><br>
            <span>{{ c.zip }}</span>
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
  name: 'Customers',
  data() {
    return {
      customer: {},
      customers: [],
    }
  },
  created() {
    this.getCustomers();
  },
  methods: {
    getCustomers() {
      axios.get("http://192.168.49.2:32324/customers").then(({ data }) => {
        this.customers = data;
      });
    },
    newCustomer() {
      const data = this.customer;
      axios.post("http://192.168.49.2:32324/customers", data).then((res) => {
        console.log(res);
        window.alert("Cliente cadastrado!");
        this.getCustomers();
        this.customer = {};
      })
    }
  }
}
</script>


<style>
</style>
