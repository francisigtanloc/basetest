<template>
  <div>
    <div class="container">
      <div class="page-inner">
        <!-- Page Header -->
        <div class="d-flex align-items-left align-items-md-center flex-column flex-md-row pt-2 pb-4">
          <div>
            <h3 class="fw-bold mb-3">Dashboard</h3>
            <h6 class="op-7 mb-2">Free Bootstrap 5 Admin Dashboard</h6>
          </div>
          <div class="ms-md-auto py-2 py-md-0">
            <a href="#" class="btn btn-label-info btn-round me-2">Manage</a>
            <a href="#" class="btn btn-primary btn-round">Add Customer</a>
          </div>
        </div>

        <!-- Statistics Cards Row -->
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
                      <p class="card-category">Visitors</p>
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
                      <p class="card-category">Subscribers</p>
                      <h4 class="card-title">1303</h4>
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
                      <i class="fas fa-luggage-cart"></i>
                    </div>
                  </div>
                  <div class="col col-stats ms-3 ms-sm-0">
                    <div class="numbers">
                      <p class="card-category">Sales</p>
                      <h4 class="card-title">$ 1,345</h4>
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
                      <p class="card-category">Order</p>
                      <h4 class="card-title">576</h4>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Charts Row -->
        <div class="row">
          <div class="col-md-8">
            <div class="card card-round">
              <div class="card-header">
                <div class="card-head-row">
                  <div class="card-title">Statistics</div>
                  <div class="card-tools">
                    <a href="#" class="btn btn-label-success btn-round btn-sm me-2">
                      <span class="btn-label">
                        <i class="fa fa-pencil"></i>
                      </span>
                      Export
                    </a>
                    <a href="#" class="btn btn-label-info btn-round btn-sm">
                      <span class="btn-label">
                        <i class="fa fa-print"></i>
                      </span>
                      Print
                    </a>
                  </div>
                </div>
              </div>
              <div class="card-body">
                <div class="chart-container" style="min-height: 375px">
                  <canvas id="statisticsChart"></canvas>
                </div>
                <div id="myChartLegend"></div>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card card-primary card-round">
              <div class="card-header">
                <div class="card-head-row">
                  <div class="card-title">Daily Sales</div>
                  <div class="card-tools">
                    <div class="dropdown">
                      <button
                        class="btn btn-sm btn-label-light dropdown-toggle"
                        type="button"
                        data-bs-toggle="dropdown"
                        aria-haspopup="true"
                        aria-expanded="false"
                      >
                        Export
                      </button>
                      <div class="dropdown-menu">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Separated link</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="card-body pb-0">
                <div class="mb-4 mt-2">
                  <h1>$4,578.58</h1>
                </div>
                <div class="pull-in">
                  <canvas id="dailySalesChart"></canvas>
                </div>
              </div>
            </div>
            <div class="card card-round">
              <div class="card-body pb-0">
                <div class="h1 fw-bold float-end text-primary">+5%</div>
                <h2 class="mb-2">17</h2>
                <p class="text-muted">Users online</p>
                <div class="pull-in sparkline-fix">
                  <div id="lineChart"></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Tasks and User Statistics Row -->
        <div class="row">
          <div class="col-md-6">
            <div class="card card-round">
              <div class="card-header">
                <div class="card-head-row card-tools-still-right">
                  <div class="card-title">Tasks</div>
                  <div class="card-tools">
                    <div class="dropdown">
                      <button
                        class="btn btn-sm btn-label-light dropdown-toggle"
                        type="button"
                        data-bs-toggle="dropdown"
                        aria-haspopup="true"
                        aria-expanded="false"
                      >
                        Export
                      </button>
                      <div class="dropdown-menu">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Separated link</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="card-body p-0">
                <div class="table-responsive">
                  <table class="table align-items-center mb-0">
                    <thead class="thead-light">
                      <tr>
                        <th scope="col">Task</th>
                        <th scope="col" class="text-end">Progress</th>
                        <th scope="col" class="text-end">Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">
                          <button class="btn btn-icon btn-round btn-sm btn-primary me-2">
                            <i class="fa fa-envelope"></i>
                          </button>
                          Fix Website Issue
                        </th>
                        <td class="text-end">95%</td>
                        <td class="text-end">
                          <span class="badge badge-success">Complete</span>
                        </td>
                      </tr>
                      <tr>
                        <th scope="row">
                          <button class="btn btn-icon btn-round btn-sm btn-warning me-2">
                            <i class="fa fa-bell"></i>
                          </button>
                          Add new feature
                        </th>
                        <td class="text-end">60%</td>
                        <td class="text-end">
                          <span class="badge badge-warning">In Progress</span>
                        </td>
                      </tr>
                      <tr>
                        <th scope="row">
                          <button class="btn btn-icon btn-round btn-sm btn-danger me-2">
                            <i class="fa fa-phone"></i>
                          </button>
                          Call John Doe
                        </th>
                        <td class="text-end">30%</td>
                        <td class="text-end">
                          <span class="badge badge-danger">Pending</span>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card card-round">
              <div class="card-header">
                <div class="card-head-row">
                  <div class="card-title">User Statistics</div>
                  <div class="card-tools">
                    <div class="btn-group dropdown">
                      <button
                        type="button"
                        class="btn btn-sm btn-label-info dropdown-toggle"
                        data-bs-toggle="dropdown"
                        aria-haspopup="true"
                        aria-expanded="false"
                      >
                        <i class="fa fa-cog"></i>
                      </button>
                      <div class="dropdown-menu" role="menu">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <a class="dropdown-item" href="#">Something else here</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Separated link</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="card-body">
                <ol class="activity-feed">
                  <li class="feed-item feed-item-secondary">
                    <time class="date" datetime="9-25">Sep 25</time>
                    <span class="text">Responded to need <a href="#">"Volunteer opportunity"</a></span>
                  </li>
                  <li class="feed-item feed-item-success">
                    <time class="date" datetime="9-24">Sep 24</time>
                    <span class="text">Added an interest <a href="#">"Volunteer Activities"</a></span>
                  </li>
                  <li class="feed-item feed-item-info">
                    <time class="date" datetime="9-23">Sep 23</time>
                    <span class="text">Joined the group <a href="#">"Boardsmanship Forum"</a></span>
                  </li>
                  <li class="feed-item feed-item-warning">
                    <time class="date" datetime="9-21">Sep 21</time>
                    <span class="text">Responded to need <a href="#">"In-Kind Opportunity"</a></span>
                  </li>
                  <li class="feed-item feed-item-danger">
                    <time class="date" datetime="9-18">Sep 18</time>
                    <span class="text">Created need <a href="#">"Volunteer Opportunity"</a></span>
                  </li>
                  <li class="feed-item">
                    <time class="date" datetime="9-17">Sep 17</time>
                    <span class="text">Attending the event <a href="#">"Some New Event"</a></span>
                  </li>
                </ol>
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
  name: 'KaiAdminDashboard',
  layout: 'kaiadmin',
  mounted() {
    // Client-side only: Load Chart.js and initialize charts
    if (process.client) {
      this.loadChartAssets()
    }
  },
  methods: {
    async loadChartAssets() {
      try {
        // Import Chart.js dynamically like the samples page
        await import('@basetest/assets/chartjs/chart.umd.js')
        console.log('Chart.js loaded successfully for dashboard')
        
        // Wait for DOM and other assets to be ready
        this.$nextTick(() => {
          setTimeout(() => {
            this.initializeCharts()
          }, 500) // Give extra time for layout assets to load
        })
        
      } catch (error) {
        console.error('Failed to load Chart.js:', error)
      }
    },
    initializeCharts() {
      // Statistics Chart
      const statisticsChart = document.getElementById('statisticsChart')
      if (statisticsChart) {
        const ctx = statisticsChart.getContext('2d')
        const chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
              label: 'Subscribers',
              borderColor: '#1d7af3',
              pointBorderColor: '#FFF',
              pointBackgroundColor: '#1d7af3',
              pointBorderWidth: 2,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 1,
              pointRadius: 4,
              backgroundColor: 'transparent',
              fill: true,
              borderWidth: 2,
              data: [542, 480, 430, 550, 530, 453, 380, 434, 568, 610, 700, 900]
            }, {
              label: 'New Visitors',
              borderColor: '#59d05d',
              pointBorderColor: '#FFF',
              pointBackgroundColor: '#59d05d',
              pointBorderWidth: 2,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 1,
              pointRadius: 4,
              backgroundColor: 'transparent',
              fill: true,
              borderWidth: 2,
              data: [240, 300, 340, 250, 290, 200, 230, 300, 252, 200, 230, 400]
            }, {
              label: 'Active Users',
              borderColor: '#f3545d',
              pointBorderColor: '#FFF',
              pointBackgroundColor: '#f3545d',
              pointBorderWidth: 2,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 1,
              pointRadius: 4,
              backgroundColor: 'transparent',
              fill: true,
              borderWidth: 2,
              data: [345, 390, 330, 400, 380, 343, 342, 434, 568, 610, 700, 900]
            }]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                display: false
              },
              tooltip: {
                bodySpacing: 4,
                mode: "nearest",
                intersect: false,
                position: "nearest",
                padding: 10,
                caretPadding: 10
              }
            },
            layout: {
              padding: { left: 5, right: 5, top: 15, bottom: 15 }
            },
            scales: {
              y: {
                ticks: {
                  font: { weight: "500" },
                  beginAtZero: false,
                  maxTicksLimit: 5,
                  padding: 20
                },
                grid: {
                  drawTicks: false,
                  display: false
                }
              },
              x: {
                grid: {
                  color: "transparent"
                },
                ticks: {
                  padding: 20,
                  font: { weight: "500" }
                }
              }
            },
            // Legend callback removed for Chart.js v4 compatibility
          }
        })
        
        // Generate legend for Chart.js v4
        const legendContainer = document.getElementById('myChartLegend')
        if (legendContainer && chart.data.datasets) {
          const legendHTML = chart.data.datasets.map(dataset => 
            `<li><span style="background-color:${dataset.borderColor}"></span>${dataset.label}</li>`
          ).join('')
          legendContainer.innerHTML = `<ul class="${chart.canvas.id}-legend html-legend">${legendHTML}</ul>`
        }
      }

      // Daily Sales Chart
      const dailySalesChart = document.getElementById('dailySalesChart')
      if (dailySalesChart) {
        const ctx2 = dailySalesChart.getContext('2d')
        new Chart(ctx2, {
          type: 'line',
          data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            datasets: [{
              label: 'Sales Analytics',
              fill: !0,
              backgroundColor: 'rgba(255,255,255,0.2)',
              borderColor: '#fff',
              borderCapStyle: 'butt',
              borderDash: [],
              borderWidth: 2,
              pointBorderColor: '#fff',
              pointBackgroundColor: '#fff',
              pointBorderWidth: 1,
              pointHoverRadius: 5,
              pointHoverBackgroundColor: '#fff',
              pointHoverBorderColor: '#fff',
              pointHoverBorderWidth: 1,
              pointRadius: 1,
              pointHitRadius: 10,
              data: [65, 59, 80, 81, 56, 55, 40, 35, 30, 20, 25, 30]
            }]
          },
          options: {
            maintainAspectRatio: false,
            plugins: {
              legend: {
                display: false
              }
            },
            animation: {
              easing: 'easeInOutBack'
            },
            scales: {
              y: {
                display: false
              },
              x: {
                display: false
              }
            },
            elements: {
              line: {
                borderWidth: 1
              },
              point: {
                radius: 4
              }
            },
            layout: {
              padding: {
                left: 0,
                right: 0,
                top: 15,
                bottom: 15
              }
            }
          }
        })
      }

      // Initialize sparklines
      if (window.$) {
        $('#lineChart').sparkline([102, 109, 120, 99, 110, 105, 115], {
          type: 'line',
          height: '70',
          width: '100%',
          lineWidth: '2',
          lineColor: '#177dff',
          fillColor: 'rgba(23, 125, 255, 0.14)'
        })
      }
    }
  }
}
</script>