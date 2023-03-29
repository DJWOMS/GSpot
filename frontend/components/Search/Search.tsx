'use client'

import s from './Search.module.scss'
import { IconSearch } from '@tabler/icons-react'
import { useEffect, useState } from 'react'
import { useDebounce } from 'hooks'
import { fetchServerSide } from 'lib/fetchServerSide'
import SearchInput from './SearchInput'

const Search = () => {
  const [result, setResult] = useState<{ id: number; name: string }[]>([{ id: 1, name: 'Экшн' }])
  const [query, setQuery] = useState('')

  const debouncedValue = useDebounce(query, 50)

  useEffect(() => {
    if (debouncedValue.length > 3) {
      fetchServerSide<{ id: number; name: string }[]>({
        path: `/search?query=${debouncedValue}`,
      }).then((r) => r && setResult(r))
    } else {
      setResult([])
    }
  }, [debouncedValue])

  return (
    <div className={s.container}>
      <SearchInput onChange={setQuery} result={result} />
      <button className={s.searchBtn}>
        <IconSearch />
      </button>
    </div>
  )
}

export default Search
