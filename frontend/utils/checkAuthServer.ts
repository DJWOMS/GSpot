import { fetchServerSide } from 'lib/fetchServerSide'
import { cookies } from 'next/headers'

export const checkAuthServer = (): boolean => {
  const cookieStore = cookies()
  const accessToken = cookieStore.get('access_token')

  if (accessToken) return true

  const refreshToken = cookieStore.get('refresh_token')

  if (refreshToken) {
    fetchServerSide({
      path: '/auth/refresh',
      body: JSON.stringify({ refresh_token: refreshToken }),
      method: 'POST',
    }).then(() => {
      const accessToken = cookieStore.get('access_token')

      if (accessToken) return true
    })
  }

  return false
}
