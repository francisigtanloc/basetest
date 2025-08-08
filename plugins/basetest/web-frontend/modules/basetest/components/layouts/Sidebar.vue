<template>
  <!-- Sidebar -->
  <div class="sidebar" data-background-color="dark">
    <div class="sidebar-logo">
      <!-- Logo Header -->
      <div class="logo-header" data-background-color="dark">
        <nuxt-link to="/kaiadmin/dashboard" class="logo">
          <img
            src="/@basetest/assets/img/kaiadmin/logo_light.svg"
            alt="navbar brand"
            class="navbar-brand"
            height="20"
          />
        </nuxt-link>
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
      <!-- End Logo Header -->
    </div>
    <div class="sidebar-wrapper scrollbar scrollbar-inner">
      <div class="sidebar-content">
        <ul class="nav nav-secondary">
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/dashboard') }">
            <a
              data-bs-toggle="collapse"
              href="#dashboard"
              class="collapsed"
              aria-expanded="false"
            >
              <i class="fas fa-home"></i>
              <p>Dashboard</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/kaiadmin/dashboard') }" id="dashboard">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/dashboard">
                    <span class="sub-item">Dashboard 1</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-section">
            <span class="sidebar-mini-icon">
              <i class="fa fa-ellipsis-h"></i>
            </span>
            <h4 class="text-section">Components</h4>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/components') }">
            <a data-bs-toggle="collapse" href="#base">
              <i class="fas fa-layer-group"></i>
              <p>Base</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/kaiadmin/components') }" id="base">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/components/avatars">
                    <span class="sub-item">Avatars</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/buttons">
                    <span class="sub-item">Buttons</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/gridsystem">
                    <span class="sub-item">Grid System</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/panels">
                    <span class="sub-item">Panels</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/notifications">
                    <span class="sub-item">Notifications</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/sweetalert">
                    <span class="sub-item">Sweet Alert</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/icons">
                    <span class="sub-item">Font Awesome Icons</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/typography">
                    <span class="sub-item">Typography</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/forms') }">
            <a data-bs-toggle="collapse" href="#forms">
              <i class="fas fa-pen-square"></i>
              <p>Forms</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/kaiadmin/forms') }" id="forms">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/forms/basic">
                    <span class="sub-item">Basic Form</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/tables') }">
            <a data-bs-toggle="collapse" href="#tables">
              <i class="fas fa-table"></i>
              <p>Tables</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/kaiadmin/tables') }" id="tables">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/tables/basic">
                    <span class="sub-item">Basic Table</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/tables/datatables">
                    <span class="sub-item">Datatables</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/maps') }">
            <a data-bs-toggle="collapse" href="#maps">
              <i class="fas fa-map-marker-alt"></i>
              <p>Maps</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/kaiadmin/maps') }" id="maps">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/maps/googlemaps">
                    <span class="sub-item">Google Maps</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/maps/jsvectormap">
                    <span class="sub-item">Jsvectormap</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/charts') }">
            <a data-bs-toggle="collapse" href="#charts">
              <i class="far fa-chart-bar"></i>
              <p>Charts</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/kaiadmin/charts') }" id="charts">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/charts/chartjs">
                    <span class="sub-item">Chart Js</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/charts/sparkline">
                    <span class="sub-item">Sparkline</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/kaiadmin/widgets') }">
            <nuxt-link to="/kaiadmin/widgets">
              <i class="fas fa-desktop"></i>
              <p>Widgets</p>
              <span class="badge badge-success">4</span>
            </nuxt-link>
          </li>
          
          <li class="nav-item">
            <a href="#" @click.prevent="showDocumentation">
              <i class="fas fa-file"></i>
              <p>Documentation</p>
              <span class="badge badge-secondary">1</span>
            </a>
          </li>
          
          <li class="nav-section">
            <span class="sidebar-mini-icon">
              <i class="fa fa-ellipsis-h"></i>
            </span>
            <h4 class="text-section">Demo Pages</h4>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/demo') }">
            <a data-bs-toggle="collapse" href="#demoPages">
              <i class="fas fa-graduation-cap"></i>
              <p>Original Demo</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/demo') }" id="demoPages">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/demo/index">
                    <span class="sub-item">Demo Index</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/demo/users">
                    <span class="sub-item">Users</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/demo/courses">
                    <span class="sub-item">Courses</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          
          <li class="nav-item" :class="{ active: $route.path.includes('/samples') }">
            <a data-bs-toggle="collapse" href="#samplePages">
              <i class="fas fa-flask"></i>
              <p>Samples</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" :class="{ show: $route.path.includes('/samples') }" id="samplePages">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/samples">
                    <span class="sub-item">Sample Index</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/samples/home">
                    <span class="sub-item">Sample Home</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- End Sidebar -->
</template>

<script>
export default {
  name: 'Sidebar',
  methods: {
    showDocumentation() {
      this.$swal({
        title: 'Documentation',
        text: 'KAI Admin documentation would be available here.',
        type: 'info',
        confirmButtonText: 'OK'
      })
    }
  }
}
</script>