<template>
  <div>
    <div class="container">
      <div class="page-inner">
        <div class="page-header">
          <h3 class="fw-bold mb-3">Buttons</h3>
          <ul class="breadcrumbs mb-3">
            <li class="nav-home">
              <nuxt-link to="/kaiadmin/dashboard">
                <i class="icon-home"></i>
              </nuxt-link>
            </li>
            <li class="separator">
              <i class="icon-arrow-right"></i>
            </li>
            <li class="nav-item">
              <nuxt-link to="#">Base</nuxt-link>
            </li>
            <li class="separator">
              <i class="icon-arrow-right"></i>
            </li>
            <li class="nav-item">
              <a href="#">Buttons</a>
            </li>
          </ul>
        </div>
        
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Basic Buttons</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <button class="btn btn-primary">Primary</button>
                  <button class="btn btn-secondary">Secondary</button>
                  <button class="btn btn-info">Info</button>
                  <button class="btn btn-success">Success</button>
                  <button class="btn btn-warning">Warning</button>
                  <button class="btn btn-danger">Danger</button>
                  <button class="btn btn-light">Light</button>
                  <button class="btn btn-dark">Dark</button>
                  <button class="btn btn-link">Link</button>
                </p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Button States</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <button class="btn btn-primary" disabled>Disabled</button>
                  <button class="btn btn-primary">
                    <span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>
                    Loading
                  </button>
                  <button class="btn btn-primary btn-loading" data-loading-text="Loading">
                    <i class="fas fa-spinner fa-spin me-2"></i>
                    With Icon
                  </button>
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Button Sizes</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <button class="btn btn-primary btn-lg">Large</button>
                  <button class="btn btn-primary">Default</button>
                  <button class="btn btn-primary btn-sm">Small</button>
                  <button class="btn btn-primary btn-xs">Extra Small</button>
                </p>
                <p class="demo">
                  <button class="btn btn-primary btn-block">Block Button</button>
                </p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Button Styles</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <button class="btn btn-primary btn-round">Round</button>
                  <button class="btn btn-info btn-round">Round Info</button>
                  <button class="btn btn-success btn-round">Round Success</button>
                </p>
                <p class="demo">
                  <button class="btn btn-outline-primary">Outline Primary</button>
                  <button class="btn btn-outline-secondary">Outline Secondary</button>
                  <button class="btn btn-outline-info">Outline Info</button>
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Icon Buttons</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <button class="btn btn-icon btn-primary">
                    <i class="fas fa-heart"></i>
                  </button>
                  <button class="btn btn-icon btn-info">
                    <i class="fas fa-star"></i>
                  </button>
                  <button class="btn btn-icon btn-success">
                    <i class="fas fa-check"></i>
                  </button>
                  <button class="btn btn-icon btn-warning">
                    <i class="fas fa-exclamation"></i>
                  </button>
                  <button class="btn btn-icon btn-danger">
                    <i class="fas fa-times"></i>
                  </button>
                </p>
                <p class="demo">
                  <button class="btn btn-icon btn-round btn-primary">
                    <i class="fas fa-heart"></i>
                  </button>
                  <button class="btn btn-icon btn-round btn-info">
                    <i class="fas fa-star"></i>
                  </button>
                  <button class="btn btn-icon btn-round btn-success">
                    <i class="fas fa-check"></i>
                  </button>
                </p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Button Groups</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-primary">Left</button>
                    <button type="button" class="btn btn-primary">Middle</button>
                    <button type="button" class="btn btn-primary">Right</button>
                  </div>
                </p>
                <p class="demo">
                  <div class="btn-group-vertical" role="group">
                    <button type="button" class="btn btn-secondary">Top</button>
                    <button type="button" class="btn btn-secondary">Middle</button>
                    <button type="button" class="btn btn-secondary">Bottom</button>
                  </div>
                </p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Label Buttons</div>
              </div>
              <div class="card-body">
                <p class="demo">
                  <button class="btn btn-label-primary">
                    <span class="btn-label">
                      <i class="fas fa-heart"></i>
                    </span>
                    Primary
                  </button>
                  <button class="btn btn-label-secondary">
                    <span class="btn-label">
                      <i class="fas fa-star"></i>
                    </span>
                    Secondary
                  </button>
                  <button class="btn btn-label-info">
                    <span class="btn-label">
                      <i class="fas fa-info"></i>
                    </span>
                    Info
                  </button>
                  <button class="btn btn-label-success">
                    <span class="btn-label">
                      <i class="fas fa-check"></i>
                    </span>
                    Success
                  </button>
                  <button class="btn btn-label-warning">
                    <span class="btn-label">
                      <i class="fas fa-exclamation"></i>
                    </span>
                    Warning
                  </button>
                  <button class="btn btn-label-danger">
                    <span class="btn-label">
                      <i class="fas fa-times"></i>
                    </span>
                    Danger
                  </button>
                </p>
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
  name: 'ButtonsPage',
  layout: 'kaiadmin',
  head() {
    return {
      title: 'Buttons - KAI Admin'
    }
  }
}
</script>

<style scoped>
.demo {
  margin-bottom: 1rem;
}

.demo .btn {
  margin: 0.25rem;
}
</style>