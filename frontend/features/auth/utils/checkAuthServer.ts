import { fetchServerSide } from 'lib/fetchServerSide'
import { cookies } from 'next/headers'
import { refresh_token } from '../auth'

export const checkAuthServer = async (): Promise<boolean> => {
  const cookieStore = cookies()
  const accessToken = cookieStore.get('access_token')

  if (accessToken) return true

  const refreshToken = cookieStore.get('refresh_token')

  if (refreshToken) {
    try {
      await fetchServerSide({
        path: '/auth/refresh',
        method: 'POST',
        headers: {
          cookie: `refresh_token=${refresh_token}`,
        },
      })

      const accessToken = cookieStore.get('access_token')

      if (accessToken) return true
    } catch (error) {
      console.log(error)
    }
  }

  return false
}
