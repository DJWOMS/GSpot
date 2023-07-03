import { toast } from 'react-hot-toast'
import checkAuthClient from '../features/auth/utils/checkAuthClient'
import { fetchServerSide } from './fetchServerSide'

export const errorHandler = async (error: number) => {
  if (error === 401 && typeof window === 'undefined') {
    const authorized = await checkAuthClient()

    if (!authorized) {
      toast.error('Пользователь не авторизирован')
    }
  }

  if (error === 400) {
    toast.error('Возникла ошибка при авторизации')
  }
}
