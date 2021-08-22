<template>
  <div class="hello">
    <h1>Exemplo de Microserviços e Service Mesh</h1>
    <p>
      Para mais informações, visite o repositório
      <a href="https://github.com/camalejao/service-mesh" target="_blank" rel="noopener">no GitHub</a>.
    </p>
    <div class="">
      <h4>Navegação</h4>
      <router-link :to="'/'">Início</router-link><br>
      <router-link :to="'/products'">Produtos</router-link><br>
      <router-link :to="'/customers'">Clientes</router-link><br>
      <router-link :to="'/orders'">Pedidos</router-link><br>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
</style>
