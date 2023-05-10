'use client'

import { useEffect, useState } from 'react'
import { IconSearch } from '@tabler/icons-react'
import type { GameCardSimpleInterface } from 'features/games/types'
import { useDebounce } from 'hooks'
import { fetchServerSide } from 'lib/fetchServerSide'
import s from './Search.module.css'
import SearchInput from './SearchInput'

const Search = () => {
  const [result, setResult] = useState<GameCardSimpleInterface[]>()
  const [query, setQuery] = useState('')

  const debouncedValue = useDebounce(query, 50)

  useEffect(() => {
    if (debouncedValue.length > 3) {
      fetchServerSide<GameCardSimpleInterface[]>({
        path: `/games/search?query=${debouncedValue}`,
      }).then((data) => data && setResult(data))
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
