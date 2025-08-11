export default function ({ redirect, route }) {
  // Client-side authentication check
  if (process.client) {
    const token = localStorage.getItem('kai_access_token')
    
    // If no token and trying to access protected routes
    if (!token && route.path.startsWith('/student')) {
      return redirect('/kaiadmin/login')
    }
    
    // If logged in and trying to access login page
    if (token && route.path === '/kaiadmin/login') {
      return redirect('/student/dashboard')
    }
  }
}