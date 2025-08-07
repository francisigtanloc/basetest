<template>
  <div class="container">
    <div class="page-inner">
      <div class="d-flex align-items-left align-items-md-center flex-column flex-md-row pt-2 pb-4">
        <div>
          <h3 class="fw-bold mb-3">Sample Components</h3>
          <h6 class="op-7 mb-2">KaiAdmin Template Components Showcase</h6>
        </div>
      </div>

      <!-- Stats Cards Row -->
      <div class="row">
        <div class="col-sm-6 col-md-3">
          <div class="card card-stats card-round">
            <div class="card-body">
              <div class="row align-items-center">
                <div class="col-icon">
                  <div class="icon-big text-center icon-primary bubble-shadow-small">
                    <i class="fas fa-users"></i>
                  </div>
                </div>
                <div class="col col-stats ms-3 ms-sm-0">
                  <div class="numbers">
                    <p class="card-category">Users</p>
                    <h4 class="card-title">1,294</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-md-3">
          <div class="card card-stats card-round">
            <div class="card-body">
              <div class="row align-items-center">
                <div class="col-icon">
                  <div class="icon-big text-center icon-info bubble-shadow-small">
                    <i class="fas fa-user-check"></i>
                  </div>
                </div>
                <div class="col col-stats ms-3 ms-sm-0">
                  <div class="numbers">
                    <p class="card-category">Active</p>
                    <h4 class="card-title">1,303</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-md-3">
          <div class="card card-stats card-round">
            <div class="card-body">
              <div class="row align-items-center">
                <div class="col-icon">
                  <div class="icon-big text-center icon-success bubble-shadow-small">
                    <i class="fas fa-chart-line"></i>
                  </div>
                </div>
                <div class="col col-stats ms-3 ms-sm-0">
                  <div class="numbers">
                    <p class="card-category">Growth</p>
                    <h4 class="card-title">+15%</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-md-3">
          <div class="card card-stats card-round">
            <div class="card-body">
              <div class="row align-items-center">
                <div class="col-icon">
                  <div class="icon-big text-center icon-secondary bubble-shadow-small">
                    <i class="far fa-check-circle"></i>
                  </div>
                </div>
                <div class="col col-stats ms-3 ms-sm-0">
                  <div class="numbers">
                    <p class="card-category">Complete</p>
                    <h4 class="card-title">576</h4>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Buttons and Components -->
      <div class="row mt-4">
        <div class="col-md-6">
          <div class="card card-round">
            <div class="card-header">
              <div class="card-title">Button Variants</div>
            </div>
            <div class="card-body">
              <div class="d-flex flex-wrap gap-2 mb-3">
                <button class="btn btn-primary">Primary</button>
                <button class="btn btn-secondary">Secondary</button>
                <button class="btn btn-success">Success</button>
                <button class="btn btn-danger">Danger</button>
                <button class="btn btn-warning">Warning</button>
                <button class="btn btn-info">Info</button>
              </div>
              
              <div class="d-flex flex-wrap gap-2 mb-3">
                <button class="btn btn-outline-primary">Primary</button>
                <button class="btn btn-outline-secondary">Secondary</button>
                <button class="btn btn-outline-success">Success</button>
                <button class="btn btn-outline-danger">Danger</button>
              </div>

              <div class="d-flex flex-wrap gap-2">
                <button class="btn btn-round btn-primary">Round Primary</button>
                <button class="btn btn-round btn-success">Round Success</button>
                <button class="btn btn-round btn-danger">Round Danger</button>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-6">
          <div class="card card-round">
            <div class="card-header">
              <div class="card-title">Badges and Labels</div>
            </div>
            <div class="card-body">
              <div class="mb-3">
                <h6>Badge Examples</h6>
                <span class="badge badge-primary me-2">Primary</span>
                <span class="badge badge-secondary me-2">Secondary</span>
                <span class="badge badge-success me-2">Success</span>
                <span class="badge badge-danger me-2">Danger</span>
                <span class="badge badge-warning me-2">Warning</span>
                <span class="badge badge-info">Info</span>
              </div>

              <div class="mb-3">
                <h6>Pills</h6>
                <span class="badge rounded-pill bg-primary me-2">Primary Pill</span>
                <span class="badge rounded-pill bg-success me-2">Success Pill</span>
                <span class="badge rounded-pill bg-warning me-2">Warning Pill</span>
                <span class="badge rounded-pill bg-danger">Danger Pill</span>
              </div>

              <div>
                <h6>With Icons</h6>
                <span class="badge badge-primary me-2">
                  <i class="fas fa-user me-1"></i>Users
                </span>
                <span class="badge badge-success me-2">
                  <i class="fas fa-check me-1"></i>Complete
                </span>
                <span class="badge badge-warning">
                  <i class="fas fa-exclamation me-1"></i>Warning
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Progress Bars and Alerts -->
      <div class="row mt-4">
        <div class="col-md-6">
          <div class="card card-round">
            <div class="card-header">
              <div class="card-title">Progress Bars</div>
            </div>
            <div class="card-body">
              <div class="mb-3">
                <div class="progress mb-2">
                  <div class="progress-bar" role="progressbar" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <div class="progress mb-2">
                  <div class="progress-bar bg-success" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <div class="progress mb-2">
                  <div class="progress-bar bg-info" role="progressbar" style="width: 75%" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
                <div class="progress">
                  <div class="progress-bar bg-warning" role="progressbar" style="width: 90%" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-md-6">
          <div class="card card-round">
            <div class="card-header">
              <div class="card-title">Alert Messages</div>
            </div>
            <div class="card-body">
              <div class="alert alert-primary mb-2" role="alert">
                <strong>Info!</strong> This is a primary alert.
              </div>
              <div class="alert alert-success mb-2" role="alert">
                <strong>Success!</strong> Your action was completed successfully.
              </div>
              <div class="alert alert-warning mb-2" role="alert">
                <strong>Warning!</strong> Please check your input.
              </div>
              <div class="alert alert-danger" role="alert">
                <strong>Error!</strong> Something went wrong.
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Form Elements -->
      <div class="row mt-4">
        <div class="col-12">
          <div class="card card-round">
            <div class="card-header">
              <div class="card-title">Form Elements</div>
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group">
                    <label for="exampleInput">Text Input</label>
                    <input type="text" class="form-control" id="exampleInput" placeholder="Enter text">
                  </div>
                  
                  <div class="form-group">
                    <label for="exampleSelect">Select Dropdown</label>
                    <select class="form-select" id="exampleSelect">
                      <option>Choose option</option>
                      <option>Option 1</option>
                      <option>Option 2</option>
                      <option>Option 3</option>
                    </select>
                  </div>

                  <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                      Default checkbox
                    </label>
                  </div>
                </div>

                <div class="col-md-6">
                  <div class="form-group">
                    <label for="exampleTextarea">Textarea</label>
                    <textarea class="form-control" id="exampleTextarea" rows="3" placeholder="Enter your message"></textarea>
                  </div>

                  <div class="form-group">
                    <label>Radio Buttons</label>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault1">
                      <label class="form-check-label" for="flexRadioDefault1">
                        Default radio
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="flexRadioDefault" id="flexRadioDefault2" checked>
                      <label class="form-check-label" for="flexRadioDefault2">
                        Default checked radio
                      </label>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SamplesPage',
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
.card-stats {
  border: none;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
}

.icon-big {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.icon-primary {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.icon-info {
  background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
  color: white;
}

.icon-success {
  background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
  color: #2d7a2d;
}

.icon-secondary {
  background: linear-gradient(135deg, #d299c2 0%, #fef9d7 100%);
  color: #6c757d;
}

.bubble-shadow-small {
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.gap-2 {
  gap: 0.5rem !important;
}
</style>