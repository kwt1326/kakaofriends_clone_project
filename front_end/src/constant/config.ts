export function serverUrl() {
  switch (process.env.NODE_ENV) {
    case 'production':
      return ''
    case 'development':
    default:
      return 'http://localhost:8000/'
  }
}