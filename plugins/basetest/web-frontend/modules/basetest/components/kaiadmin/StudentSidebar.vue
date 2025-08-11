<template>
  <div class="sidebar" data-background-color="dark">
    <div class="sidebar-logo">
      <!-- Logo Header -->
      <div class="logo-header" data-background-color="dark">
        <nuxt-link to="/student/dashboard" class="logo">
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
          <!-- Dashboard -->
          <li class="nav-item" :class="{ active: isActive('/student/dashboard') }">
            <a
              @click="toggleCollapse('dashboard')"
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
                  <nuxt-link to="/student/dashboard">
                    <span class="sub-item">Overview</span>
                  </nuxt-link>
                </li>
              </ul>
            </div>
          </li>

          <!-- My Courses -->
          <li class="nav-item" :class="{ active: isActive('/student/courses') }">
            <a
              @click="toggleCollapse('courses')"
              data-bs-target="#courses"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-book-open"></i>
              <p>My Courses</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="courses">
              <ul class="nav nav-collapse">
                <li>
                  <nuxt-link to="/student/courses">
                    <span class="sub-item">All Courses</span>
                  </nuxt-link>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">In Progress</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Completed</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>

          <!-- Assignments -->
          <li class="nav-item">
            <a
              @click="toggleCollapse('assignments')"
              data-bs-target="#assignments"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-tasks"></i>
              <p>Assignments</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="assignments">
              <ul class="nav nav-collapse">
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Pending</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Submitted</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Graded</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>

          <!-- Grades -->
          <li class="nav-item">
            <a
              @click="toggleCollapse('grades')"
              data-bs-target="#grades"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-chart-line"></i>
              <p>Grades</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="grades">
              <ul class="nav nav-collapse">
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Grade Report</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Transcripts</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>

          <!-- Calendar -->
          <li class="nav-item">
            <a href="#" @click.prevent="showNotImplemented">
              <i class="fas fa-calendar-alt"></i>
              <p>Calendar</p>
            </a>
          </li>

          <!-- Messages -->
          <li class="nav-item">
            <a href="#" @click.prevent="showNotImplemented">
              <i class="fas fa-envelope"></i>
              <p>Messages</p>
              <span class="badge badge-success" v-if="unreadMessages > 0">{{ unreadMessages }}</span>
            </a>
          </li>

          <!-- Resources -->
          <li class="nav-item">
            <a
              @click="toggleCollapse('resources')"
              data-bs-target="#resources"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-folder"></i>
              <p>Resources</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="resources">
              <ul class="nav nav-collapse">
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Library</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Downloads</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Study Materials</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>

          <!-- Settings -->
          <li class="nav-item">
            <a
              @click="toggleCollapse('settings')"
              data-bs-target="#settings"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-cog"></i>
              <p>Settings</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="settings">
              <ul class="nav nav-collapse">
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Profile</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Preferences</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Notifications</span>
                  </a>
                </li>
              </ul>
            </div>
          </li>

          <!-- Help & Support -->
          <li class="nav-item">
            <a
              @click="toggleCollapse('help')"
              data-bs-target="#help"
              class="collapsed"
              aria-expanded="false"
              role="button"
            >
              <i class="fas fa-question-circle"></i>
              <p>Help & Support</p>
              <span class="caret"></span>
            </a>
            <div class="collapse" id="help">
              <ul class="nav nav-collapse">
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">FAQ</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">Contact Support</span>
                  </a>
                </li>
                <li>
                  <a href="#" @click.prevent="showNotImplemented">
                    <span class="sub-item">User Guide</span>
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
  name: 'StudentSidebar',
  data() {
    return {
      unreadMessages: 3 // Mock data
    }
  },
  mounted() {
    this.initializeSidebar()
  },
  methods: {
    isActive(path) {
      return this.$route.path === path || this.$route.path.startsWith(path + '/')
    },
    
    toggleCollapse(targetId) {
      if (process.client) {
        const targetElement = document.getElementById(targetId)
        if (targetElement) {
          // Toggle Bootstrap collapse
          if (window.bootstrap && window.bootstrap.Collapse) {
            const bsCollapse = new window.bootstrap.Collapse(targetElement, {
              toggle: true
            })
          } else {
            // Fallback manual toggle
            targetElement.classList.toggle('show')
          }
        }
      }
    },
    
    initializeSidebar() {
      if (process.client) {
        // Prevent default anchor behavior and implement proper navigation
        const menuLinks = document.querySelectorAll('.sidebar a[data-bs-target]')
        
        menuLinks.forEach(element => {
          element.addEventListener('click', (e) => {
            e.preventDefault() // Prevent default anchor behavior and scrolling
            const target = element.getAttribute('href') || element.getAttribute('data-bs-target')
            if (target && target.startsWith('#')) {
              const targetElement = document.querySelector(target)
              if (targetElement) {
                targetElement.classList.toggle('show')
                element.classList.toggle('collapsed')
              }
            }
          })
        })
        
        // Load CSS dynamically
        this.loadSidebarCSS()
      }
    },
    
    async loadSidebarCSS() {
      try {
        // Import the Bootstrap CSS if not already loaded
        await import('@basetest/assets/styles/bootstrap.min.css')
      } catch (error) {
        console.error('Failed to load sidebar CSS:', error)
      }
    },
    
    showNotImplemented() {
      if (this.$swal) {
        this.$swal({
          title: 'Coming Soon',
          text: 'This feature is currently under development and will be available soon.',
          type: 'info',
          confirmButtonText: 'OK'
        })
      } else {
        alert('This feature is currently under development and will be available soon.')
      }
    }
  }
}
</script>

<style scoped>
/* Custom scrollbar for sidebar like macOS */
.sidebar-wrapper::-webkit-scrollbar {
  width: 8px;
}

.sidebar-wrapper::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
  border-radius: 10px;
}

.sidebar-wrapper::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.15);
  border-radius: 10px;
  transition: all 0.3s ease;
}

.sidebar-wrapper::-webkit-scrollbar-thumb:hover {
  background: rgba(255, 255, 255, 0.25);
}

/* Active menu item styling */
.nav-item.active > a {
  background-color: rgba(255, 255, 255, 0.1);
  color: #fff;
}

/* Badge styling for notifications */
.badge {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 10px;
  padding: 2px 6px;
}

/* Smooth transitions for menu items */
.nav-item a {
  transition: all 0.3s ease;
}

.nav-item a:hover {
  background-color: rgba(255, 255, 255, 0.05);
  color: #fff;
}

/* Collapse animation */
.collapse {
  transition: all 0.3s ease;
}

.collapse.show {
  background-color: rgba(0, 0, 0, 0.1);
}
</style>