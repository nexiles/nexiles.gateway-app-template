<script setup>
 import { useQuasar } from 'quasar'

 import MyComponent from './components/SimpleCounter.vue'
 import MainPage from "./pages/MainPage.vue";

 const $q = useQuasar()
</script>


<template>
  <q-layout view="hHh lpR fFf">

    <q-header class="bg-light-green-4 text-grey-9" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="resources/img/logo.png">
          </q-avatar>
          nexiles|gateway app demo
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container class="bg-light-green-2">
      <MainPage />
    </q-page-container>

    <q-footer elevated class="bg-light-green-6 text-white">
        hello
    </q-footer>

  </q-layout>
</template>


<style scoped>
</style>
