<template>
  <div>
    <div class="container">
      <div class="page-inner">
        <div class="page-header">
          <h3 class="fw-bold mb-3">Tables</h3>
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
              <nuxt-link to="#">Tables</nuxt-link>
            </li>
            <li class="separator">
              <i class="icon-arrow-right"></i>
            </li>
            <li class="nav-item">
              <a href="#">Basic Table</a>
            </li>
          </ul>
        </div>
        
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Basic Table</div>
              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-hover">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                        <th scope="col">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(item, index) in basicTableData" :key="index">
                        <td>{{ item.id }}</td>
                        <td>{{ item.first }}</td>
                        <td>{{ item.last }}</td>
                        <td>{{ item.handle }}</td>
                        <td>
                          <div class="form-button-action">
                            <button type="button" data-bs-toggle="tooltip" title="" class="btn btn-link btn-primary btn-lg" data-original-title="Edit Task" @click="editItem(item)">
                              <i class="fa fa-edit"></i>
                            </button>
                            <button type="button" data-bs-toggle="tooltip" title="" class="btn btn-link btn-danger" data-original-title="Remove" @click="removeItem(item.id)">
                              <i class="fa fa-times"></i>
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
        
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Striped Table</div>
              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-striped">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Position</th>
                        <th scope="col">Office</th>
                        <th scope="col">Age</th>
                        <th scope="col">Start date</th>
                        <th scope="col">Salary</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(employee, index) in employeeData" :key="index">
                        <td>{{ employee.id }}</td>
                        <td>{{ employee.name }}</td>
                        <td>{{ employee.position }}</td>
                        <td>{{ employee.office }}</td>
                        <td>{{ employee.age }}</td>
                        <td>{{ employee.startDate }}</td>
                        <td>{{ employee.salary }}</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Bordered Table</div>
              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-bordered">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">1</th>
                        <td>Mark</td>
                        <td>Otto</td>
                        <td>@mdo</td>
                      </tr>
                      <tr>
                        <th scope="row">2</th>
                        <td>Jacob</td>
                        <td>Thornton</td>
                        <td>@fat</td>
                      </tr>
                      <tr>
                        <th scope="row">3</th>
                        <td>Larry</td>
                        <td>the Bird</td>
                        <td>@twitter</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Borderless Table</div>
              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table table-borderless">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">1</th>
                        <td>Mark</td>
                        <td>Otto</td>
                        <td>@mdo</td>
                      </tr>
                      <tr>
                        <th scope="row">2</th>
                        <td>Jacob</td>
                        <td>Thornton</td>
                        <td>@fat</td>
                      </tr>
                      <tr>
                        <th scope="row">3</th>
                        <td>Larry</td>
                        <td>the Bird</td>
                        <td>@twitter</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <div class="card-header">
                <div class="card-title">Table with Head Options</div>
              </div>
              <div class="card-body">
                <div class="table-responsive">
                  <table class="table">
                    <thead class="thead-light">
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">First</th>
                        <th scope="col">Last</th>
                        <th scope="col">Handle</th>
                        <th scope="col">Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(user, index) in statusTableData" :key="index">
                        <th scope="row">{{ user.id }}</th>
                        <td>{{ user.first }}</td>
                        <td>{{ user.last }}</td>
                        <td>{{ user.handle }}</td>
                        <td>
                          <span class="badge" :class="getBadgeClass(user.status)">
                            {{ user.status }}
                          </span>
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'BasicTablesPage',
  layout: 'kaiadmin',
  data() {
    return {
      basicTableData: [
        { id: 1, first: 'Mark', last: 'Otto', handle: '@mdo' },
        { id: 2, first: 'Jacob', last: 'Thornton', handle: '@fat' },
        { id: 3, first: 'Larry', last: 'the Bird', handle: '@twitter' },
        { id: 4, first: 'John', last: 'Doe', handle: '@johndoe' },
        { id: 5, first: 'Jane', last: 'Smith', handle: '@janesmith' }
      ],
      employeeData: [
        {
          id: 1,
          name: 'Tiger Nixon',
          position: 'System Architect',
          office: 'Edinburgh',
          age: 61,
          startDate: '2011/04/25',
          salary: '$320,800'
        },
        {
          id: 2,
          name: 'Garrett Winters',
          position: 'Accountant',
          office: 'Tokyo',
          age: 63,
          startDate: '2011/07/25',
          salary: '$170,750'
        },
        {
          id: 3,
          name: 'Ashton Cox',
          position: 'Junior Technical Author',
          office: 'San Francisco',
          age: 66,
          startDate: '2009/01/12',
          salary: '$86,000'
        },
        {
          id: 4,
          name: 'Cedric Kelly',
          position: 'Senior Javascript Developer',
          office: 'Edinburgh',
          age: 22,
          startDate: '2012/03/29',
          salary: '$433,060'
        }
      ],
      statusTableData: [
        { id: 1, first: 'Mark', last: 'Otto', handle: '@mdo', status: 'Active' },
        { id: 2, first: 'Jacob', last: 'Thornton', handle: '@fat', status: 'Pending' },
        { id: 3, first: 'Larry', last: 'the Bird', handle: '@twitter', status: 'Inactive' },
        { id: 4, first: 'John', last: 'Doe', handle: '@johndoe', status: 'Active' },
        { id: 5, first: 'Jane', last: 'Smith', handle: '@janesmith', status: 'Suspended' }
      ]
    }
  },
  head() {
    return {
      title: 'Basic Tables - KAI Admin'
    }
  },
  mounted() {
    // Ensure components are available for tables
    if (process.client) {
      setTimeout(() => {
        if (window.$ && window.jQuery) {
          console.log('Table components initialized')
        }
      }, 1000)
    }
  },
  methods: {
    editItem(item) {
      this.$swal({
        title: 'Edit Item',
        text: `Edit item: ${item.first} ${item.last}`,
        type: 'info',
        confirmButtonText: 'OK'
      })
    },
    
    removeItem(id) {
      this.$swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
      }).then((result) => {
        if (result.value) {
          const index = this.basicTableData.findIndex(item => item.id === id)
          if (index > -1) {
            this.basicTableData.splice(index, 1)
          }
          
          this.$swal(
            'Deleted!',
            'Your item has been deleted.',
            'success'
          )
        }
      })
    },
    
    getBadgeClass(status) {
      switch (status.toLowerCase()) {
        case 'active':
          return 'badge-success'
        case 'pending':
          return 'badge-warning'
        case 'inactive':
          return 'badge-secondary'
        case 'suspended':
          return 'badge-danger'
        default:
          return 'badge-primary'
      }
    }
  }
}
</script>