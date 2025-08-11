<template>
  <div>
    <!-- Page Header -->
    <div class="d-flex align-items-left align-items-md-center flex-column flex-md-row pt-2 pb-4">
      <div>
        <h3 class="fw-bold mb-3">Welcome back, {{ userName }}!</h3>
        <h6 class="op-7 mb-2">Student Dashboard - Track your learning progress</h6>
      </div>
      <div class="ms-md-auto py-2 py-md-0">
        <nuxt-link to="/student/courses" class="btn btn-label-info btn-round me-2">My Courses</nuxt-link>
        <a href="#" class="btn btn-primary btn-round">View Calendar</a>
      </div>
    </div>

    <!-- Quick Stats Cards Row -->
    <div class="row">
      <div class="col-sm-6 col-md-3">
        <div class="card card-stats card-round">
          <div class="card-body">
            <div class="row align-items-center">
              <div class="col-icon">
                <div class="icon-big text-center icon-primary bubble-shadow-small">
                  <i class="fas fa-book-open"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Enrolled Courses</p>
                  <h4 class="card-title">{{ stats.enrolledCourses }}</h4>
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
                  <i class="fas fa-trophy"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Completed</p>
                  <h4 class="card-title">{{ stats.completedCourses }}</h4>
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
                  <i class="fas fa-clock"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Hours Studied</p>
                  <h4 class="card-title">{{ stats.hoursStudied }}</h4>
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
                  <i class="fas fa-certificate"></i>
                </div>
              </div>
              <div class="col col-stats ms-3 ms-sm-0">
                <div class="numbers">
                  <p class="card-category">Certificates</p>
                  <h4 class="card-title">{{ stats.certificates }}</h4>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content Row -->
    <div class="row">
      <!-- Current Courses -->
      <div class="col-md-8">
        <div class="card card-round">
          <div class="card-header">
            <div class="card-head-row">
              <div class="card-title">Current Courses</div>
              <div class="card-tools">
                <nuxt-link to="/student/courses" class="btn btn-label-success btn-round btn-sm">
                  <span class="btn-label">
                    <i class="fa fa-eye"></i>
                  </span>
                  View All
                </nuxt-link>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="row" v-if="currentCourses.length > 0">
              <div class="col-md-6 mb-3" v-for="course in currentCourses" :key="course.id">
                <div class="card border-left-primary h-100">
                  <div class="card-body">
                    <div class="d-flex align-items-center mb-2">
                      <div class="course-icon me-3">
                        <i :class="course.icon" class="fa-2x text-primary"></i>
                      </div>
                      <div>
                        <h6 class="card-title mb-1">{{ course.name }}</h6>
                        <small class="text-muted">{{ course.instructor }}</small>
                      </div>
                    </div>
                    <div class="progress mb-2">
                      <div 
                        class="progress-bar" 
                        :class="getProgressBarClass(course.progress)"
                        role="progressbar" 
                        :style="`width: ${course.progress}%`"
                        :aria-valuenow="course.progress" 
                        aria-valuemin="0" 
                        aria-valuemax="100"
                      >
                        {{ course.progress }}%
                      </div>
                    </div>
                    <div class="d-flex justify-content-between align-items-center">
                      <small class="text-muted">
                        <i class="fas fa-clock me-1"></i>
                        {{ course.nextDeadline }}
                      </small>
                      <a href="#" class="btn btn-primary btn-sm">Continue</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div v-else class="text-center py-4">
              <i class="fas fa-graduation-cap fa-3x text-muted mb-3"></i>
              <h5>No courses enrolled yet</h5>
              <p class="text-muted">Start your learning journey by browsing available courses</p>
              <a href="#" class="btn btn-primary">Browse Courses</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Learning Progress & Activities -->
      <div class="col-md-4">
        <div class="card card-round mb-3">
          <div class="card-header">
            <div class="card-head-row">
              <div class="card-title">Learning Progress</div>
            </div>
          </div>
          <div class="card-body">
            <div class="progress-card">
              <div class="d-flex justify-content-between mb-1">
                <small class="text-muted">Overall Progress</small>
                <small class="text-muted">{{ overallProgress }}%</small>
              </div>
              <div class="progress mb-3">
                <div 
                  class="progress-bar bg-gradient-primary" 
                  role="progressbar" 
                  :style="`width: ${overallProgress}%`"
                ></div>
              </div>
              
              <div class="achievement-badges">
                <h6 class="mb-2">Recent Achievements</h6>
                <div class="d-flex flex-wrap gap-2">
                  <span class="badge bg-success">First Course Completed</span>
                  <span class="badge bg-info">Week Streak</span>
                  <span class="badge bg-warning">Quiz Master</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Recent Activities -->
        <div class="card card-round">
          <div class="card-header">
            <div class="card-head-row">
              <div class="card-title">Recent Activities</div>
            </div>
          </div>
          <div class="card-body pb-0">
            <div class="activity-feed">
              <div class="activity-item d-flex align-items-start mb-3" v-for="activity in recentActivities" :key="activity.id">
                <div class="activity-icon me-3">
                  <i :class="[activity.icon, activity.iconColor]"></i>
                </div>
                <div class="activity-content">
                  <p class="mb-1">{{ activity.description }}</p>
                  <small class="text-muted">{{ activity.time }}</small>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Upcoming Deadlines Row -->
    <div class="row">
      <div class="col-12">
        <div class="card card-round">
          <div class="card-header">
            <div class="card-head-row">
              <div class="card-title">
                <i class="fas fa-calendar-alt me-2"></i>
                Upcoming Deadlines
              </div>
              <div class="card-tools">
                <a href="#" class="btn btn-label-info btn-round btn-sm">
                  <span class="btn-label">
                    <i class="fa fa-calendar"></i>
                  </span>
                  View Calendar
                </a>
              </div>
            </div>
          </div>
          <div class="card-body">
            <div class="table-responsive">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th>Course</th>
                    <th>Assignment</th>
                    <th>Due Date</th>
                    <th>Status</th>
                    <th>Action</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="deadline in upcomingDeadlines" :key="deadline.id">
                    <td>
                      <div class="d-flex align-items-center">
                        <i :class="deadline.courseIcon" class="me-2 text-primary"></i>
                        {{ deadline.courseName }}
                      </div>
                    </td>
                    <td>{{ deadline.assignment }}</td>
                    <td>
                      <span :class="getDeadlineClass(deadline.daysLeft)">
                        {{ deadline.dueDate }}
                        <small class="d-block text-muted">{{ deadline.daysLeft }} days left</small>
                      </span>
                    </td>
                    <td>
                      <span class="badge" :class="getStatusBadgeClass(deadline.status)">
                        {{ deadline.status }}
                      </span>
                    </td>
                    <td>
                      <a href="#" class="btn btn-primary btn-sm">
                        {{ deadline.status === 'Not Started' ? 'Start' : 'Continue' }}
                      </a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'StudentDashboard',
  layout: 'student',
  data() {
    return {
      userName: '',
      stats: {
        enrolledCourses: 5,
        completedCourses: 2,
        hoursStudied: 47,
        certificates: 3
      },
      overallProgress: 68,
      currentCourses: [
        {
          id: 1,
          name: 'Advanced JavaScript',
          instructor: 'Dr. Sarah Johnson',
          progress: 75,
          nextDeadline: 'Assignment due in 3 days',
          icon: 'fab fa-js-square'
        },
        {
          id: 2,
          name: 'Web Design Fundamentals',
          instructor: 'Prof. Mike Chen',
          progress: 45,
          nextDeadline: 'Quiz due in 1 week',
          icon: 'fas fa-paint-brush'
        },
        {
          id: 3,
          name: 'Database Systems',
          instructor: 'Dr. Emily Rodriguez',
          progress: 30,
          nextDeadline: 'Project due in 2 weeks',
          icon: 'fas fa-database'
        }
      ],
      recentActivities: [
        {
          id: 1,
          description: 'Completed "Functions and Scope" lesson',
          time: '2 hours ago',
          icon: 'fas fa-check-circle',
          iconColor: 'text-success'
        },
        {
          id: 2,
          description: 'Submitted JavaScript Assignment #3',
          time: '1 day ago',
          icon: 'fas fa-file-upload',
          iconColor: 'text-info'
        },
        {
          id: 3,
          description: 'Started "CSS Grid Layout" module',
          time: '2 days ago',
          icon: 'fas fa-play-circle',
          iconColor: 'text-primary'
        },
        {
          id: 4,
          description: 'Earned "Quick Learner" badge',
          time: '3 days ago',
          icon: 'fas fa-medal',
          iconColor: 'text-warning'
        }
      ],
      upcomingDeadlines: [
        {
          id: 1,
          courseName: 'Advanced JavaScript',
          courseIcon: 'fab fa-js-square',
          assignment: 'DOM Manipulation Project',
          dueDate: 'March 15, 2024',
          daysLeft: 3,
          status: 'In Progress'
        },
        {
          id: 2,
          courseName: 'Web Design Fundamentals',
          courseIcon: 'fas fa-paint-brush',
          assignment: 'Responsive Layout Quiz',
          dueDate: 'March 20, 2024',
          daysLeft: 8,
          status: 'Not Started'
        },
        {
          id: 3,
          courseName: 'Database Systems',
          courseIcon: 'fas fa-database',
          assignment: 'SQL Query Assignment',
          dueDate: 'March 25, 2024',
          daysLeft: 13,
          status: 'Not Started'
        }
      ]
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
      // Get user data from localStorage
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
    
    getProgressBarClass(progress) {
      if (progress >= 80) return 'bg-success'
      if (progress >= 60) return 'bg-info'
      if (progress >= 40) return 'bg-warning'
      return 'bg-danger'
    },
    
    getDeadlineClass(daysLeft) {
      if (daysLeft <= 2) return 'text-danger fw-bold'
      if (daysLeft <= 5) return 'text-warning fw-bold'
      return 'text-success'
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
    }
  }
}
</script>

<style scoped>
.border-left-primary {
  border-left: 4px solid #007bff;
}

.course-icon {
  min-width: 40px;
}

.progress-card {
  padding: 10px 0;
}

.achievement-badges .badge {
  font-size: 0.75rem;
  padding: 0.375rem 0.75rem;
}

.activity-feed {
  max-height: 300px;
  overflow-y: auto;
}

.activity-item {
  padding-bottom: 10px;
  border-bottom: 1px solid #f0f0f0;
}

.activity-item:last-child {
  border-bottom: none;
  padding-bottom: 0;
}

.activity-icon {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8f9fa;
  flex-shrink: 0;
}

.activity-icon i {
  font-size: 14px;
}

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

.table th {
  border-top: none;
  font-weight: 600;
  font-size: 13px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  color: #8392a5;
  padding: 20px 15px 10px;
}

.table td {
  padding: 15px;
  border-top: 1px solid #f0f0f0;
  vertical-align: middle;
}

.table-hover tbody tr:hover {
  background-color: rgba(0, 123, 255, 0.05);
}

@media (max-width: 768px) {
  .card-stats .icon-big {
    width: 50px;
    height: 50px;
  }
  
  .card-stats .numbers h4 {
    font-size: 24px;
  }
  
  .activity-feed {
    max-height: 250px;
  }
}
</style>