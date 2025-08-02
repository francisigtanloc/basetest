<template>
    <div>
      <div class="wrapper">
        <Sidebar />
        <main class="main-content">
          <Nuxt />
        </main>
        
  
        <!-- Custom template | don't include it in your project! -->
        <div class="custom-template">
          <div class="title">Settings</div>
          <div class="custom-content">
            <div class="switcher">
              <div class="switch-block">
                <h4>Logo Header</h4>
                <div class="btnSwitch">
                  <button
                    type="button"
                    class="selected changeLogoHeaderColor"
                    data-color="dark"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="blue"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="purple"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="light-blue"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="green"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="orange"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="red"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="white"
                  ></button>
                  <br />
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="dark2"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="blue2"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="purple2"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="light-blue2"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="green2"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="orange2"
                  ></button>
                  <button
                    type="button"
                    class="changeLogoHeaderColor"
                    data-color="red2"
                  ></button>
                </div>
              </div>
              <div class="switch-block">
                <h4>Navbar Header</h4>
                <div class="btnSwitch">
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="dark"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="blue"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="purple"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="light-blue"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="green"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="orange"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="red"
                  ></button>
                  <button
                    type="button"
                    class="selected changeTopBarColor"
                    data-color="white"
                  ></button>
                  <br />
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="dark2"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="blue2"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="purple2"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="light-blue2"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="green2"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="orange2"
                  ></button>
                  <button
                    type="button"
                    class="changeTopBarColor"
                    data-color="red2"
                  ></button>
                </div>
              </div>
              <div class="switch-block">
                <h4>Sidebar</h4>
                <div class="btnSwitch">
                  <button
                    type="button"
                    class="changeSideBarColor"
                    data-color="white"
                  ></button>
                  <button
                    type="button"
                    class="selected changeSideBarColor"
                    data-color="dark"
                  ></button>
                  <button
                    type="button"
                    class="changeSideBarColor"
                    data-color="dark2"
                  ></button>
                </div>
              </div>
            </div>
          </div>
          <div class="custom-toggle">
            <i class="icon-settings"></i>
          </div>
        </div>
        <!-- End Custom template -->
      </div>
      <!--   Core JS Files   -->
    </div>
</template>
  
<script>
    import '@basetest/assets/styles/bootstrap.min.css'
    import '@basetest/assets/styles/kaiadmin.css'
    import Sidebar from '@basetest/components/layouts/Sidebar.vue'
    import '@basetest/assets/styles/demo.css'
    import '@basetest/assets/styles/fonts.css'
    
    export default {
        name: 'MainLayout',
        ssr: false,
        layout: 'main',
        components: {
            Sidebar,
        },
        data() {
            return {}
        },
        head() {
            return {
            script: [
                {
                src: './assets/js/core/jquery-3.7.1.min.js',
                body: true,
                },
                {
                src: './assets/js/core/popper.min.js',
                body: true,
                },
                {
                src: './assets/js/core/bootstrap.min.js',
                body: true,
                },
                {
                src: './assets/js/plugin/jquery-scrollbar/jquery.scrollbar.min.js',
                body: true,
                },
                {
                src: './assets/js/plugin/jquery.sparkline/jquery.sparkline.min.js',
                body: true,
                },
                { src: './assets/js/kaiadmin.min.js', body: true },
                { src: './assets/js/demo.js', body: true },
            ],
            }
        },
        mounted() {
            this.$nextTick(() => {
            // Wait for jQuery to load
            const checkJQuery = setInterval(() => {
                if (window.$ !== undefined) {
                clearInterval(checkJQuery)

                // Initialize jQuery plugins
                $('[data-bs-toggle="tooltip"]').tooltip()
                $('[data-bs-toggle="popover"]').popover()

                // Initialize sparklines
                $('#lineChart').sparkline([102, 109, 120, 99, 110, 105, 115], {
                    type: 'line',
                    height: '70',
                    width: '100%',
                    lineWidth: '2',
                    lineColor: '#177dff',
                    fillColor: 'rgba(23, 125, 255, 0.14)',
                })

                $('#lineChart2').sparkline([99, 125, 122, 105, 110, 124, 115], {
                    type: 'line',
                    height: '70',
                    width: '100%',
                    lineWidth: '2',
                    lineColor: '#f3545d',
                    fillColor: 'rgba(243, 84, 93, .14)',
                })

                $('#lineChart3').sparkline([105, 103, 123, 100, 95, 105, 115], {
                    type: 'line',
                    height: '70',
                    width: '100%',
                    lineWidth: '2',
                    lineColor: '#ffa534',
                    fillColor: 'rgba(255, 165, 52, .14)',
                })
                }
            }, 100)
            })
        },    
    }
</script>
    
<style scoped>
    .dashboard-page {
        max-width: 1200px;
        margin: 0 auto;
    }
  </style>