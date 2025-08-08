import path from 'path'

export const routes = [
  {
    name: 'starting',
    path: '/starting',
    component: path.resolve(__dirname, 'pages/starting.vue'),
  },
  
  // KAI Admin Routes
  {
    name: 'kaiadmin-dashboard',
    path: '/kaiadmin/dashboard',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'),
  },
  
  // Components Routes
  {
    name: 'kaiadmin-avatars',
    path: '/kaiadmin/components/avatars',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-buttons',
    path: '/kaiadmin/components/buttons',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'),
  },
  {
    name: 'kaiadmin-gridsystem',
    path: '/kaiadmin/components/gridsystem',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-panels',
    path: '/kaiadmin/components/panels',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-notifications',
    path: '/kaiadmin/components/notifications',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-sweetalert',
    path: '/kaiadmin/components/sweetalert',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-font-awesome-icons',
    path: '/kaiadmin/components/font-awesome-icons',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-simple-line-icons',
    path: '/kaiadmin/components/simple-line-icons',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  {
    name: 'kaiadmin-typography',
    path: '/kaiadmin/components/typography',
    component: path.resolve(__dirname, 'pages/kaiadmin/components/buttons.vue'), // Using buttons as placeholder
  },
  
  // Layout Routes
  {
    name: 'kaiadmin-sidebar-style-2',
    path: '/kaiadmin/layouts/sidebar-style-2',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  {
    name: 'kaiadmin-icon-menu',
    path: '/kaiadmin/layouts/icon-menu',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  
  // Forms Routes
  {
    name: 'kaiadmin-forms-basic',
    path: '/kaiadmin/forms/basic',
    component: path.resolve(__dirname, 'pages/kaiadmin/forms/basic.vue'),
  },
  
  // Tables Routes
  {
    name: 'kaiadmin-tables-basic',
    path: '/kaiadmin/tables/basic',
    component: path.resolve(__dirname, 'pages/kaiadmin/tables/basic.vue'),
  },
  {
    name: 'kaiadmin-tables-datatables',
    path: '/kaiadmin/tables/datatables',
    component: path.resolve(__dirname, 'pages/kaiadmin/tables/basic.vue'), // Using basic tables as placeholder
  },
  
  // Maps Routes
  {
    name: 'kaiadmin-maps-googlemaps',
    path: '/kaiadmin/maps/googlemaps',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  {
    name: 'kaiadmin-maps-jsvectormap',
    path: '/kaiadmin/maps/jsvectormap',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  
  // Charts Routes
  {
    name: 'kaiadmin-charts-chartjs',
    path: '/kaiadmin/charts/chartjs',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  {
    name: 'kaiadmin-charts-sparkline',
    path: '/kaiadmin/charts/sparkline',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  
  // Widgets Route
  {
    name: 'kaiadmin-widgets',
    path: '/kaiadmin/widgets',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  
  // Documentation Route
  {
    name: 'kaiadmin-documentation',
    path: '/kaiadmin/documentation',
    component: path.resolve(__dirname, 'pages/kaiadmin/dashboard.vue'), // Using dashboard as placeholder
  },
  
  // // Original Demo Routes
  // {
  //   name: 'test1',
  //   path: '/demo/test1',
  //   component: path.resolve(__dirname, 'pages/demo/index.vue'),
  // },
  // {
  //   name: 'users',
  //   path: '/demo/users',
  //   component: path.resolve(__dirname, 'pages/demo/users.vue'),
  // },
  // {
  //   name: 'courses',
  //   path: '/demo/courses',
  //   component: path.resolve(__dirname, 'pages/demo/courses.vue'),
  // },
  
  // Bootstrap & Samples Routes
  // {
  //   name: 'bootstrap',
  //   path: '/bootstrap',
  //   component: path.resolve(__dirname, 'pages/bootstrap/home.vue'),
  // },
  // {
  //   name: 'new_test',
  //   path: '/bootstrap/new_test',
  //   component: path.resolve(__dirname, 'pages/bootstrap/new_test.vue'),
  // },
  // {
  //   name: 'samples',
  //   path: '/samples',
  //   component: path.resolve(__dirname, 'pages/samples/index.vue'),
  // },
  // {
  //   name: 'samples_home',
  //   path: '/samples/home',
  //   component: path.resolve(__dirname, 'pages/samples/home.vue'),
  // },
  

]
