<template>
  <div class="container-fluid">
    <div class="page-inner">
      <!-- Hero Section -->
      <div class="row mb-5">
        <div class="col-12">
          <div class="hero-section bg-primary text-white rounded-4 p-5 text-center">
            <div class="container">
              <h1 class="display-4 fw-bold mb-4">Bootstrap 5 Sample Home</h1>
              <p class="lead mb-4">Welcome to the Bootstrap 5 sample page showcasing modern UI components and responsive design patterns</p>
              <div class="d-flex gap-3 justify-content-center">
                <button class="btn btn-light btn-lg">Get Started</button>
                <button class="btn btn-outline-light btn-lg">Learn More</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Feature Cards -->
      <div class="row mb-5">
        <div class="col-12 text-center mb-4">
          <h2 class="h1 fw-bold">Key Features</h2>
          <p class="text-muted">Discover what makes our Bootstrap 5 integration special</p>
        </div>
        
        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card h-100 shadow-sm border-0">
            <div class="card-body text-center p-4">
              <div class="feature-icon bg-primary bg-gradient text-white rounded-circle d-inline-flex align-items-center justify-content-center mb-3">
                <i class="fas fa-mobile-alt fa-2x"></i>
              </div>
              <h5 class="card-title fw-bold">Responsive Design</h5>
              <p class="card-text text-muted">Built with mobile-first approach ensuring perfect display across all devices and screen sizes.</p>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card h-100 shadow-sm border-0">
            <div class="card-body text-center p-4">
              <div class="feature-icon bg-success bg-gradient text-white rounded-circle d-inline-flex align-items-center justify-content-center mb-3">
                <i class="fas fa-rocket fa-2x"></i>
              </div>
              <h5 class="card-title fw-bold">Fast Performance</h5>
              <p class="card-text text-muted">Optimized code and modern CSS techniques deliver lightning-fast loading times.</p>
            </div>
          </div>
        </div>

        <div class="col-lg-4 col-md-6 mb-4">
          <div class="card h-100 shadow-sm border-0">
            <div class="card-body text-center p-4">
              <div class="feature-icon bg-info bg-gradient text-white rounded-circle d-inline-flex align-items-center justify-content-center mb-3">
                <i class="fas fa-palette fa-2x"></i>
              </div>
              <h5 class="card-title fw-bold">Modern Design</h5>
              <p class="card-text text-muted">Contemporary UI components with smooth animations and intuitive user experience.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Statistics Section -->
      <div class="row mb-5">
        <div class="col-12">
          <div class="card bg-dark text-white rounded-4 overflow-hidden">
            <div class="card-body p-5">
              <div class="row text-center">
                <div class="col-md-3 col-6 mb-4">
                  <div class="stat-item">
                    <h2 class="display-4 fw-bold text-primary mb-0">150+</h2>
                    <p class="text-white-50 mb-0">Components</p>
                  </div>
                </div>
                <div class="col-md-3 col-6 mb-4">
                  <div class="stat-item">
                    <h2 class="display-4 fw-bold text-success mb-0">25K+</h2>
                    <p class="text-white-50 mb-0">Downloads</p>
                  </div>
                </div>
                <div class="col-md-3 col-6 mb-4">
                  <div class="stat-item">
                    <h2 class="display-4 fw-bold text-warning mb-0">95%</h2>
                    <p class="text-white-50 mb-0">Satisfaction</p>
                  </div>
                </div>
                <div class="col-md-3 col-6 mb-4">
                  <div class="stat-item">
                    <h2 class="display-4 fw-bold text-info mb-0">24/7</h2>
                    <p class="text-white-50 mb-0">Support</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Carousel Section -->
      <div class="row mb-5">
        <div class="col-12">
          <h3 class="fw-bold text-center mb-4">Image Carousel</h3>
          <div id="sampleCarousel" class="carousel slide" data-bs-ride="carousel">
            <div class="carousel-indicators">
              <button type="button" data-bs-target="#sampleCarousel" data-bs-slide-to="0" class="active"></button>
              <button type="button" data-bs-target="#sampleCarousel" data-bs-slide-to="1"></button>
              <button type="button" data-bs-target="#sampleCarousel" data-bs-slide-to="2"></button>
            </div>
            <div class="carousel-inner rounded-3">
              <div class="carousel-item active">
                <div class="bg-primary d-flex align-items-center justify-content-center text-white" style="height: 300px;">
                  <div class="text-center">
                    <h4>First Slide</h4>
                    <p>Beautiful carousel component with Bootstrap 5</p>
                  </div>
                </div>
              </div>
              <div class="carousel-item">
                <div class="bg-success d-flex align-items-center justify-content-center text-white" style="height: 300px;">
                  <div class="text-center">
                    <h4>Second Slide</h4>
                    <p>Responsive and touch-friendly navigation</p>
                  </div>
                </div>
              </div>
              <div class="carousel-item">
                <div class="bg-info d-flex align-items-center justify-content-center text-white" style="height: 300px;">
                  <div class="text-center">
                    <h4>Third Slide</h4>
                    <p>Smooth transitions and modern design</p>
                  </div>
                </div>
              </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#sampleCarousel" data-bs-slide="prev">
              <span class="carousel-control-prev-icon"></span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#sampleCarousel" data-bs-slide="next">
              <span class="carousel-control-next-icon"></span>
            </button>
          </div>
        </div>
      </div>

      <!-- Accordion Section -->
      <div class="row mb-5">
        <div class="col-lg-6">
          <h4 class="fw-bold mb-3">Frequently Asked Questions</h4>
          <div class="accordion" id="faqAccordion">
            <div class="accordion-item">
              <h2 class="accordion-header">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne">
                  What is Bootstrap 5?
                </button>
              </h2>
              <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#faqAccordion">
                <div class="accordion-body">
                  Bootstrap 5 is the latest version of the world's most popular CSS framework for building responsive, mobile-first websites.
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo">
                  How is it integrated with Vue.js?
                </button>
              </h2>
              <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                <div class="accordion-body">
                  Bootstrap 5 CSS and JS are imported into Vue.js components, allowing you to use all Bootstrap classes and components seamlessly.
                </div>
              </div>
            </div>
            <div class="accordion-item">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree">
                  Is it mobile responsive?
                </button>
              </h2>
              <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#faqAccordion">
                <div class="accordion-body">
                  Yes, Bootstrap 5 is built with a mobile-first approach and provides excellent responsive behavior across all devices.
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-lg-6">
          <h4 class="fw-bold mb-3">Contact Form</h4>
          <form class="bg-light p-4 rounded-3">
            <div class="mb-3">
              <label for="name" class="form-label">Full Name</label>
              <input type="text" class="form-control" id="name" placeholder="Enter your full name">
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Email Address</label>
              <input type="email" class="form-control" id="email" placeholder="Enter your email">
            </div>
            <div class="mb-3">
              <label for="subject" class="form-label">Subject</label>
              <select class="form-select" id="subject">
                <option selected>Choose a subject</option>
                <option value="general">General Inquiry</option>
                <option value="support">Technical Support</option>
                <option value="feedback">Feedback</option>
              </select>
            </div>
            <div class="mb-3">
              <label for="message" class="form-label">Message</label>
              <textarea class="form-control" id="message" rows="4" placeholder="Type your message here"></textarea>
            </div>
            <div class="mb-3 form-check">
              <input type="checkbox" class="form-check-input" id="newsletter">
              <label class="form-check-label" for="newsletter">
                Subscribe to our newsletter
              </label>
            </div>
            <button type="submit" class="btn btn-primary w-100">Send Message</button>
          </form>
        </div>
      </div>

      <!-- Modal Trigger -->
      <div class="row mb-5">
        <div class="col-12 text-center">
          <h4 class="fw-bold mb-3">Modal Example</h4>
          <button type="button" class="btn btn-lg btn-outline-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
            Launch Demo Modal
          </button>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1">
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Bootstrap 5 Modal</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <p>This is a sample modal dialog built with Bootstrap 5. It demonstrates the modal component with modern styling and smooth animations.</p>
            <div class="alert alert-info mb-0">
              <i class="fas fa-info-circle me-2"></i>
              Modals are fully accessible and keyboard navigable.
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save Changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SamplesHome',
  data() {
    return {}
  },
  mounted() {
    // Client-side only: Import Bootstrap CSS and JS
    if (process.client) {
      // Import Bootstrap CSS
      import('@basetest/assets/bootstrap5/css/bootstrap.min.css')
      
      // Import Bootstrap JS
      import('@basetest/assets/bootstrap5/js/bootstrap.bundle.min.js').then(bootstrap => {
        console.log('Bootstrap 5 loaded successfully')
        // Bootstrap components are now available
        if (window.bootstrap) {
          console.log('Bootstrap components initialized')
        }
      }).catch(err => {
        console.error('Bootstrap loading failed:', err)
      })
    }
  }
}
</script>

<style scoped>
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto;
}

.card {
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.15);
}

.stat-item h2 {
  font-size: 3rem;
}

.carousel-item div {
  background: linear-gradient(45deg, var(--bs-primary), var(--bs-primary-rgb));
}

.accordion-button:not(.collapsed) {
  background-color: rgba(13, 110, 253, 0.1);
  border-color: rgba(13, 110, 253, 0.2);
}

.bg-gradient {
  background-image: linear-gradient(180deg, rgba(255, 255, 255, 0.15), rgba(255, 255, 255, 0));
}

@media (max-width: 768px) {
  .display-4 {
    font-size: 2rem;
  }
  
  .hero-section {
    padding: 2rem !important;
  }
  
  .stat-item h2 {
    font-size: 2rem;
  }
}
</style>