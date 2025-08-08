<template>
  <div>
    <div class="container">
      <div class="page-inner">
        <div class="page-header">
          <h3 class="fw-bold mb-3">Forms</h3>
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
              <nuxt-link to="#">Forms</nuxt-link>
            </li>
            <li class="separator">
              <i class="icon-arrow-right"></i>
            </li>
            <li class="nav-item">
              <a href="#">Basic Form</a>
            </li>
          </ul>
        </div>
        
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Basic Form</div>
              </div>
              <div class="card-body">
                <form @submit.prevent="submitBasicForm">
                  <div class="form-group">
                    <label for="email2">Email Address</label>
                    <input type="email" class="form-control" id="email2" placeholder="Enter Email" v-model="basicForm.email">
                    <small class="form-text text-muted">We'll never share your email with anyone else.</small>
                  </div>
                  <div class="form-group">
                    <label for="password">Password</label>
                    <input type="password" class="form-control" id="password" placeholder="Password" v-model="basicForm.password">
                  </div>
                  <div class="form-group">
                    <label for="exampleFormControlSelect1">Example select</label>
                    <select class="form-control" id="exampleFormControlSelect1" v-model="basicForm.selectOption">
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                      <option>5</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="exampleFormControlTextarea1">Example textarea</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="3" v-model="basicForm.textarea"></textarea>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault" v-model="basicForm.agreeTerms">
                    <label class="form-check-label" for="flexCheckDefault">
                      Agree with terms and conditions
                    </label>
                  </div>
                  <div class="card-action">
                    <button type="submit" class="btn btn-success">Submit</button>
                    <button type="button" class="btn btn-danger" @click="cancelForm">Cancel</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Form with Icons</div>
              </div>
              <div class="card-body">
                <form @submit.prevent="submitIconForm">
                  <div class="form-group">
                    <label for="username">Username</label>
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                          <i class="fas fa-user"></i>
                        </span>
                      </div>
                      <input type="text" class="form-control" id="username" placeholder="Username" v-model="iconForm.username">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="emailIcon">Email</label>
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                          <i class="fas fa-envelope"></i>
                        </span>
                      </div>
                      <input type="email" class="form-control" id="emailIcon" placeholder="Email" v-model="iconForm.email">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="passwordIcon">Password</label>
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                          <i class="fas fa-lock"></i>
                        </span>
                      </div>
                      <input type="password" class="form-control" id="passwordIcon" placeholder="Password" v-model="iconForm.password">
                    </div>
                  </div>
                  <div class="form-group">
                    <label for="phone">Phone Number</label>
                    <div class="input-group">
                      <div class="input-group-prepend">
                        <span class="input-group-text">
                          <i class="fas fa-phone"></i>
                        </span>
                      </div>
                      <input type="tel" class="form-control" id="phone" placeholder="Phone Number" v-model="iconForm.phone">
                    </div>
                  </div>
                  <div class="card-action">
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="button" class="btn btn-secondary" @click="resetIconForm">Reset</button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Form Controls</div>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <label for="largeInput">Large Input</label>
                  <input type="text" class="form-control form-control-lg" id="largeInput" placeholder="Large Input">
                </div>
                <div class="form-group">
                  <label for="defaultInput">Default Input</label>
                  <input type="text" class="form-control" id="defaultInput" placeholder="Default Input">
                </div>
                <div class="form-group">
                  <label for="smallInput">Small Input</label>
                  <input type="text" class="form-control form-control-sm" id="smallInput" placeholder="Small Input">
                </div>
                <div class="form-group">
                  <label for="squareInput">Square Input</label>
                  <input type="text" class="form-control input-square" id="squareInput" placeholder="Square Input">
                </div>
                <div class="form-group">
                  <label for="pillInput">Pill Input</label>
                  <input type="text" class="form-control input-pill" id="pillInput" placeholder="Pill Input">
                </div>
                <div class="form-group">
                  <label for="solidInput">Solid Input</label>
                  <input type="text" class="form-control input-solid" id="solidInput" placeholder="Solid Input">
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Form Check</div>
              </div>
              <div class="card-body">
                <div class="form-group">
                  <label class="form-label">Radios</label>
                  <div class="selectgroup w-100">
                    <label class="selectgroup-item">
                      <input type="radio" name="radio-example" value="option1" class="selectgroup-input" v-model="formControls.radioValue">
                      <span class="selectgroup-button">Option 1</span>
                    </label>
                    <label class="selectgroup-item">
                      <input type="radio" name="radio-example" value="option2" class="selectgroup-input" v-model="formControls.radioValue">
                      <span class="selectgroup-button">Option 2</span>
                    </label>
                    <label class="selectgroup-item">
                      <input type="radio" name="radio-example" value="option3" class="selectgroup-input" v-model="formControls.radioValue">
                      <span class="selectgroup-button">Option 3</span>
                    </label>
                  </div>
                </div>
                
                <div class="form-group">
                  <label class="form-label">Checkboxes</label>
                  <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkbox1" v-model="formControls.checkbox1">
                    <label class="form-check-label" for="checkbox1">
                      Option one is this
                    </label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkbox2" v-model="formControls.checkbox2">
                    <label class="form-check-label" for="checkbox2">
                      Option two can be something else
                    </label>
                  </div>
                  <div class="form-check">
                    <input class="form-check-input" type="checkbox" id="checkbox3" v-model="formControls.checkbox3" disabled>
                    <label class="form-check-label" for="checkbox3">
                      Option three is disabled
                    </label>
                  </div>
                </div>
                
                <div class="form-group">
                  <label class="form-label">Toggle Switch</label>
                  <div class="form-check form-switch">
                    <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" v-model="formControls.toggleSwitch">
                    <label class="form-check-label" for="flexSwitchCheckDefault">Default switch checkbox input</label>
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
  name: 'BasicFormsPage',
  layout: 'kaiadmin',
  data() {
    return {
      basicForm: {
        email: '',
        password: '',
        selectOption: '1',
        textarea: '',
        agreeTerms: false
      },
      iconForm: {
        username: '',
        email: '',
        password: '',
        phone: ''
      },
      formControls: {
        radioValue: 'option1',
        checkbox1: false,
        checkbox2: false,
        checkbox3: false,
        toggleSwitch: false
      }
    }
  },
  head() {
    return {
      title: 'Basic Forms - KAI Admin'
    }
  },
  mounted() {
    // Ensure components are available for forms
    if (process.client) {
      setTimeout(() => {
        if (window.$ && window.jQuery) {
          console.log('Form components initialized')
        }
      }, 1000)
    }
  },
  methods: {
    submitBasicForm() {
      if (!this.basicForm.agreeTerms) {
        this.$swal({
          title: 'Warning!',
          text: 'Please agree to the terms and conditions.',
          type: 'warning',
          confirmButtonText: 'OK'
        })
        return
      }
      
      this.$swal({
        title: 'Success!',
        text: 'Basic form submitted successfully!',
        type: 'success',
        confirmButtonText: 'OK'
      })
    },
    
    submitIconForm() {
      if (!this.iconForm.username || !this.iconForm.email || !this.iconForm.password) {
        this.$swal({
          title: 'Error!',
          text: 'Please fill in all required fields.',
          type: 'error',
          confirmButtonText: 'OK'
        })
        return
      }
      
      this.$swal({
        title: 'Success!',
        text: 'Icon form submitted successfully!',
        type: 'success',
        confirmButtonText: 'OK'
      })
    },
    
    cancelForm() {
      this.basicForm = {
        email: '',
        password: '',
        selectOption: '1',
        textarea: '',
        agreeTerms: false
      }
      
      this.$swal({
        title: 'Cancelled!',
        text: 'Form has been cancelled.',
        type: 'info',
        confirmButtonText: 'OK'
      })
    },
    
    resetIconForm() {
      this.iconForm = {
        username: '',
        email: '',
        password: '',
        phone: ''
      }
    }
  }
}
</script>