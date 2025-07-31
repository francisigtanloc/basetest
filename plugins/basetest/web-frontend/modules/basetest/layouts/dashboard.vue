<template>
    <div class="app-container">
      <Navbar />
      <div class="app-content">
        <Sidebar />
        <main class="main-content">
          <Nuxt />
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import Navbar from '@basetest/components/Navbar'
  import Sidebar from '@basetest/components/Sidebar'
  
  // import Toasts from '@baserow/modules/core/components/toasts/Toasts'
  
  export default {
    components: { Navbar, Sidebar },
    name: 'Dashboard',
    head() {
      return {
        script: [
          {
            src: 'https://cdn.tailwindcss.com',
            defer: true
          }
        ]
      }
    }
  }
  </script>
  
  <style>
  .app-container {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }
  
  .app-content {
    display: flex;
    flex: 1;
    margin-top: 60px; /* Navbar height */
  }
  
  .main-content {
    flex: 1;
    padding: 20px;
    background: #f8fafc;
    margin-left: 220px; /* Sidebar width */
    min-height: calc(100vh - 60px);
  }
  </style>