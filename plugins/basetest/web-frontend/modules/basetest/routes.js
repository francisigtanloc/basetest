import path from 'path'

export const routes = [
  {
    name: 'starting',
    path: '/starting',
    component: path.resolve(__dirname, 'pages/starting.vue'),
  },
  {
    name: 'index',
    path: '/demo/index',
    component: path.resolve(__dirname, 'pages/demo/index.vue'),
  },
  {
    name: 'users',
    path: '/demo/users',
    component: path.resolve(__dirname, 'pages/demo/users.vue'),
  },
  {
    name: 'courses',
    path: '/demo/courses',
    component: path.resolve(__dirname, 'pages/demo/courses.vue'),
  },
  {
    name: 'bootstrap',
    path: '/bootstrap',
    component: path.resolve(__dirname, 'pages/bootstrap/home.vue'),
  },
  {
    name: 'new_test',
    path: '/bootstrap/new_test',
    component: path.resolve(__dirname, 'pages/bootstrap/new_test.vue'),
  },
  {
    name: 'samples',
    path: '/samples',
    component: path.resolve(__dirname, 'pages/samples/index.vue'),
  },
  {
    name: 'samples_home',
    path: '/samples/home',
    component: path.resolve(__dirname, 'pages/samples/home.vue'),
  },
  

]
