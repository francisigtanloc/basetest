<template>
    <div>
      <div class="wrapper">
        <Sidebar />
        <div class="main-panel">
          <div class="main-header">
            <div class="main-header-logo">
              <!-- Logo Header -->
              <div class="logo-header" data-background-color="dark">
                <a href="index.html" class="logo">
                  <img
                    src="@basetest/assets/img/kaiadmin/logo_light.svg"
                    alt="navbar brand"
                    class="navbar-brand"
                    height="20"
                  />
                </a>
                <div class="nav-toggle">
                  <button class="btn btn-toggle toggle-sidebar">
                    <i class="gg-menu-right"></i>
                  </button>
                  <button class="btn btn-toggle sidenav-toggler">
                    <i class="gg-menu-left"></i>
                  </button>
                </div>
                <button class="topbar-toggler more">
                  <i class="gg-more-vertical-alt"></i>
                </button>
              </div>
            </div>
            <!-- Navbar Header -->
            <nav class="navbar navbar-header navbar-header-transparent navbar-expand-lg border-bottom">
              <div class="container-fluid">
                <nav class="navbar navbar-header-left navbar-expand-lg navbar-form nav-search p-0 d-none d-lg-flex">
                  <div class="input-group">
                    <div class="input-group-prepend">
                      <button type="submit" class="btn btn-search pe-1">
                        <i class="fa fa-search search-icon"></i>
                      </button>
                    </div>
                    <input type="text" placeholder="Search ..." class="form-control" />
                  </div>
                </nav>
                <ul class="navbar-nav topbar-nav ms-md-auto align-items-center">
                  <li class="nav-item topbar-user dropdown hidden-caret">
                    <a class="dropdown-toggle profile-pic" data-bs-toggle="dropdown" href="#" aria-expanded="false">
                      <div class="avatar-sm">
                        <img src="@basetest/assets/img/profile.jpg" alt="..." class="avatar-img rounded-circle" />
                      </div>
                      <span class="profile-username">
                        <span class="op-7">Hi,</span>
                        <span class="fw-bold">User</span>
                      </span>
                    </a>
                  </li>
                </ul>
              </div>
            </nav>
          </div>
          <main class="main-content">
            <Nuxt />
          </main>
          <footer class="footer">
            <div class="container-fluid d-flex justify-content-between">
              <nav class="pull-left">
                <ul class="nav">
                  <li class="nav-item">
                    <a class="nav-link" href="#">BaseTest Plugin</a>
                  </li>
                </ul>
              </nav>
              <div class="copyright">
                2024, powered by BaseRow
              </div>
            </div>
          </footer>
        </div>
        
  
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
    import '@basetest/assets/styles/fonts.min.css'
    import '@basetest/assets/styles/kaiadmin.min.css'
    import '@basetest/assets/styles/demo.css'
    import Sidebar from '@basetest/components/layouts/Sidebar.vue'
    
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
                src: '/@basetest/assets/js/core/jquery-3.7.1.min.js',
                body: true,
                },
                {
                src: '/@basetest/assets/js/core/popper.min.js',
                body: true,
                },
                {
                src: '/@basetest/assets/js/core/bootstrap.min.js',
                body: true,
                },
                {
                src: '/@basetest/assets/js/plugin/jquery-scrollbar/jquery.scrollbar.min.js',
                body: true,
                },
                {
                src: '/@basetest/assets/js/plugin/jquery.sparkline/jquery.sparkline.min.js',
                body: true,
                },
                { src: '/@basetest/assets/js/kaiadmin.min.js', body: true },
                { src: '/@basetest/assets/js/demo.js', body: true },
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