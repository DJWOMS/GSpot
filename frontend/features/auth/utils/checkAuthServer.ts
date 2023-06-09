import { cookies } from 'next/headers'

export const checkAuthServer = async (): Promise<boolean> => {
  const cookieStore = cookies()
  const accessToken = cookieStore.get('access_token')?.value

  if (accessToken) return true

  return false
}
