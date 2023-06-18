import { toast } from 'react-hot-toast'
import { cookies } from 'next/headers'
import { fetchServerSide } from './fetchServerSide'

export const errorHandler = async (error: number) => {
  if (error === 401) {
    const refreshToken = cookies().get('refresh_token')?.value

    if (refreshToken) {
      try {
        await fetchServerSide({ path: 'auth/refresh', method: 'POST' })
      } catch (e) {
        console.log(e)
      }
    }

    toast.error('Пользователь не авторизирован')
  }

  if (error === 400) {
    toast.error('Возникла ошибка при авторизации')
  }
}
