import { API_URL } from 'configs'

interface fetchProps extends RequestInit {
  method?: 'POST' | 'GET' | 'PUT' | 'DELETE'
  headers?: HeadersInit
  path: string
  cache?: 'no-store' | 'reload' | 'no-cache' | 'force-cache'
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
      return
    }

    return await res.json()
  } catch (error) {
    console.log(error)
  }
}
