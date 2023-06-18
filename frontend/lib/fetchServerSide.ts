import { API_URL } from 'configs'
import checkAuthClient from 'features/auth/utils/checkAuthClient'
import { errorHandler } from './errorHandler'

interface fetchProps extends RequestInit {
  method?: 'POST' | 'GET' | 'PUT' | 'DELETE'
  headers?: HeadersInit
  path: string
  cache?: 'no-store' | 'reload' | 'no-cache' | 'force-cache'
  error?: boolean
}

export const fetchServerSide = async <T>({
  path,
  cache = 'no-cache',
  ...props
}: fetchProps): Promise<T | undefined> => {
  try {
    const res = await fetch(`${API_URL}${path}`, {
      ...props,
      cache,
    })

    if (!res.ok) {
      if (res.status === 403 && typeof window === 'undefined' && !props.error) {
        if (await checkAuthClient()) {
          return await fetchServerSide({ path, cache, ...props, error: true })
        }
      }

      await errorHandler(res.status)
    }

    return await res.json()
  } catch (error) {
    console.log(error)
  }
}
