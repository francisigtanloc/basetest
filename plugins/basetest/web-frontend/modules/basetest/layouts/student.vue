<template>
  <div>
    <div class="wrapper">
      <StudentSidebar />
      <div class="main-panel">
        <KaiAdminNavbar />
        <div class="container">
          <div class="page-inner">
            <Nuxt />
          </div>
        </div>
        <KaiAdminFooter />
      </div>
    </div>
  </div>
</template>

<script>
import StudentSidebar from '@basetest/components/kaiadmin/StudentSidebar.vue'
import KaiAdminNavbar from '@basetest/components/kaiadmin/KaiAdminNavbar.vue'  
import KaiAdminFooter from '@basetest/components/kaiadmin/KaiAdminFooter.vue'

export default {
  name: 'StudentLayout',
  components: {
    StudentSidebar,
    KaiAdminNavbar,
    KaiAdminFooter
  },
  head() {
    return {
      title: 'Student Portal - Learning Management System',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1.0, shrink-to-fit=no' },
        { 'http-equiv': 'X-UA-Compatible', content: 'IE=edge' }
      ],
      link: [
        { rel: 'icon', href: '/static/@basetest/assets/img/kaiadmin/favicon.ico', type: 'image/x-icon' },
      ],
    }
  },
  mounted() {
    // Client-side only: Load KAI Admin assets
    if (process.client) {
      this.loadKaiAdminCSS()
      this.loadKaiAdminAssets()
    }
  },
  methods: {
    async loadKaiAdminCSS() {
      try {
        console.log('Loading KAI Admin CSS assets...')
        // Load CSS files using dynamic imports like other working pages
        await import('@basetest/assets/styles/bootstrap.min.css')
        await import('@basetest/assets/styles/fonts.min.css')
        await import('@basetest/assets/styles/kaiadmin.min.css')
        await import('@basetest/assets/styles/demo.css')
        console.log('KAI Admin CSS loaded successfully')
      } catch (error) {
        console.error('Failed to load KAI Admin CSS:', error)
      }
    },
    
    async loadKaiAdminAssets() {
      try {
        console.log('Loading KAI Admin JavaScript assets...')
        
        // Load WebFont first (if not already loaded via head)
        if (!document.querySelector('script[src="@basetest/assets/js/plugin/webfont/webfont.min.js"]')) {
          await this.loadScript('@basetest/assets/js/plugin/webfont/webfont.min.js')
        }
        
        // Initialize WebFont (if not already initialized)
        if (window.WebFont && !sessionStorage.fonts) {
          window.WebFont.load({
            google: { families: ["Public Sans:300,400,500,600,700"] },
            custom: {
              families: [
                "Font Awesome 5 Solid",
                "Font Awesome 5 Regular", 
                "Font Awesome 5 Brands",
                "simple-line-icons",
              ],
              urls: ["@basetest/assets/styles/fonts.min.css"],
            },
            active: function () {
              sessionStorage.fonts = true
            },
          })
        }
        
        // Load core JS libraries in sequence
        await this.loadScript('@basetest/assets/js/core/jquery-3.7.1.min.js')
        await this.loadScript('@basetest/assets/js/core/popper.min.js') 
        await this.loadScript('@basetest/assets/js/core/bootstrap.min.js')
        await this.loadScript('@basetest/assets/js/plugin/jquery-scrollbar/jquery.scrollbar.min.js')
        await this.loadScript('@basetest/assets/js/kaiadmin.min.js')
        
        console.log('KAI Admin JS loaded successfully')
        
        // Initialize KAI Admin after all scripts loaded
        this.$nextTick(() => {
          this.initializeKaiAdmin()
        })
        
      } catch (error) {
        console.error('Failed to load KAI Admin JavaScript assets:', error)
        // Initialize basic functionality even if some assets fail
        this.$nextTick(() => {
          this.initializeKaiAdmin()
        })
      }
    },
    
    loadScript(src) {
      return new Promise((resolve, reject) => {
        const existing = document.querySelector(`script[src="${src}"]`)
        if (existing) {
          resolve()
          return
        }
        
        const script = document.createElement('script')
        script.src = src
        script.onload = resolve
        script.onerror = reject
        document.body.appendChild(script)
      })
    },
    
    initializeKaiAdmin() {
      // Initialize sidebar toggle functionality
      if (window.$ && window.jQuery) {
        console.log('Initializing KAI Admin components with jQuery')
        
        // Initialize sidebar toggles
        $('.sidenav-toggler').click(function() {
          $('body').toggleClass('sidebar_minimize')
        })
        
        $('.toggle-sidebar').click(function() {
          $('body').toggleClass('toggle-sidebar')
        })
        
        // Initialize scrollbar
        if ($.fn.scrollbar) {
          $('.scrollbar-inner').scrollbar()
        }
        
        // Initialize Bootstrap tooltips
        if (window.bootstrap && document.querySelectorAll('[data-bs-toggle="tooltip"]').length) {
          var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
          tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new window.bootstrap.Tooltip(tooltipTriggerEl)
          })
        }
        
        // Initialize dropdowns
        if (window.bootstrap && document.querySelectorAll('.dropdown-toggle').length) {
          var dropdownElementList = [].slice.call(document.querySelectorAll('.dropdown-toggle'))
          dropdownElementList.map(function (dropdownToggleEl) {
            return new window.bootstrap.Dropdown(dropdownToggleEl)
          })
        }
      }
    }
  }
}
</script>