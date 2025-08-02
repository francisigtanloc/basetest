import path from 'path'

import { routes } from './routes'

export default function () {
  this.options.alias['@basetest'] = path.resolve(
    __dirname,
    './'
  )
  this.addLayout(path.resolve(__dirname, 'layouts/dashboard.vue'), 'dashboard')
  this.addLayout(path.resolve(__dirname, 'layouts/main.vue'), 'main')

  this.extendRoutes((configRoutes) => {
    configRoutes.push(...routes)
  })
  this.appendPlugin({
    src: path.resolve(__dirname, 'plugin.js'),
  })
  this.options.css.push(path.resolve(__dirname, 'assets/scss/default.scss'))
}
