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

]
