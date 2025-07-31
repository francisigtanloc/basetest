<template>
  <div class="dashboard-page">
    <div class="table-header">
      <h1 class="table-title">Courses</h1>
      <div class="table-actions">
        <button
          @click="openCreateModal"
          class="action-btn btn-edit"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="12" y1="5" x2="12" y2="19"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
          </svg>
          New Course
        </button>
        <button
          @click="refreshCourses"
          class="refresh-btn"
          :disabled="loading"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/>
          </svg>
          <span v-if="!loading">Refresh</span>
          <span v-else>Loading...</span>
        </button>
      </div>
    </div>

    <div v-if="error" class="error-message">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="12" cy="12" r="10"></circle>
        <line x1="12" y1="8" x2="12" y2="12"></line>
        <line x1="12" y1="16" x2="12.01" y2="16"></line>
      </svg>
      {{ error }}
    </div>

    <div class="table-container">
      <table class="courses-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Description</th>
            <th>Status</th>
            <th>Start Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="5" class="loading-state">
              <svg class="animate-spin h-5 w-5 text-gray-500" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
            </td>
          </tr>
          <tr v-else-if="courses.length === 0">
            <td colspan="5" class="empty-state">
              No courses found.
            </td>
          </tr>
          <tr v-for="course in courses" :key="course.id">
            <td>
              <div class="font-medium text-gray-900">{{ course.Name || 'Untitled' }}</div>
            </td>
            <td>
              <div class="text-gray-600">{{ course.Description || 'No description' }}</div>
            </td>
            <td>
              <span :class="['status-badge', course.Active ? 'status-active' : 'status-inactive']">
                {{ course.Active ? 'Active' : 'Inactive' }}
              </span>
            </td>
            <td>
              {{ formatDate(course['Start Date']) }}
            </td>
            <td>
              <div class="flex space-x-2">
                <button @click="editCourse(course)" class="action-btn btn-edit">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"></path>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"></path>
                  </svg>
                  Edit
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Edit Course Modal -->
    <div v-if="editingCourse" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <!-- Overlay -->
      <div 
        class="absolute inset-0 bg-black bg-opacity-50"
        @click="cancelEdit"
      ></div>
      
      <!-- Modal Container -->
      <div class="relative w-full max-w-md">
        <!-- Modal Content -->
        <div class="bg-white rounded-lg shadow-xl">
          <!-- Modal Header -->
          <div class="px-6 py-4 border-b border-gray-200">
            <div class="flex items-center justify-between">
              <h3 class="text-lg font-medium text-gray-900">
                Edit Course
              </h3>
              <button
                type="button"
                @click="cancelEdit"
                class="text-gray-400 hover:text-gray-500"
              >
                <span class="sr-only">Close</span>
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
          
          <!-- Modal Body -->
          <div class="p-6">
            <div class="space-y-4">
              <!-- Course Name -->
              <div>
                <label for="editCourseName" class="block text-sm font-medium text-gray-700">
                  Course Name <span class="text-red-500">*</span>
                </label>
                <input
                  type="text"
                  id="editCourseName"
                  v-model="editingCourse.Name"
                  :class="{
                    'border-red-300': editFormErrors.name,
                    'border-gray-300': !editFormErrors.name
                  }"
                  class="mt-1 block w-full rounded-md shadow-sm py-2 px-3 border focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="Enter course name"
                />
                <p v-if="editFormErrors.name" class="mt-1 text-sm text-red-600">
                  {{ editFormErrors.name }}
                </p>
              </div>

              <!-- Description -->
              <div>
                <label for="editCourseDescription" class="block text-sm font-medium text-gray-700">
                  Description
                </label>
                <textarea
                  id="editCourseDescription"
                  v-model="editingCourse.Description"
                  rows="3"
                  class="mt-1 block w-full rounded-md border border-gray-300 shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="Enter course description"
                ></textarea>
              </div>

              <!-- Start Date -->
              <div>
                <label for="editStartDate" class="block text-sm font-medium text-gray-700">
                  Start Date <span class="text-red-500">*</span>
                </label>
                <input
                  type="date"
                  id="editStartDate"
                  v-model="editingCourse['Start Date']"
                  :class="{
                    'border-red-300': editFormErrors.startDate,
                    'border-gray-300': !editFormErrors.startDate
                  }"
                  class="mt-1 block w-full rounded-md border shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                />
                <p v-if="editFormErrors.startDate" class="mt-1 text-sm text-red-600">
                  {{ editFormErrors.startDate }}
                </p>
              </div>

              <!-- Active Status -->
              <div class="flex items-center">
                <input
                  id="editIsActive"
                  type="checkbox"
                  v-model="editingCourse.Active"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
                <label for="editIsActive" class="ml-2 block text-sm text-gray-700">
                  Active
                </label>
              </div>
            </div>
          </div>
          
          <!-- Modal Footer -->
          <div class="bg-gray-50 px-6 py-4 border-t border-gray-200 rounded-b-lg flex justify-end space-x-3">
            <button
              type="button"
              @click="cancelEdit"
              class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              :disabled="isUpdating"
            >
              Cancel
            </button>
            <button
              type="button"
              @click="updateCourse"
              class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
              :disabled="isUpdating"
            >
              <svg v-if="isUpdating" class="w-4 h-4 mr-2 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span v-else class="flex items-center">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                Update Course
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Create Course Modal -->
    <div v-if="showCreateModal" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <!-- Overlay -->
      <div 
        class="absolute inset-0 bg-black bg-opacity-50"
        @click="closeCreateModal"
      ></div>
      
      <!-- Modal Container -->
      <div class="relative w-full max-w-md">
        <!-- Modal Content -->
        <div class="bg-white rounded-lg shadow-xl">
          <!-- Modal Header -->
          <div class="px-6 py-4 border-b border-gray-200">
            <div class="flex items-center justify-between">
              <h3 class="text-lg font-medium text-gray-900">
                Create New Course
              </h3>
              <button
                type="button"
                @click="closeCreateModal"
                class="text-gray-400 hover:text-gray-500"
              >
                <span class="sr-only">Close</span>
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
          
          <!-- Modal Body -->
          <div class="p-6">
            <div class="space-y-4">
              <!-- Course Name -->
              <div>
                <label for="courseName" class="block text-sm font-medium text-gray-700">
                  Course Name <span class="text-red-500">*</span>
                </label>
                <input
                  type="text"
                  id="courseName"
                  v-model="newCourse.Name"
                  :class="{
                    'border-red-300': formErrors.name,
                    'border-gray-300': !formErrors.name
                  }"
                  class="mt-1 block w-full rounded-md shadow-sm py-2 px-3 border focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="Enter course name"
                />
                <p v-if="formErrors.name" class="mt-1 text-sm text-red-600">
                  {{ formErrors.name }}
                </p>
              </div>

              <!-- Description -->
              <div>
                <label for="courseDescription" class="block text-sm font-medium text-gray-700">
                  Description
                </label>
                <textarea
                  id="courseDescription"
                  v-model="newCourse.Description"
                  rows="3"
                  class="mt-1 block w-full rounded-md border border-gray-300 shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                  placeholder="Enter course description"
                ></textarea>
              </div>

              <!-- Start Date -->
              <div>
                <label for="startDate" class="block text-sm font-medium text-gray-700">
                  Start Date <span class="text-red-500">*</span>
                </label>
                <input
                  type="date"
                  id="startDate"
                  v-model="newCourse['Start Date']"
                  :class="{
                    'border-red-300': formErrors.startDate,
                    'border-gray-300': !formErrors.startDate
                  }"
                  class="mt-1 block w-full rounded-md border shadow-sm py-2 px-3 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm"
                />
                <p v-if="formErrors.startDate" class="mt-1 text-sm text-red-600">
                  {{ formErrors.startDate }}
                </p>
              </div>

              <!-- Active Status -->
              <div class="flex items-center">
                <input
                  id="isActive"
                  type="checkbox"
                  v-model="newCourse.Active"
                  class="h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
                />
                <label for="isActive" class="ml-2 block text-sm text-gray-700">
                  Active
                </label>
              </div>
            </div>
          </div>
          
          <!-- Modal Footer -->
          <div class="bg-gray-50 px-6 py-4 border-t border-gray-200 rounded-b-lg flex justify-end space-x-3">
            <button
              type="button"
              @click="closeCreateModal"
              class="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              :disabled="isCreating"
            >
              Cancel
            </button>
            <button
              type="button"
              @click="createCourse"
              class="inline-flex items-center px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50"
              :disabled="isCreating"
            >
              <svg v-if="isCreating" class="w-4 h-4 mr-2 animate-spin" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span v-else class="flex items-center">
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                </svg>
                Create Course
              </span>
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  layout: 'dashboard',
  
  data() {
    return {
      courses: [],
      loading: false,
      error: null,
      // Edit modal state
      editingCourse: null,
      isUpdating: false,
      editFormErrors: {},
      // Create modal state
      showCreateModal: false,
      isCreating: false,
      newCourse: {
        Name: '',
        Description: '',
        'Start Date': '',
        Active: true
      },
      formErrors: {}
    }
  },

  async asyncData({ app }) {
    try {
      const response = await app.$client.get('basetest/courses/')
      return {
        courses: response.data.courses || [],
        loading: false,
        error: null
      }
    } catch (error) {
      console.error('Failed to fetch courses:', error)
      return {
        courses: [],
        loading: false,
        error: 'Failed to load courses. Please try again.'
      }
    }
  },
  
  methods: {
    async fetchCourses() {
      this.loading = true
      this.error = null
      
      try {
        const response = await this.$client.get('basetest/courses/')
        this.courses = response.data.courses || []
      } catch (error) {
        console.error('Failed to fetch courses:', error)
        this.error = 'Failed to load courses. Please try again.'
      } finally {
        this.loading = false
      }
    },
    
    async refreshCourses() {
      await this.fetchCourses()
    },
    
    formatDate(dateString) {
      if (!dateString) return 'N/A'
      const options = { year: 'numeric', month: 'short', day: 'numeric' }
      return new Date(dateString).toLocaleDateString(undefined, options)
    },

    editCourse(course) {
      // Create a deep copy of the course to edit
      this.editingCourse = JSON.parse(JSON.stringify(course))
      this.editFormErrors = {}
    },

    cancelEdit() {
      this.editingCourse = null
      this.editFormErrors = {}
    },

    validateEditForm() {
      this.editFormErrors = {}
      let isValid = true

      if (!this.editingCourse.Name?.trim()) {
        this.editFormErrors.name = 'Course name is required'
        isValid = false
      }

      if (!this.editingCourse['Start Date']) {
        this.editFormErrors.startDate = 'Start date is required'
        isValid = false
      }

      return isValid
    },

    async updateCourse() {
      if (!this.validateEditForm()) {
        return
      }

      this.isUpdating = true
      this.error = null
      
      try {
        // Format the data as a JSON string for the API
        const courseData = JSON.stringify({
          Name: this.editingCourse.Name,
          Description: this.editingCourse.Description,
          'Start Date': this.editingCourse['Start Date'],
          Active: this.editingCourse.Active
        })
        
        const response = await this.$client.put(`basetest/courses/${this.editingCourse.id}/`, courseData)
        console.log('API Response (update):', response);
        
        // Safely extract the course data from the response
        try {
          // Try to find the course data in the response
          let updatedCourse;
          
          if (response && response.data) {
            // Check for course directly in response
            if (response.data.course) {
              updatedCourse = response.data.course;
            }
            // Check for nested data structure
            else if (response.data.data && response.data.data.course) {
              updatedCourse = response.data.data.course;
            }
            
            // If we found a course, update it in the list
            if (updatedCourse) {
              const index = this.courses.findIndex(c => c.id === this.editingCourse.id)
              if (index !== -1) {
                this.courses.splice(index, 1, updatedCourse)
              }
            } else {
              console.warn('Could not find course data in response');
            }
          }
        } catch (parseError) {
          console.error('Error processing response:', parseError);
        }
        
        // Reset error state since operation was successful
        this.error = null
        
        // Close the modal
        this.editingCourse = null
        
        // Show success message
        // this.$toast.success('Course updated successfully!')
      } catch (error) {
        console.error('Error updating course:', error)
        // Handle error response
        if (error.response?.data?.data?.message) {
          this.error = error.response.data.data.message
        } else if (error.response?.data?.message) {
          this.error = error.response.data.message
        } else if (error.response?.data?.detail) {
          this.error = error.response.data.detail
        } else {
          this.error = 'Failed to update course'
        }
        
        // Handle validation errors
        if (error.response?.data?.data?.errors) {
          this.editFormErrors = error.response.data.data.errors
        } else if (error.response?.data?.errors) {
          this.editFormErrors = error.response.data.errors
        } else if (error.response?.status === 400) {
          this.editFormErrors = error.response.data
        }
      } finally {
        this.isUpdating = false
      }
    },

    
    openCreateModal() {
      this.showCreateModal = true
    },
    
    closeCreateModal() {
      this.showCreateModal = false
      this.resetNewCourse()
      this.formErrors = {}
    },
    
    resetNewCourse() {
      this.newCourse = {
        Name: '',
        Description: '',
        'Start Date': '',
        Active: true
      }
    },
    
    validateForm() {
      this.formErrors = {}
      let isValid = true
      
      if (!this.newCourse.Name || this.newCourse.Name.trim() === '') {
        this.formErrors.name = 'Course name is required'
        isValid = false
      }
      
      if (!this.newCourse['Start Date']) {
        this.formErrors.startDate = 'Start date is required'
        isValid = false
      }
      
      return isValid
    },
    
    async createCourse() {
      if (!this.validateForm()) {
        return
      }
      
      this.isCreating = true
      this.error = null
      
      try {
        // Format the data to match the API expected format
        // Format the data for the API
        const courseData = {
          Name: this.newCourse.Name,
          Description: this.newCourse.Description,
          'Start Date': this.newCourse['Start Date'],
          Active: this.newCourse.Active
        }
        
        const response = await this.$client.post('basetest/courses/', courseData)
        console.log('API Response:', response);
        
        // Safely extract the course data from the response
        try {
          // Try to find the course data in the response
          let newCourse;
          
          if (response && response.data) {
            // Check for course directly in response
            if (response.data.course) {
              newCourse = response.data.course;
            }
            // Check for nested data structure
            else if (response.data.data && response.data.data.course) {
              newCourse = response.data.data.course;
            }
            // If we found a course, add it to the list
            if (newCourse) {
              this.courses.unshift(newCourse);
            } else {
              console.warn('Could not find course data in response');
            }
          }
        } catch (parseError) {
          console.error('Error processing response:', parseError);
        }
        
        // Reset error state since operation was successful
        this.error = null
        
        // Close the modal and reset the form
        this.closeCreateModal()
        
        // Show success message
        // this.$toast.success('Course created successfully!')
        
      } catch (error) {
        console.error('Failed to create course:', error)
        // Handle error response
        if (error.response?.data?.data?.message) {
          this.error = error.response.data.data.message
        } else if (error.response?.data?.message) {
          this.error = error.response.data.message
        } else if (error.response?.data?.detail) {
          this.error = error.response.data.detail
        } else {
          this.error = 'Failed to create course'
        }
        
        // Handle validation errors
        if (error.response?.data?.data?.errors) {
          this.formErrors = { ...this.formErrors, ...error.response.data.data.errors }
        } else if (error.response?.data?.errors) {
          this.formErrors = { ...this.formErrors, ...error.response.data.errors }
        } else if (error.response?.data) {
          this.formErrors = { ...this.formErrors, ...error.response.data }
        }
      } finally {
        this.isCreating = false
      }
    }
  }
}
</script>
q
<style scoped>
.dashboard-page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1.5rem;
}

.courses-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  background: white;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.courses-table thead th {
  background-color: #f9fafb;
  color: #6b7280;
  font-weight: 500;
  text-transform: uppercase;
  font-size: 0.75rem;
  letter-spacing: 0.05em;
  text-align: left;
  padding: 0.75rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
}

.courses-table tbody tr {
  transition: background-color 0.15s ease;
}

.courses-table tbody tr:hover {
  background-color: #f9fafb;
}

.courses-table tbody td {
  padding: 1rem 1.5rem;
  border-bottom: 1px solid #e5e7eb;
  font-size: 0.875rem;
  color: #374151;
}

.courses-table tbody tr:last-child td {
  border-bottom: none;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-size: 0.75rem;
  font-weight: 500;
  line-height: 1.25rem;
}

.status-active {
  background-color: #ecfdf5;
  color: #065f46;
}

.status-inactive {
  background-color: #fef2f2;
  color: #991b1b;
}

.action-btn {
  padding: 0.375rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
}

.action-btn:hover {
  transform: translateY(-1px);
}

.btn-edit {
  background-color: #e0f2fe;
  color: #0369a1;
}

.btn-edit:hover {
  background-color: #bae6fd;
}

.btn-delete {
  background-color: #fee2e2;
  color: #b91c1c;
}

.btn-delete:hover {
  background-color: #fecaca;
}

.loading-state {
  display: flex;
  justify-content: center;
  padding: 2rem;
}

.empty-state {
  text-align: center;
  padding: 3rem 1rem;
  color: #6b7280;
}

.error-message {
  background-color: #fef2f2;
  color: #b91c1c;
  padding: 0.75rem 1rem;
  border-radius: 0.375rem;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.table-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.table-title {
  font-size: 1.5rem;
  font-weight: 600;
  color: #111827;
}

.table-actions {
  display: flex;
  gap: 0.75rem;
}

.refresh-btn {
  padding: 0.5rem 1rem;
  background-color: #f3f4f6;
  border-radius: 0.375rem;
  font-weight: 500;
  color: #374151;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: background-color 0.15s ease;
}

.refresh-btn:hover {
  background-color: #e5e7eb;
}

.refresh-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}
</style>