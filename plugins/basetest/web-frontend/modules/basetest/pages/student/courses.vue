<template>
  <div>
    <!-- Page Header -->
    <div class="d-flex align-items-left align-items-md-center flex-column flex-md-row pt-2 pb-4">
      <div>
        <h3 class="fw-bold mb-3">My Courses</h3>
        <h6 class="op-7 mb-2">Track your learning progress and continue your education journey</h6>
      </div>
      <div class="ms-md-auto py-2 py-md-0">
        <nuxt-link to="/student/dashboard" class="btn btn-label-info btn-round me-2">
          <span class="btn-label">
            <i class="fa fa-home"></i>
          </span>
          Dashboard
        </nuxt-link>
        <a href="#" class="btn btn-primary btn-round">Browse Catalog</a>
      </div>
    </div>

    <!-- Course Stats Cards -->
    <div class="row mb-4">
      <div class="col-sm-6 col-lg-3">
        <div class="card card-stats card-round">
          <div class="card-body">
            <div class="row align-items-center">
              <div class="col-icon">
                <div class="icon-big text-center icon-primary bubble-shadow-small">
                  <i class="fas fa-play-circle"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">In Progress</p>
                  <h4 class="card-title">{{ inProgressCount }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-lg-3">
        <div class="card card-stats card-round">
          <div class="card-body">
            <div class="row align-items-center">
              <div class="col-icon">
                <div class="icon-big text-center icon-success bubble-shadow-small">
                  <i class="fas fa-check-circle"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Completed</p>
                  <h4 class="card-title">{{ completedCount }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-lg-3">
        <div class="card card-stats card-round">
          <div class="card-body">
            <div class="row align-items-center">
              <div class="col-icon">
                <div class="icon-big text-center icon-warning bubble-shadow-small">
                  <i class="fas fa-clock"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Total Hours</p>
                  <h4 class="card-title">{{ totalHours }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-sm-6 col-lg-3">
        <div class="card card-stats card-round">
          <div class="card-body">
            <div class="row align-items-center">
              <div class="col-icon">
                <div class="icon-big text-center icon-info bubble-shadow-small">
                  <i class="fas fa-certificate"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Certificates</p>
                  <h4 class="card-title">{{ certificatesCount }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Filter and Search -->
    <div class="row mb-4">
      <div class="col-md-8">
        <div class="card card-round">
          <div class="card-body p-3">
            <div class="d-flex align-items-center justify-content-between flex-wrap">
              <div class="d-flex align-items-center gap-3 mb-2 mb-md-0">
                <label class="form-label mb-0 me-2">Filter:</label>
                <select v-model="selectedFilter" class="form-select form-select-sm" style="width: auto;">
                  <option value="all">All Courses</option>
                  <option value="in-progress">In Progress</option>
                  <option value="completed">Completed</option>
                  <option value="not-started">Not Started</option>
                </select>
                <select v-model="selectedCategory" class="form-select form-select-sm" style="width: auto;">
                  <option value="all">All Categories</option>
                  <option value="programming">Programming</option>
                  <option value="design">Design</option>
                  <option value="business">Business</option>
                  <option value="data">Data Science</option>
                </select>
              </div>
              <div class="search-box">
                <div class="input-group input-group-sm">
                  <input 
                    v-model="searchQuery" 
                    type="text" 
                    class="form-control" 
                    placeholder="Search courses..."
                    style="min-width: 200px;"
                  >
                  <span class="input-group-text">
                    <i class="fas fa-search"></i>
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card card-round">
          <div class="card-body p-3">
            <div class="d-flex align-items-center justify-content-between">
              <div class="text-muted">
                <i class="fas fa-book-open me-2"></i>
                {{ filteredCourses.length }} course(s) found
              </div>
              <div class="view-toggle">
                <div class="btn-group btn-group-sm" role="group">
                  <button 
                    type="button" 
                    class="btn btn-outline-secondary"
                    :class="{ active: viewMode === 'grid' }"
                    @click="viewMode = 'grid'"
                  >
                    <i class="fas fa-th-large"></i>
                  </button>
                  <button 
                    type="button" 
                    class="btn btn-outline-secondary"
                    :class="{ active: viewMode === 'list' }"
                    @click="viewMode = 'list'"
                  >
                    <i class="fas fa-list"></i>
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Course Cards -->
    <div class="row">
      <!-- Grid View -->
      <div v-if="viewMode === 'grid'" class="col-12">
        <div class="row">
          <div 
            v-for="course in filteredCourses" 
            :key="course.id" 
            class="col-lg-4 col-md-6 mb-4"
          >
            <div class="card course-card h-100">
              <!-- Course Image -->
              <div class="course-image">
                <div v-if="course.image" class="course-image-wrapper">
                  <img :src="course.image" :alt="course.title" class="card-img-top">
                </div>
                <div v-else class="course-image-placeholder">
                  <i class="fas fa-book-open fa-3x"></i>
                </div>
                <div class="course-badge">
                  <span class="badge" :class="getStatusBadgeClass(course.status)">
                    {{ course.status }}
                  </span>
                </div>
                <div class="course-actions">
                  <button class="btn btn-sm btn-light course-action-btn" title="Add to Favorites">
                    <i class="fas fa-heart"></i>
                  </button>
                  <button class="btn btn-sm btn-light course-action-btn" title="Share">
                    <i class="fas fa-share-alt"></i>
                  </button>
                </div>
              </div>

              <!-- Course Content -->
              <div class="card-body d-flex flex-column">
                <div class="course-meta mb-2">
                  <span class="course-category">{{ course.category }}</span>
                  <div class="course-rating">
                    <div class="stars">
                      <i v-for="n in 5" :key="n" class="fas fa-star" :class="n <= course.rating ? 'text-warning' : 'text-muted'"></i>
                    </div>
                    <small class="text-muted ms-1">({{ course.reviews }})</small>
                  </div>
                </div>

                <h5 class="card-title mb-2">{{ course.title }}</h5>
                <p class="card-text text-muted mb-2">{{ course.description }}</p>
                
                <div class="instructor-info mb-3">
                  <div class="d-flex align-items-center">
                    <div v-if="course.instructorAvatar" class="instructor-avatar me-2">
                      <img :src="course.instructorAvatar" :alt="course.instructor">
                    </div>
                    <div v-else class="instructor-avatar instructor-initials me-2">
                      {{ getInstructorInitials(course.instructor) }}
                    </div>
                    <div>
                      <small class="d-block fw-semibold">{{ course.instructor }}</small>
                      <small class="text-muted">{{ course.instructorTitle }}</small>
                    </div>
                  </div>
                </div>

                <div class="course-progress mb-3">
                  <div class="d-flex justify-content-between mb-1">
                    <small class="text-muted">Progress</small>
                    <small class="fw-semibold">{{ course.progress }}%</small>
                  </div>
                  <div class="progress progress-sm">
                    <div 
                      class="progress-bar" 
                      :class="getProgressBarClass(course.progress)"
                      role="progressbar" 
                      :style="`width: ${course.progress}%`"
                    ></div>
                  </div>
                </div>

                <div class="course-stats mb-3">
                  <div class="row text-center">
                    <div class="col-4">
                      <small class="d-block text-muted">Duration</small>
                      <small class="fw-semibold">{{ course.duration }}</small>
                    </div>
                    <div class="col-4">
                      <small class="d-block text-muted">Lessons</small>
                      <small class="fw-semibold">{{ course.lessons }}</small>
                    </div>
                    <div class="col-4">
                      <small class="d-block text-muted">Level</small>
                      <small class="fw-semibold">{{ course.level }}</small>
                    </div>
                  </div>
                </div>

                <!-- Action Buttons -->
                <div class="mt-auto">
                  <div class="d-flex gap-2">
                    <button 
                      class="btn btn-primary flex-fill"
                      @click="continueCourse(course)"
                    >
                      <i :class="course.progress > 0 ? 'fas fa-play' : 'fas fa-play-circle'"></i>
                      {{ course.progress > 0 ? 'Continue' : 'Start Course' }}
                    </button>
                    <button 
                      class="btn btn-outline-secondary"
                      @click="viewCourse(course)"
                      title="View Details"
                    >
                      <i class="fas fa-info-circle"></i>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- List View -->
      <div v-else class="col-12">
        <div class="card card-round">
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover course-list-table">
                <thead>
                  <tr>
                    <th>Course</th>
                    <th>Category</th>
                    <th>Progress</th>
                    <th>Status</th>
                    <th>Rating</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="course in filteredCourses" :key="course.id" class="course-list-row">
                    <td>
                      <div class="d-flex align-items-center">
                        <div v-if="course.image" class="course-list-image me-3">
                          <img :src="course.image" :alt="course.title">
                        </div>
                        <div v-else class="course-list-image course-list-placeholder me-3">
                          <i class="fas fa-book"></i>
                        </div>
                        <div>
                          <h6 class="mb-1">{{ course.title }}</h6>
                          <small class="text-muted">{{ course.instructor }}</small>
                          <div class="text-muted small">{{ course.duration }} • {{ course.lessons }} lessons</div>
                        </div>
                      </div>
                    </td>
                    <td>
                      <span class="badge bg-light text-dark">{{ course.category }}</span>
                    </td>
                    <td>
                      <div class="progress progress-sm mb-1" style="width: 100px;">
                        <div 
                          class="progress-bar" 
                          :class="getProgressBarClass(course.progress)"
                          :style="`width: ${course.progress}%`"
                        ></div>
                      </div>
                      <small class="text-muted">{{ course.progress }}%</small>
                    </td>
                    <td>
                      <span class="badge" :class="getStatusBadgeClass(course.status)">
                        {{ course.status }}
                      </span>
                    </td>
                    <td>
                      <div class="d-flex align-items-center">
                        <div class="stars me-1">
                          <i v-for="n in 5" :key="n" class="fas fa-star" :class="n <= course.rating ? 'text-warning' : 'text-muted'" style="font-size: 12px;"></i>
                        </div>
                        <small class="text-muted">({{ course.reviews }})</small>
                      </div>
                    </td>
                    <td>
                      <div class="d-flex gap-1">
                        <button 
                          class="btn btn-primary btn-sm"
                          @click="continueCourse(course)"
                        >
                          {{ course.progress > 0 ? 'Continue' : 'Start' }}
                        </button>
                        <button 
                          class="btn btn-outline-secondary btn-sm"
                          @click="viewCourse(course)"
                        >
                          <i class="fas fa-eye"></i>
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-if="filteredCourses.length === 0" class="row">
      <div class="col-12">
        <div class="card card-round">
          <div class="card-body text-center py-5">
            <i class="fas fa-search fa-3x text-muted mb-3"></i>
            <h5>No courses found</h5>
            <p class="text-muted">Try adjusting your filters or search terms</p>
            <button class="btn btn-primary" @click="clearFilters">Clear Filters</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyCourses',
  layout: 'student',
  data() {
    return {
      userName: '',
      searchQuery: '',
      selectedFilter: 'all',
      selectedCategory: 'all',
      viewMode: 'grid',
      courses: [
        {
          id: 1,
          title: 'Advanced JavaScript Development',
          description: 'Master modern JavaScript concepts including ES6+, async/await, modules, and advanced DOM manipulation techniques.',
          instructor: 'Dr. Sarah Johnson',
          instructorTitle: 'Senior JavaScript Developer',
          instructorAvatar: null, // Will show initials SJ
          category: 'Programming',
          image: null, // Will show placeholder
          progress: 75,
          status: 'In Progress',
          rating: 4.8,
          reviews: 245,
          duration: '12 weeks',
          lessons: 48,
          level: 'Advanced',
          totalHours: 36
        },
        {
          id: 2,
          title: 'Web Design Fundamentals',
          description: 'Learn the principles of modern web design including typography, color theory, layout, and responsive design.',
          instructor: 'Prof. Mike Chen',
          instructorTitle: 'UX/UI Design Expert',
          instructorAvatar: null, // Will show initials MC
          category: 'Design',
          image: null, // Will show placeholder
          progress: 45,
          status: 'In Progress',
          rating: 4.6,
          reviews: 189,
          duration: '8 weeks',
          lessons: 32,
          level: 'Beginner',
          totalHours: 24
        },
        {
          id: 3,
          title: 'Database Systems & SQL',
          description: 'Comprehensive guide to database design, SQL queries, normalization, and database optimization techniques.',
          instructor: 'Dr. Emily Rodriguez',
          instructorTitle: 'Database Architect',
          instructorAvatar: null, // Will show initials ER
          category: 'Programming',
          image: null, // Will show placeholder
          progress: 30,
          status: 'In Progress',
          rating: 4.7,
          reviews: 156,
          duration: '10 weeks',
          lessons: 40,
          level: 'Intermediate',
          totalHours: 30
        },
        {
          id: 4,
          title: 'Digital Marketing Mastery',
          description: 'Complete digital marketing course covering SEO, SEM, social media marketing, email campaigns, and analytics.',
          instructor: 'Lisa Thompson',
          instructorTitle: 'Marketing Strategist',
          instructorAvatar: null, // Will show initials LT
          category: 'Business',
          image: null, // Will show placeholder
          progress: 100,
          status: 'Completed',
          rating: 4.9,
          reviews: 312,
          duration: '6 weeks',
          lessons: 24,
          level: 'Intermediate',
          totalHours: 18
        },
        {
          id: 5,
          title: 'Data Science with Python',
          description: 'Learn data analysis, visualization, and machine learning using Python, pandas, matplotlib, and scikit-learn.',
          instructor: 'Dr. Alex Kumar',
          instructorTitle: 'Data Science Lead',
          instructorAvatar: null, // Will show initials AK
          category: 'Data',
          image: null, // Will show placeholder
          progress: 0,
          status: 'Not Started',
          rating: 4.8,
          reviews: 198,
          duration: '14 weeks',
          lessons: 56,
          level: 'Advanced',
          totalHours: 42
        },
        {
          id: 6,
          title: 'Mobile App Development',
          description: 'Build cross-platform mobile applications using React Native and Flutter with modern development practices.',
          instructor: 'James Wilson',
          instructorTitle: 'Mobile App Developer',
          instructorAvatar: null, // Will show initials JW
          category: 'Programming',
          image: null, // Will show placeholder
          progress: 85,
          status: 'In Progress',
          rating: 4.5,
          reviews: 134,
          duration: '12 weeks',
          lessons: 48,
          level: 'Intermediate',
          totalHours: 36
        }
      ]
    }
  },
  computed: {
    filteredCourses() {
      let filtered = this.courses

      // Filter by status
      if (this.selectedFilter !== 'all') {
        filtered = filtered.filter(course => {
          const status = course.status.toLowerCase().replace(' ', '-')
          return status === this.selectedFilter
        })
      }

      // Filter by category
      if (this.selectedCategory !== 'all') {
        filtered = filtered.filter(course => 
          course.category.toLowerCase() === this.selectedCategory.toLowerCase()
        )
      }

      // Filter by search query
      if (this.searchQuery.trim()) {
        const query = this.searchQuery.toLowerCase()
        filtered = filtered.filter(course =>
          course.title.toLowerCase().includes(query) ||
          course.instructor.toLowerCase().includes(query) ||
          course.description.toLowerCase().includes(query)
        )
      }

      return filtered
    },
    inProgressCount() {
      return this.courses.filter(course => course.status === 'In Progress').length
    },
    completedCount() {
      return this.courses.filter(course => course.status === 'Completed').length
    },
    totalHours() {
      return this.courses.reduce((total, course) => {
        if (course.status === 'Completed') {
          return total + course.totalHours
        } else if (course.status === 'In Progress') {
          return total + Math.round(course.totalHours * (course.progress / 100))
        }
        return total
      }, 0)
    },
    certificatesCount() {
      return this.courses.filter(course => course.status === 'Completed').length
    }
  },
  mounted() {
    this.checkAuth()
    this.loadUserData()
  },
  methods: {
    checkAuth() {
      // Check if user is authenticated
      if (process.client) {
        const token = localStorage.getItem('kai_access_token')
        if (!token) {
          this.$router.push('/kaiadmin/login')
          return
        }
      }
    },
    
    loadUserData() {
      if (process.client) {
        const userData = localStorage.getItem('kai_user')
        if (userData) {
          const user = JSON.parse(userData)
          this.userName = user.name || user.email || 'Student'
        } else {
          this.userName = 'Student'
        }
      }
    },
    
    getStatusBadgeClass(status) {
      switch (status) {
        case 'Completed':
          return 'bg-success'
        case 'In Progress':
          return 'bg-info'
        case 'Not Started':
          return 'bg-secondary'
        default:
          return 'bg-primary'
      }
    },
    
    getProgressBarClass(progress) {
      if (progress >= 80) return 'bg-success'
      if (progress >= 60) return 'bg-info'
      if (progress >= 40) return 'bg-warning'
      return 'bg-danger'
    },
    
    continueCourse(course) {
      // TODO: Implement course navigation
      console.log('Continue course:', course.title)
      // this.$router.push(`/student/course/${course.id}/lesson`)
    },
    
    viewCourse(course) {
      // TODO: Implement course details view
      console.log('View course:', course.title)
      // this.$router.push(`/student/course/${course.id}`)
    },
    
    clearFilters() {
      this.searchQuery = ''
      this.selectedFilter = 'all'
      this.selectedCategory = 'all'
    },
    
    getInstructorInitials(name) {
      // Get first letter of each word, max 2 letters
      return name.split(' ')
                .map(word => word.charAt(0).toUpperCase())
                .slice(0, 2)
                .join('')
    }
  }
}
</script>

<style scoped>
/* Course Card Styles */
.course-card {
  border: none;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.3s ease;
  box-shadow: 0 4px 6px rgba(0,0,0,0.07);
}

/* Course Image Placeholder */
.course-image-placeholder {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.course-image-wrapper {
  height: 200px;
}

.course-image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Instructor Avatar Styles */
.instructor-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.instructor-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.instructor-initials {
  background-color: #007bff;
  color: white;
  font-weight: 600;
  font-size: 12px;
}

.course-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 24px rgba(0,0,0,0.15);
}

.course-image {
  position: relative;
  height: 200px;
  overflow: hidden;
}

.course-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.course-card:hover .course-image img {
  transform: scale(1.05);
}

.course-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  z-index: 2;
}

.course-actions {
  position: absolute;
  top: 12px;
  right: 12px;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 2;
}

.course-card:hover .course-actions {
  opacity: 1;
}

.course-action-btn {
  width: 32px;
  height: 32px;
  padding: 0;
  margin-left: 4px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.course-category {
  background-color: #f8f9fa;
  color: #6c757d;
  font-size: 12px;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.course-rating {
  display: flex;
  align-items: center;
}

.stars i {
  font-size: 14px;
}

.instructor-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.progress-sm {
  height: 6px;
}

/* List View Styles */
.course-list-table th {
  border-top: none;
  font-weight: 600;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #8392a5;
  padding: 20px 15px 10px;
}

.course-list-table td {
  padding: 15px;
  border-top: 1px solid #f0f0f0;
  vertical-align: middle;
}

.course-list-row:hover {
  background-color: rgba(0, 123, 255, 0.05);
}

.course-list-image {
  width: 60px;
  height: 40px;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.course-list-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.course-list-placeholder {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

/* Stats Cards */
.card-stats .icon-big {
  width: 70px;
  height: 70px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
}

.card-stats .numbers p {
  margin-bottom: 5px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.card-stats .numbers h4 {
  font-size: 28px;
  font-weight: 700;
  margin: 0;
}

/* Filter Controls */
.form-select-sm {
  padding: 6px 12px;
  font-size: 14px;
}

.search-box .input-group-text {
  background-color: #f8f9fa;
  border-color: #dee2e6;
  color: #6c757d;
}

/* View Toggle */
.view-toggle .btn-group .btn {
  border-color: #dee2e6;
}

.view-toggle .btn-group .btn.active {
  background-color: #007bff;
  border-color: #007bff;
  color: white;
}

/* Responsive Design */
@media (max-width: 768px) {
  .course-image {
    height: 160px;
  }
  
  .card-stats .icon-big {
    width: 50px;
    height: 50px;
  }
  
  .card-stats .numbers h4 {
    font-size: 24px;
  }
  
  .course-card {
    margin-bottom: 20px;
  }
  
  .d-flex.align-items-center.justify-content-between.flex-wrap > div {
    width: 100%;
    margin-bottom: 1rem;
  }
  
  .d-flex.align-items-center.justify-content-between.flex-wrap > div:last-child {
    margin-bottom: 0;
  }
  
  .search-box .input-group input {
    min-width: 150px !important;
  }
}

@media (max-width: 576px) {
  .course-stats .row .col-4 {
    margin-bottom: 8px;
  }
  
  .course-list-image {
    width: 50px;
    height: 35px;
  }
  
  .course-list-table td {
    padding: 10px 8px;
  }
  
  .course-list-table .d-flex.gap-1 {
    flex-direction: column;
    gap: 4px !important;
  }
  
  .course-list-table .btn-sm {
    padding: 4px 8px;
    font-size: 12px;
  }
}
</style>