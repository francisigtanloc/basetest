<template>
  <div class="login-page">
    <!-- Background Pattern -->
    <div class="login-background">
      <div class="pattern-overlay"></div>
    </div>
    
    <!-- Login Container -->
    <div class="login-container">
      <div class="login-card">
        <!-- Logo Section -->
        <div class="login-header">
          <div class="logo-container">
            <img src="@basetest/assets/img/kaiadmin/logo_light.svg" alt="KAI Admin" class="logo">
            <h1 class="brand-text">KAI Admin</h1>
          </div>
          <p class="login-subtitle">Sign in to your account</p>
        </div>

        <!-- Login Form -->
        <form @submit.prevent="handleLogin" class="login-form">
          <!-- Email Field -->
          <div class="form-group">
            <label for="email" class="form-label">
              <i class="fas fa-envelope"></i>
              Email Address
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              class="form-control"
              :class="{ 'is-invalid': errors.email }"
              placeholder="Enter your email"
              required
              :disabled="loading"
            />
            <div v-if="errors.email" class="invalid-feedback">
              {{ errors.email }}
            </div>
          </div>

          <!-- Password Field -->
          <div class="form-group">
            <label for="password" class="form-label">
              <i class="fas fa-lock"></i>
              Password
            </label>
            <div class="password-input">
              <input
                id="password"
                v-model="form.password"
                :type="showPassword ? 'text' : 'password'"
                class="form-control"
                :class="{ 'is-invalid': errors.password }"
                placeholder="Enter your password"
                required
                :disabled="loading"
              />
              <button
                type="button"
                class="password-toggle"
                @click="showPassword = !showPassword"
                :disabled="loading"
              >
                <i :class="showPassword ? 'fas fa-eye-slash' : 'fas fa-eye'"></i>
              </button>
            </div>
            <div v-if="errors.password" class="invalid-feedback">
              {{ errors.password }}
            </div>
          </div>

          <!-- Remember Me -->
          <div class="form-group form-check-container">
            <div class="form-check">
              <input
                id="rememberMe"
                v-model="form.rememberMe"
                type="checkbox"
                class="form-check-input"
                :disabled="loading"
              />
              <label for="rememberMe" class="form-check-label">
                Remember me
              </label>
            </div>
            <a href="#" class="forgot-password" @click.prevent="forgotPassword">
              Forgot Password?
            </a>
          </div>

          <!-- Error Message -->
          <div v-if="errors.general" class="alert alert-danger">
            <i class="fas fa-exclamation-triangle"></i>
            {{ errors.general }}
          </div>

          <!-- Success Message -->
          <div v-if="success" class="alert alert-success">
            <i class="fas fa-check-circle"></i>
            Login successful! Redirecting...
          </div>

          <!-- Login Button -->
          <button
            type="submit"
            class="btn btn-login btn-block"
            :disabled="loading"
          >
            <span v-if="loading" class="login-loading">
              <i class="fas fa-spinner fa-spin"></i>
              Signing in...
            </span>
            <span v-else>
              <i class="fas fa-sign-in-alt"></i>
              Sign In
            </span>
          </button>
        </form>

        <!-- Footer Links -->
        <div class="login-footer">
          <p class="login-footer-text">
            Don't have an account? 
            <a href="#" @click.prevent="signUp" class="signup-link">Sign up</a>
          </p>
          <div class="login-footer-links">
            <a href="#" @click.prevent="showHelp">Help</a>
            <span>•</span>
            <a href="#" @click.prevent="showPrivacy">Privacy</a>
            <span>•</span>
            <a href="#" @click.prevent="showTerms">Terms</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'KaiAdminLogin',
  layout: false, // No layout for login page
  data() {
    return {
      form: {
        email: '',
        password: '',
        rememberMe: false
      },
      errors: {},
      loading: false,
      success: false,
      showPassword: false
    }
  },
  head() {
    return {
      title: 'Login - KAI Admin',
      meta: [
        { name: 'viewport', content: 'width=device-width, initial-scale=1.0' },
        { name: 'description', content: 'Login to KAI Admin Dashboard' }
      ],
      link: [
        { rel: 'icon', href: '@basetest/assets/img/kaiadmin/favicon.ico', type: 'image/x-icon' }
      ]
    }
  },
  mounted() {
    // Check if already logged in
    if (this.isLoggedIn()) {
      this.$router.push('/student/dashboard')
    }
    
    // Load CSS dynamically
    if (process.client) {
      this.loadLoginAssets()
    }
    
    // Pre-fill test credentials for development
    if (process.env.NODE_ENV === 'development') {
      this.form.email = 'test@email.com'
      this.form.password = '12345678'
    }
  },
  methods: {
    async loadLoginAssets() {
      try {
        // Load Bootstrap and KAI Admin CSS
        await import('@basetest/assets/styles/bootstrap.min.css')
        await import('@basetest/assets/styles/fonts.min.css') 
        await import('@basetest/assets/styles/kaiadmin.min.css')
        console.log('Login CSS loaded successfully')
      } catch (error) {
        console.error('Failed to load login CSS:', error)
      }
    },
    
    async handleLogin() {
      // Reset errors
      this.errors = {}
      this.loading = true
      
      try {
        // Validate form
        if (!this.validateForm()) {
          this.loading = false
          return
        }
        
        // Make API request to token-auth endpoint
        const response = await this.$client.post('basetest/token-auth/', {
          email: this.form.email,
          password: this.form.password
        })
        
        console.log('Login response:', response.data)
        
        if (response.data && response.data.access && response.data.refresh) {
          // Standard JWT token response
          this.storeTokens(response.data)
          
          // Show success message
          this.success = true
          
          // Redirect after short delay
          setTimeout(() => {
            this.$router.push('/student/dashboard')
          }, 1500)
          
        } else if (response.data && response.data.success && response.data.user) {
          // Alternative success format (like debug-auth endpoint)
          // Create token-like structure for compatibility
          const tokenData = {
            access: 'mock_token', // In a real scenario, you'd need proper tokens
            user: response.data.user
          }
          this.storeTokens(tokenData)
          
          // Show success message
          this.success = true
          
          // Redirect after short delay
          setTimeout(() => {
            this.$router.push('/student/dashboard')
          }, 1500)
          
        } else {
          this.errors.general = 'Invalid response from server'
        }
        
      } catch (error) {
        console.error('Login error:', error)
        
        if (error.response) {
          // Server responded with error
          const status = error.response.status
          const data = error.response.data
          
          if (status === 401) {
            this.errors.general = 'Invalid email or password'
          } else if (data && data.detail) {
            this.errors.general = data.detail
          } else if (data && data.error) {
            this.errors.general = data.error
          } else if (data && data.message) {
            this.errors.general = data.message
          } else if (data && !data.success) {
            this.errors.general = data.message || 'Authentication failed'
          } else {
            this.errors.general = 'Login failed. Please try again.'
          }
        } else if (error.request) {
          // Network error
          this.errors.general = 'Network error. Please check your connection.'
        } else {
          // Other error
          this.errors.general = 'An unexpected error occurred.'
        }
        
      } finally {
        this.loading = false
      }
    },
    
    validateForm() {
      const errors = {}
      
      if (!this.form.email) {
        errors.email = 'Email is required'
      } else if (!this.isValidEmail(this.form.email)) {
        errors.email = 'Please enter a valid email'
      }
      
      if (!this.form.password) {
        errors.password = 'Password is required'
      } else if (this.form.password.length < 6) {
        errors.password = 'Password must be at least 6 characters'
      }
      
      this.errors = errors
      return Object.keys(errors).length === 0
    },
    
    isValidEmail(email) {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return emailRegex.test(email)
    },
    
    storeTokens(tokenData) {
      if (process.client) {
        // Store tokens in localStorage
        localStorage.setItem('kai_access_token', tokenData.access)
        if (tokenData.refresh) {
          localStorage.setItem('kai_refresh_token', tokenData.refresh)
        }
        
        // Store user info if available
        if (tokenData.user) {
          localStorage.setItem('kai_user', JSON.stringify(tokenData.user))
        }
        
        // Set remember me preference
        if (this.form.rememberMe) {
          localStorage.setItem('kai_remember_me', 'true')
        }
        
        console.log('Tokens stored successfully')
      }
    },
    
    isLoggedIn() {
      if (process.client) {
        const token = localStorage.getItem('kai_access_token')
        return !!token
      }
      return false
    },
    
    forgotPassword() {
      // TODO: Implement forgot password
      alert('Forgot password functionality will be implemented soon.')
    },
    
    signUp() {
      // TODO: Implement sign up
      alert('Sign up functionality will be implemented soon.')
    },
    
    showHelp() {
      alert('Help documentation will be available soon.')
    },
    
    showPrivacy() {
      alert('Privacy policy will be available soon.')
    },
    
    showTerms() {
      alert('Terms of service will be available soon.')
    }
  }
}
</script>

<style scoped>
/* Login Page Styles */
.login-page {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  font-family: 'Public Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.login-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(255,255,255,0.1) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(255,255,255,0.1) 0%, transparent 50%);
  background-size: 400px 400px;
  animation: float 20s ease-in-out infinite;
}

.pattern-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Ccircle cx='30' cy='30' r='2'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(5deg); }
}

.login-container {
  width: 100%;
  max-width: 420px;
  padding: 20px;
  z-index: 10;
}

.login-card {
  background: rgba(255, 255, 255, 0.98);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 
    0 20px 40px rgba(0,0,0,0.1),
    0 10px 20px rgba(0,0,0,0.05);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,0.2);
  animation: slideUp 0.6s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.login-header {
  text-align: center;
  margin-bottom: 40px;
}

.logo-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin-bottom: 16px;
}

.logo {
  height: 32px;
  width: auto;
}

.brand-text {
  font-size: 28px;
  font-weight: 700;
  color: #1f2937;
  margin: 0;
}

.login-subtitle {
  color: #6b7280;
  font-size: 16px;
  margin: 0;
  font-weight: 400;
}

.login-form {
  margin-bottom: 30px;
}

.form-group {
  margin-bottom: 24px;
}

.form-label {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: #374151;
  margin-bottom: 8px;
  font-size: 14px;
}

.form-label i {
  color: #6b7280;
  width: 16px;
}

.form-control {
  width: 100%;
  padding: 12px 16px;
  border: 2px solid #e5e7eb;
  border-radius: 12px;
  font-size: 16px;
  transition: all 0.3s ease;
  background-color: #f9fafb;
}

.form-control:focus {
  outline: none;
  border-color: #667eea;
  background-color: #ffffff;
  box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

.form-control.is-invalid {
  border-color: #ef4444;
  background-color: #fef2f2;
}

.form-control:disabled {
  background-color: #f3f4f6;
  cursor: not-allowed;
}

.password-input {
  position: relative;
}

.password-toggle {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  color: #6b7280;
  cursor: pointer;
  padding: 4px;
  transition: color 0.3s ease;
}

.password-toggle:hover {
  color: #374151;
}

.form-check-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.form-check {
  display: flex;
  align-items: center;
  gap: 8px;
}

.form-check-input {
  width: 18px;
  height: 18px;
  border-radius: 4px;
}

.form-check-label {
  color: #374151;
  font-size: 14px;
  cursor: pointer;
  margin: 0;
}

.forgot-password {
  color: #667eea;
  text-decoration: none;
  font-size: 14px;
  font-weight: 500;
  transition: color 0.3s ease;
}

.forgot-password:hover {
  color: #4338ca;
  text-decoration: underline;
}

.invalid-feedback {
  color: #ef4444;
  font-size: 14px;
  margin-top: 6px;
  display: flex;
  align-items: center;
  gap: 4px;
}

.alert {
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 14px;
  font-weight: 500;
}

.alert-danger {
  background-color: #fef2f2;
  color: #dc2626;
  border: 1px solid #fecaca;
}

.alert-success {
  background-color: #f0fdf4;
  color: #166534;
  border: 1px solid #bbf7d0;
}

.btn-login {
  width: 100%;
  padding: 14px 24px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 12px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.btn-login:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
}

.btn-login:active {
  transform: translateY(0);
}

.btn-login:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  transform: none;
}

.login-loading {
  display: flex;
  align-items: center;
  gap: 8px;
}

.login-footer {
  text-align: center;
  border-top: 1px solid #e5e7eb;
  padding-top: 24px;
}

.login-footer-text {
  color: #6b7280;
  font-size: 14px;
  margin-bottom: 16px;
}

.signup-link {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s ease;
}

.signup-link:hover {
  color: #4338ca;
  text-decoration: underline;
}

.login-footer-links {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12px;
  font-size: 12px;
}

.login-footer-links a {
  color: #9ca3af;
  text-decoration: none;
  transition: color 0.3s ease;
}

.login-footer-links a:hover {
  color: #667eea;
}

.login-footer-links span {
  color: #d1d5db;
}

/* Responsive Design */
@media (max-width: 480px) {
  .login-container {
    padding: 16px;
  }
  
  .login-card {
    padding: 24px;
    border-radius: 16px;
  }
  
  .brand-text {
    font-size: 24px;
  }
  
  .form-control {
    padding: 10px 14px;
    font-size: 16px; /* Prevent zoom on iOS */
  }
  
  .btn-login {
    padding: 12px 20px;
  }
}
</style>