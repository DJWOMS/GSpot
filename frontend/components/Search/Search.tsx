'use client'

import s from './Search.module.scss'
import { IconSearch } from '@tabler/icons-react'
import { FC, useEffect, useState } from 'react'
import useDebounce from 'lib/useDebounce'
import { fetchServerSide } from 'lib/fetchServerSide'
import Select from '../Select'
import SearchInput from './SearchInput'

interface ICategory {
  id: number
  name: string
}

interface Props {
  categories: ICategory[]
}

const Search: FC<Props> = ({ categories }) => {
  const [result, setResult] = useState<{ id: number; name: string }[]>([{ id: 1, name: 'Экшн' }])
  const [query, setQuery] = useState('')
  const [selectedCategory, setSelectedCategory] = useState<{ id: number; name: string }>({ id: 0, name: 'Все категории' })

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
      <Select selected={selectedCategory} setSelected={setSelectedCategory} options={[{ id: 0, name: 'Все категории' }, ...categories]} />
      <button className={s.searchBtn}>
        <IconSearch />
      </button>
    </div>
  )
}

export default Search
