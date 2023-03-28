interface fetchProps<B extends BodyInit | undefined = undefined> {
  body?: B
  method?: 'POST' | 'GET' | 'PUT' | 'DELETE'
  path: string
}

export const fetchServerSide = async <T, D extends BodyInit | undefined = undefined>({ path, ...props }: fetchProps<D>): Promise<T> => {
  try {
    const res = await fetch(`http://127.0.0.1:3100/api${path}`, {
      ...props,
    })

    if (!res.ok) {
      return [] as T
    }

    return (await res.json()) as T
  } catch (error) {
    console.log(error)
    return [] as T
  }
}
