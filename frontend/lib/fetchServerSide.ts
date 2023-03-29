import { API_URL } from 'configs'

interface fetchProps<B extends BodyInit | undefined = undefined> {
  body?: B
  method?: 'POST' | 'GET' | 'PUT' | 'DELETE'
  headers?: HeadersInit
  path: string
  cache?: 'no-store' | 'reload' | 'no-cache' | 'force-cache'
}

export const fetchServerSide = async <T, D extends BodyInit | undefined = undefined>({ path, ...props }: fetchProps<D>): Promise<T | undefined> => {
  try {
    const res = await fetch(`${API_URL}${path}`, {
      ...props,
    })

    if (!res.ok) {
      return
    }

    return await res.json()
  } catch (error) {
    console.log(error)
  }
}
