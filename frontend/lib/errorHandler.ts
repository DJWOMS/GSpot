import { toast } from 'react-hot-toast'
import { fetchServerSide } from './fetchServerSide'
import checkAuthClient from "../features/auth/utils/checkAuthClient";

export const errorHandler = async (error: number) => {
  if (error === 401 && typeof window === 'undefined') {
    const authorized = await checkAuthClient()

    if (authorized) {
      return await fetchServerSide({ path: 'auth/refresh', method: 'POST' })
    } else {
      toast.error('Пользователь не авторизирован')
    }
  }

  if (error === 400) {
    toast.error('Возникла ошибка при авторизации')
  }
}
