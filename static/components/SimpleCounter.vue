<script setup>
 import { ref } from 'vue'
 const count = ref(0)

 console.log("MyComponent")
</script>

<template>
    <div class="q-ma-md">
        <q-btn color="primary" @click="count++">Count is: {{ count }}</q-btn>
    </div>
</template>

<style scoped>
</style>
