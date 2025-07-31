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
                <button @click="confirmDelete(course)" class="action-btn btn-delete">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <polyline points="3 6 5 6 21 6"></polyline>
                    <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
                    <line x1="10" y1="11" x2="10" y2="17"></line>
                    <line x1="14" y1="11" x2="14" y2="17"></line>
                  </svg>
                  Delete
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
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

    <!-- Delete Confirmation Modal -->
    <div v-if="showDeleteModal" class="fixed inset-0 z-50 overflow-y-auto">
      <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
        <!-- Background overlay -->
        <div class="fixed inset-0 transition-opacity" aria-hidden="true">
          <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
        </div>

        <!-- Modal content -->
        <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full">
          <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
            <div class="sm:flex sm:items-start">
              <div class="mx-auto flex-shrink-0 flex items-center justify-center h-12 w-12 rounded-full bg-red-100 sm:mx-0 sm:h-10 sm:w-10">
                <svg class="h-6 w-6 text-red-600" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                </svg>
              </div>
              <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left">
                <h3 class="text-lg leading-6 font-medium text-gray-900">
                  Delete Course
                </h3>
                <div class="mt-2">
                  <p class="text-sm text-gray-500">
                    Are you sure you want to delete "{{ selectedCourse?.Name || 'this course' }}"? This action cannot be undone.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
            <button
              type="button"
              @click="deleteCourse"
              class="w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-red-600 text-base font-medium text-white hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 sm:ml-3 sm:w-auto sm:text-sm"
              :disabled="loading"
            >
              <span v-if="!loading">Delete</span>
              <span v-else>Deleting...</span>
            </button>
            <button
              type="button"
              @click="closeModal"
              class="mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm"
              :disabled="loading"
            >
              Cancel
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
      selectedCourse: null,
      showDeleteModal: false,
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
      // Store the selected course and open edit modal
      this.selectedCourse = { ...course }
      // In a real app, you would open an edit modal here
      console.log('Edit course:', course.id)
      // Example: this.$router.push(`/courses/${course.id}/edit`)
    },

    confirmDelete(course) {
      this.selectedCourse = course
      this.showDeleteModal = true
    },

    async deleteCourse() {
      if (!this.selectedCourse) return
      
      try {
        await this.$client.delete(`basetest/courses/${this.selectedCourse.id}/`)
        // Remove the deleted course from the list
        this.courses = this.courses.filter(c => c.id !== this.selectedCourse.id)
        this.showDeleteModal = false
        this.selectedCourse = null
      } catch (error) {
        console.error('Failed to delete course:', error)
        this.error = 'Failed to delete course. Please try again.'
      }
    },

    closeModal() {
      this.showDeleteModal = false
      this.selectedCourse = null
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
        const courseData = {
          data: {
            Name: this.newCourse.Name,
            Description: this.newCourse.Description,
            'Start Date': this.newCourse['Start Date'],
            Active: this.newCourse.Active
          }
        }
        
        const response = await this.$client.post('basetest/courses/', courseData)
        
        // Add the new course to the beginning of the list
        this.courses.unshift(response.data)
        
        // Close the modal and reset the form
        this.closeCreateModal()
        
        // Show success message (you might want to add a toast notification)
        this.$toast.success('Course created successfully')
        
      } catch (error) {
        console.error('Failed to create course:', error)
        this.error = error.response?.data?.detail || 'Failed to create course. Please try again.'
        
        // Handle validation errors from the API
        if (error.response?.data) {
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