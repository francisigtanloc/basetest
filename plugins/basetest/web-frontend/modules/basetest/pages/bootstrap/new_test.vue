<template>
  <div class="container">
    <div class="page-inner">
      <div class="d-flex align-items-left align-items-md-center flex-column flex-md-row pt-2 pb-4">
        <div>
          <h3 class="fw-bold mb-3">Bootstrap Test Page</h3>
          <h6 class="op-7 mb-2">Testing Bootstrap Components Integration</h6>
        </div>
      </div>

      <!-- Hero Section -->
      <div class="row mb-4">
        <div class="col-12">
          <div class="card card-round">
            <div class="card-body p-5 bg-primary text-white text-center">
              <h1 class="text-white mb-3">Bootstrap Integration Test</h1>
              <p class="text-white-75">This page demonstrates the KaiAdmin template integration with Baserow.</p> 
            </div>
          </div>
        </div>
      </div>

      <!-- Content Cards -->
      <div class="row">
        <div class="col-sm-6 col-lg-4 mb-4">
          <div class="card card-round">
            <div class="card-body">
              <h5 class="card-title">Components</h5>
              <p class="card-text">Bootstrap components are working correctly with the KaiAdmin theme integration.</p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="text-muted">Bootstrap 5</small>
                <span class="badge badge-success">Active</span>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-lg-4 mb-4">
          <div class="card card-round">
            <div class="card-body">
              <h5 class="card-title">Responsive Design</h5>
              <p class="card-text">The layout adapts to different screen sizes using Bootstrap's responsive grid system.</p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="text-muted">Grid System</small>
                <span class="badge badge-primary">Responsive</span>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-lg-4 mb-4">
          <div class="card card-round">
            <div class="card-body">
              <h5 class="card-title">KaiAdmin Theme</h5>
              <p class="card-text">Custom styling from KaiAdmin template is properly integrated with Bootstrap classes.</p>
              <div class="d-flex justify-content-between align-items-center">
                <small class="text-muted">Theme Integration</small>
                <span class="badge badge-info">Styled</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Additional Features Row -->
      <div class="row">
        <div class="col-12">
          <div class="card card-round">
            <div class="card-header">
              <div class="card-title">Test Features</div>
            </div>
            <div class="card-body">
              <div class="row">
                <div class="col-md-6">
                  <h6>Typography & Colors</h6>
                  <p class="text-primary">Primary text color</p>
                  <p class="text-success">Success text color</p>
                  <p class="text-warning">Warning text color</p>
                  <p class="text-danger">Danger text color</p>
                </div>
                <div class="col-md-6">
                  <h6>Button Variants</h6>
                  <div class="btn-group-vertical w-100" role="group">
                    <button type="button" class="btn btn-primary mb-2">Primary Button</button>
                    <button type="button" class="btn btn-success mb-2">Success Button</button>
                    <button type="button" class="btn btn-warning mb-2">Warning Button</button>
                    <button type="button" class="btn btn-info">Info Button</button>
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
import '@basetest/assets/styles/bootstrap.min.css'

export default {
  name: 'BootstrapTest',
  layout: 'main',
  data() {
    return {}
  }
}
</script>
    
<style scoped>
.text-white-75 {
  color: rgba(255, 255, 255, 0.75) !important;
}

.card-round {
  border-radius: 0.75rem;
}

.badge {
  font-size: 0.75rem;
}

.btn-group-vertical .btn {
  border-radius: 0.375rem;
}
</style>