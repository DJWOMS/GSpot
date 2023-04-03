'use client'

import { useState } from 'react'
import s from './FilterGames.module.scss'
import { Genres } from './Genres'
import { Keywords } from './Keywords'
import { Platforms } from './Platforms'
import { Prices } from './Prices'
import { SortBy } from './SortBy'

const FilterGames = () => {
  const [filterState, setFilterState] = useState<Record<string, any>>({})

  const changeFilter = (key: string) => {
    return (data: string | boolean | object) =>
      setFilterState((state) => ({
        ...state,
        [key]:
          typeof data === 'object'
            ? Object.fromEntries(
                Object.entries({
                  ...(key in state ? state[key] : {}),
                  ...data,
                }).filter(([, value]) => !!value)
              )
            : data,
      }))
  }

  const onSubmitForm = () => console.log(filterState)

  return (
    <>
      <button className={s.openFilter}>Открыть фильтр</button>

      <div className={s.wrapper}>
        <div onSubmit={onSubmitForm} className={s.components}>
          <h4 className={s.title}>
            Фильтры <button className={s.clearFilters}>Очистить</button>
          </h4>

          <Keywords onChange={changeFilter('keywords')} />
          <SortBy onChange={changeFilter('sort_by')} />
          <Prices onChange={changeFilter('prices')} />
          <Platforms onChange={changeFilter('platforms')} />
          <Genres onChange={changeFilter('genres')} />

          <div className={s.group}>
            <button className={s.applyFilter} onClick={onSubmitForm}>
              Применить фильтр
            </button>
          </div>
        </div>
      </div>
    </>
  )
}

export { FilterGames }
