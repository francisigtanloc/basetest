<template>
  <div class="sidebar" data-background-color="dark">
    <div class="sidebar-logo">
      <!-- Logo Header -->
      <div class="logo-header" data-background-color="dark">
        <nuxt-link to="/kaiadmin/dashboard" class="logo">
          <img
            src="@basetest/assets/img/kaiadmin/logo_light.svg"
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
          <li class="nav-item" :class="{ active: isActive('/kaiadmin/dashboard') }">
            <a
              data-bs-toggle="collapse"
              data-bs-target="#dashboard"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-home"></i>
              <p>Dashboard</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="dashboard">
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
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#base" role="button">
              <i class="fas fa-layer-group"></i>
              <p>Base</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="base">
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
                  <nuxt-link to="/kaiadmin/components/font-awesome-icons">
                    <span class="sub-item">Font Awesome Icons</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/components/simple-line-icons">
                    <span class="sub-item">Simple Line Icons</span>
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
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#sidebarLayouts" role="button">
              <i class="fas fa-th-list"></i>
              <p>Sidebar Layouts</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="sidebarLayouts">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/layouts/sidebar-style-2">
                    <span class="sub-item">Sidebar Style 2</span>
                  </nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/kaiadmin/layouts/icon-menu">
                    <span class="sub-item">Icon Menu</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#forms" role="button">
              <i class="fas fa-pen-square"></i>
              <p>Forms</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="forms">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/kaiadmin/forms/basic">
                    <span class="sub-item">Basic Form</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#tables" role="button">
              <i class="fas fa-table"></i>
              <p>Tables</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="tables">
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
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#maps" role="button">
              <i class="fas fa-map-marker-alt"></i>
              <p>Maps</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="maps">
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
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#charts" role="button">
              <i class="far fa-chart-bar"></i>
              <p>Charts</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="charts">
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
          <li class="nav-item">
            <nuxt-link to="/kaiadmin/widgets">
              <i class="fas fa-desktop"></i>
              <p>Widgets</p>
              <span class="badge badge-success">4</span>
            </nuxt-link>
          </li>
          <li class="nav-item">
            <nuxt-link to="/kaiadmin/documentation">
              <i class="fas fa-file"></i>
              <p>Documentation</p>
              <span class="badge badge-secondary">1</span>
            </nuxt-link>
          </li>
          <li class="nav-item">
            <a data-bs-toggle="collapse" data-bs-target="#submenu" role="button">
              <i class="fas fa-bars"></i>
              <p>Menu Levels</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="submenu">
              <ul class="nav nav-collapse">
                <li>
                  <a data-bs-toggle="collapse" data-bs-target="#subnav1" role="button">
                    <span class="sub-item">Level 1</span>
                    <span class="caret"></span>
                  </a>
                  <div class="collapse" id="subnav1">
                    <ul class="nav nav-collapse subnav">
                      <li>
                        <a href="javascript:void(0)">
                          <span class="sub-item">Level 2</span>
                        </a>
                      </li>
                      <li>
                        <a href="javascript:void(0)">
                          <span class="sub-item">Level 2</span>
                        </a>
                      </li>
                    </ul>
                  </div>
                </li>
                <li>
                  <a href="#">
                    <span class="sub-item">Level 1</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'KaiAdminSidebar',
  mounted() {
    // Ensure Bootstrap collapse works after component mounts
    if (process.client) {
      this.$nextTick(() => {
        // Initialize Bootstrap collapse manually if needed
        setTimeout(() => {
          this.initializeCollapse()
        }, 1000)
      })
    }
  },
  methods: {
    isActive(route) {
      return this.$route.path === route
    },
    
    initializeCollapse() {
      // Manual fallback if Bootstrap collapse doesn't work
      const collapseElements = document.querySelectorAll('[data-bs-toggle="collapse"]')
      
      collapseElements.forEach(element => {
        element.addEventListener('click', (e) => {
          e.preventDefault() // Prevent default anchor behavior and scrolling
          
          const target = element.getAttribute('href') || element.getAttribute('data-bs-target')
          if (target && target.startsWith('#')) {
            const targetElement = document.querySelector(target)
            if (targetElement) {
              // Toggle collapse manually
              targetElement.classList.toggle('show')
              element.classList.toggle('collapsed')
              
              // Update aria-expanded
              const expanded = !targetElement.classList.contains('show')
              element.setAttribute('aria-expanded', expanded ? 'false' : 'true')
              
              console.log(`Toggled ${target}: ${targetElement.classList.contains('show') ? 'open' : 'closed'}`)
            }
          }
        })
      })
      
      console.log('Sidebar collapse initialized')
    }
  }
}
</script>

<style scoped>
/* Ensure collapse functionality works */
.collapse {
  display: none;
  transition: all 0.3s ease;
}

.collapse.show {
  display: block;
}

/* Caret rotation */
.collapsed .caret::before {
  transform: rotate(-90deg);
}

.caret {
  transition: transform 0.3s ease;
}

/* Smooth transitions */
.nav-collapse {
  overflow: hidden;
  transition: max-height 0.3s ease;
}

/* Custom macOS-style scrollbar */
.sidebar-wrapper::-webkit-scrollbar {
  width: 6px;
}

.sidebar-wrapper::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
}

.sidebar-wrapper::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.3);
  border-radius: 10px;
  transition: background 0.3s ease;
}

.sidebar-wrapper::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.5);
}

/* For Firefox */
.sidebar-wrapper {
  scrollbar-width: thin;
  scrollbar-color: rgba(255, 255, 255, 0.3) rgba(255, 255, 255, 0.1);
}

/* Smooth scrolling behavior */
.sidebar-wrapper {
  scroll-behavior: smooth;
}

/* Additional scrollbar styling for better visibility on dark background */
.scrollbar-inner::-webkit-scrollbar {
  width: 6px;
}

.scrollbar-inner::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
  margin: 5px;
}

.scrollbar-inner::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  transition: all 0.3s ease;
}

.scrollbar-inner::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.4);
  width: 8px;
}

.scrollbar-inner::-webkit-scrollbar-thumb:active {
  background: rgba(255, 255, 255, 0.6);
}
</style>