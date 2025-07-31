<template>
  <div class="dashboard-page p-6">
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-2xl font-semibold">Courses</h2>
      <button
        @click="refreshCourses"
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition-colors"
        :disabled="loading"
      >
        <span v-if="!loading">Refresh</span>
        <span v-else>Loading...</span>
      </button>
    </div>

    <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
      {{ error }}
    </div>

    <div class="bg-white rounded-lg shadow overflow-hidden">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Description</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Start Date</th>
            </th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-if="loading">
            <td colspan="4" class="px-6 py-4 text-center text-gray-500">
              Loading courses...
            </td>
          </tr>
          <tr v-else-if="courses.length === 0">
            <td colspan="4" class="px-6 py-4 text-center text-gray-500">
              No courses found.
            </td>
          </tr>
          <tr v-for="course in courses" :key="course.id" class="hover:bg-gray-50">
            <td class="px-6 py-4 whitespace-nowrap">
              <div class="text-sm font-medium text-gray-900">{{ course.Name || 'Untitled' }}</div>
            </td>
            <td class="px-6 py-4">
              <div class="text-sm text-gray-500">{{ course.Description || 'No description' }}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
              <span
                :class="{
                  'px-2 inline-flex text-xs leading-5 font-semibold rounded-full': true,
                  'bg-green-100 text-green-800': course.Active === true,
                  'bg-yellow-100 text-yellow-800': course.Active === false,
                  'bg-gray-100 text-gray-800': course.Active === null || course.Active === undefined
                }"
              >
                {{ course.Active === true ? 'Active' : 'Inactive' }}
              </span>
            </td>
            <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
              {{ formatDate(course['Start Date']) }}
            </td>
          </tr>
        </tbody>
      </table>
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
      error: null
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
    }
  }
}
</script>

<style scoped>
.dashboard-page {
    max-width: 1200px;
    margin: 0 auto;
  }
  </style>